#!/usr/bin/python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (Qt,QStringList, QString)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
from PyQt4.QtGui import *

from threading import Thread

from ui_mainwindow2 import Ui_Capture2
from interfaces import get_nic_list

class InitialWindow(QMainWindow,Ui_Capture2):
	def __init__(self,parent=None):
       		super(InitialWindow, self).__init__(parent)
      	 	self.setupUi(self)
        	
		self.CaptureButton.setFocusPolicy(Qt.NoFocus)
        	self.DetailButton.setFocusPolicy(Qt.NoFocus)
        	self.NIChooser.setFocusPolicy(Qt.NoFocus)
		self.setWindowIcon(QIcon('../icon/mask.ico'))
		self.DisplayTable.setEditTriggers(QAbstractItemView.NoEditTriggers)	
		self.NIChooser.addItems(QStringList(get_nic_list()))
	


		
if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
    	form = InitialWindow()
	form.show()
	app.exec_()
