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

from ui_mainwindow1 import Ui_Capture1
import capture
from interfaces import get_nic_list

class InitialWindow(QMainWindow,Ui_Capture1):
	def __init__(self,parent=None):
       		super(InitialWindow, self).__init__(parent)
      	 	self.setupUi(self)
        	
		self.CaptureButton.setFocusPolicy(Qt.NoFocus)
        	self.DetailButton.setFocusPolicy(Qt.NoFocus)
        	self.NIChooser.setFocusPolicy(Qt.NoFocus)
		self.setWindowIcon(QIcon('icon/mask.ico'))
		self.DisplayTable.setEditTriggers(QAbstractItemView.NoEditTriggers)	
		self.NIChooser.addItems(QStringList(get_nic_list()))

		
		self.handle = capture.Capture()
	
	@Slot(bool)
	def on_CaptureButton_clicked(self,checked):
		if checked==1:
			self.CaptureButton.setText(QString("stop"))
			self.DisplayTable.clearContents()
			self.DisplayTable.setRowCount(0)

			t = Thread(target=self.capture,args=())
			t.start()
		else:		
			self.handle.stop_capture
			self.CaptureButton.setText(QString("begin"))

	def capture(self):
		nic = self.NIChooser.currentText()
		self.handle.begin_capture(str(nic))
		while(True):
			result,go = self.handle.capture_packet()
			if(go==0):
				break
			else:
				self.update_Table(result)

	def update_Table(self,result):
		index,ptype,src_ip,dst_ip=result
		if(index and ptype and src_ip and dst_ip):
			self.DisplayTable.setRowCount(index)      
          		self.DisplayTable.setItem(index-1,0,QTableWidgetItem(str(ptype)))
			self.DisplayTable.setItem(index-1,1,QTableWidgetItem(str(src_ip)))
              		self.DisplayTable.setItem(index-1,2,QTableWidgetItem(str(dst_ip)))
		
if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
    	form = InitialWindow()
	form.show()
	app.exec_()
