#!/usr/bin/python
from PyQt4.QtCore import (Qt, QStringList)
import subprocess, re

def get_nic_list():
	config = subprocess.check_output("ifconfig")
	expr = re.compile("([a-zA-Z0-9]+)\s+Link")
	interfaces = expr.findall(config)
	return interfaces
if __name__=="__main__":
	from ui_mainwindow1 import Ui_Capture1
	from PyQt4.QtGui import *
	class Window(QMainWindow,Ui_Capture1):
        	def __init__(self,parent=None):
                	super(Window, self).__init__(parent)
                	self.setupUi(self)

                	self.CaptureButton.setFocusPolicy(Qt.NoFocus)
                	self.DetailButton.setFocusPolicy(Qt.NoFocus)
                	self.NIChooser.setFocusPolicy(Qt.NoFocus)
                	self.setWindowIcon(QIcon('icon/mask.ico'))

			self.NIChooser.addItems(QStringList(get_nic_list()))

			self.DisplayTable.setRowCount(1)
                        self.DisplayTable.setItem(0,0,QTableWidgetItem(self.NIChooser.currentText()))
	import sys
        app = QApplication(sys.argv)
        form = Window()
        form.show()
        app.exec_()
