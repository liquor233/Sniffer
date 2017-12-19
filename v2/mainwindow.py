#!/usr/bin/python
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import (QDate,QTime,Qt,QStringList, QString,QTimer)
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtCore import pyqtSlot as Slot
from PyQt4.QtGui import *

from threading import Thread
from Queue import Queue
import os
import time

from mthread import *
from parser import GetDetail
from sniffer_sqlite import *
from ui_mainwindow import Ui_Capture
from interfaces import get_nic_list

class InitialWindow(QMainWindow,Ui_Capture):
	def __init__(self,parent=None):
       		super(InitialWindow, self).__init__(parent)
      	 	self.setupUi(self)
        	
		self.CaptureButton.setFocusPolicy(Qt.NoFocus)
        	self.DetailButton.setFocusPolicy(Qt.NoFocus)
        	self.NIChooser.setFocusPolicy(Qt.NoFocus)
        	self.MainTable.setFocusPolicy(Qt.NoFocus)
		self.setWindowIcon(QIcon('../icon/mask.ico'))
		self.MainTable.setEditTriggers(QAbstractItemView.NoEditTriggers)	
		self.NIChooser.addItems(QStringList(get_nic_list()))
	
		self.capture=CountdownTask()
		#to show the current time dynamically
		self.show_time()
		self.Ctime.setAlignment(Qt.AlignCenter)
		self.Ctime.setStyleSheet("color:red")
		tim=QTimer(self)
        	tim.timeout.connect(self.show_time)
                #signal-slot
                self.DetailButton.clicked.connect(self.show_detail);
                self.MainTable.cellDoubleClicked.connect(self.show_detail);
		self.saveButton.clicked.connect(self.save_file)
		

	@Slot(bool)
	def on_CaptureButton_clicked(self,checked):
		if checked==1:
			#delete the database file
			if os.path.isfile('main.db') : os.remove('main.db')	
		
			self.CaptureButton.setText(QString("stop"))
			self.MainTable.clearContents()
			self.MainTable.setRowCount(0)

			#t_running to stop the Tstore function
			self.t_running=True
			nic = str(self.NIChooser.currentText())
			#q is the Queue for get and put packet
			q = Queue()
			w = Thread(target=self.capture.run,args=(nic,q,))
 			w.start()
			c = Thread(target=self.Tstore,args=(q,))
			c.start()


		else:	
			#in here we try to kill both thread	
			self.CaptureButton.setText(QString("begin"))
			#to stop Tstore function
			self.t_running=False
			#to stop capture function
			self.capture.terminate()
		        	
	#to store packet into database,which is executed in a thread
	def Tstore(self,pr):
		no=0
                sqlite_start()
                while(self.t_running):
                	packet = pr.get(True)
                        no=no+1
                        stack,ptype,sport,dport = GetProtoType(packet)
                        srcip,dstip=GetIp(packet,stack)
                        message=ptype
                        if srcip!='-1':
                        	message+='\tFrom '+srcip
                        if sport !='-1':
                        	message+=':'+str(sport)
                       	if dstip != '-1':
                        	message+=' To: '+dstip
                        if dport!='-1':
                                message+=': '+str(dport)
                       	self.MainTable.setRowCount(no)
                        self.MainTable.setItem(no-1,0,QTableWidgetItem(QString(message)))
		        insert_db(no,packet,srcip,dstip,sport,dport,ptype,stack)

	# this is the function to show the detail of packet message
	def show_detail(self):
                self.DetailViewer.clear()
                
		no = self.MainTable.currentRow()
                if no==-1:message='error!you must choose one row then click showdetail button'
                else:
			packet=detail_packet(no+1)[0]
			message=GetDetail(packet)
                self.DetailViewer.append(QString(message))

        def save_file(self):
		name = QFileDialog.getSaveFileName(self, 'Save File')
		save_txt(name)

	def show_time(self):
		a=QTime.currentTime()
        	a1=QDate.currentDate()
        	a2=a1.toString('yyyy-MM-dd')+' '+a.toString('hh:mm:ss')
		self.Ctime.setText(QString(a2))


if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
    	form = InitialWindow()
	form.show()
	app.exec_()
