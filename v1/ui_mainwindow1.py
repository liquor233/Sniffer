# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/mainwindow1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Capture1(object):
    def setupUi(self, Capture1):
        Capture1.setObjectName(_fromUtf8("Capture1"))
        Capture1.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Capture1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.NIChooser = QtGui.QComboBox(self.centralwidget)
        self.NIChooser.setObjectName(_fromUtf8("NIChooser"))
        self.verticalLayout.addWidget(self.NIChooser)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.CaptureButton = QtGui.QPushButton(self.centralwidget)
        self.CaptureButton.setCheckable(True)
        self.CaptureButton.setChecked(False)
        self.CaptureButton.setObjectName(_fromUtf8("CaptureButton"))
        self.verticalLayout.addWidget(self.CaptureButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.DetailButton = QtGui.QPushButton(self.centralwidget)
        self.DetailButton.setObjectName(_fromUtf8("DetailButton"))
        self.verticalLayout.addWidget(self.DetailButton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.DisplayTable = QtGui.QTableWidget(self.centralwidget)
        self.DisplayTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.DisplayTable.setObjectName(_fromUtf8("DisplayTable"))
        self.DisplayTable.setColumnCount(3)
        self.DisplayTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.DisplayTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.DisplayTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.DisplayTable.setHorizontalHeaderItem(2, item)
        self.DisplayTable.horizontalHeader().setDefaultSectionSize(230)
        self.DisplayTable.horizontalHeader().setSortIndicatorShown(True)
        self.DisplayTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.DisplayTable)
        Capture1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Capture1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Capture1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Capture1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Capture1.setStatusBar(self.statusbar)

        self.retranslateUi(Capture1)
        QtCore.QMetaObject.connectSlotsByName(Capture1)

    def retranslateUi(self, Capture1):
        Capture1.setWindowTitle(_translate("Capture1", "MainWindow", None))
        self.CaptureButton.setText(_translate("Capture1", "begin", None))
        self.DetailButton.setText(_translate("Capture1", "detail", None))
        self.DisplayTable.setSortingEnabled(True)
        item = self.DisplayTable.horizontalHeaderItem(0)
        item.setText(_translate("Capture1", "type", None))
        item = self.DisplayTable.horizontalHeaderItem(1)
        item.setText(_translate("Capture1", "src ip", None))
        item = self.DisplayTable.horizontalHeaderItem(2)
        item.setText(_translate("Capture1", "dst ip", None))

