#!/usr/bin/python
from __future__ import division
#from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (Qt,QStringList, QString)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
from PyQt4.QtGui import *

from threading import Thread
from time import sleep
from Queue import Queue

from ui_mainwindow import Ui_Capture
from interfaces import get_nic_list
from maindialog import SDialog
from maindialog import FDialog

class InitialWindow(QMainWindow,Ui_Capture):
	def __init__(self,parent=None):
       		super(InitialWindow, self).__init__(parent)
      	 	self.setupUi(self)
        	
		self.CaptureButton.setFocusPolicy(Qt.NoFocus)
        	self.DetailButton.setFocusPolicy(Qt.NoFocus)
        	self.NIChooser.setFocusPolicy(Qt.NoFocus)
		self.setWindowIcon(QIcon('../icon/mask.ico'))
		self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers)	
		self.NIChooser.addItems(QStringList(get_nic_list()))
	
		self.MainTable.verticalHeader().setVisible(False)	
		#signal-slot
		self.DetailButton.clicked.connect(self.show_detail);
		self.MainTable.cellDoubleClicked.connect(self.show_detail);

		self.saveButton.clicked.connect(self.file_save)

        @Slot(bool)
        def on_CaptureButton_clicked(self,checked):
                if checked==1:
                        self.CaptureButton.setText(QString("stop"))
                        self.MainTable.clearContents()
                        self.MainTable.setRowCount(0)
        	
			message='you silly'
                	self.MainTable.setRowCount(1)
			self.MainTable.setItem(0,1,QTableWidgetItem(QString(message)))
			message=1
			self.MainTable.setItem(0,0,QTableWidgetItem(QString(str(message))))
		else:
                        self.CaptureButton.setText(QString("begin"))
			print int(self.MainTable.item(0,0).text())
			print type(int(self.MainTable.item(0,0).text()))
	
	@Slot()
	def on_SearchButton_clicked(self):
		dialog = SDialog(parent=self);
 		if dialog.exec_():
			print dialog.searchtext()
	
	@Slot()
	def on_FilterButton_clicked(self):
		dialog = FDialog(parent=self);
 		if dialog.exec_():
			print dialog.GetCondition()
	
	def show_detail(self):
		m = self.MainTable.currentRow()
		self.DetailViewer.clear()
		if m==-1:message='error!you must choose one row then click showdetail button'
		else:
			message=str(m)*9000
		self.DetailViewer.append(QString(message))

	def file_save(self):
		name = QFileDialog.getSaveFileName(self, 'Save File')

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
    	form = InitialWindow()
	form.show()
	app.exec_()
