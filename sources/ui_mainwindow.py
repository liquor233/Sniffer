# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
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

class Ui_Capture(object):
    def setupUi(self, Capture):
        Capture.setObjectName(_fromUtf8("Capture"))
        Capture.resize(1242, 770)
        Capture.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(Capture)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.NIChooser = QtGui.QComboBox(self.centralwidget)
        self.NIChooser.setAutoFillBackground(True)
        self.NIChooser.setEditable(False)
        self.NIChooser.setObjectName(_fromUtf8("NIChooser"))
        self.horizontalLayout_3.addWidget(self.NIChooser)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Ctime = QtGui.QLabel(self.centralwidget)
        self.Ctime.setObjectName(_fromUtf8("Ctime"))
        self.horizontalLayout_3.addWidget(self.Ctime)
        spacerItem1 = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_3.addWidget(self.saveButton)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.CaptureButton = QtGui.QPushButton(self.centralwidget)
        self.CaptureButton.setCheckable(True)
        self.CaptureButton.setChecked(False)
        self.CaptureButton.setObjectName(_fromUtf8("CaptureButton"))
        self.horizontalLayout_2.addWidget(self.CaptureButton)
        self.DetailButton = QtGui.QPushButton(self.centralwidget)
        self.DetailButton.setObjectName(_fromUtf8("DetailButton"))
        self.horizontalLayout_2.addWidget(self.DetailButton)
        spacerItem2 = QtGui.QSpacerItem(280, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.SearchButton = QtGui.QPushButton(self.centralwidget)
        self.SearchButton.setObjectName(_fromUtf8("SearchButton"))
        self.horizontalLayout_2.addWidget(self.SearchButton)
        self.RepacketButton = QtGui.QPushButton(self.centralwidget)
        self.RepacketButton.setObjectName(_fromUtf8("RepacketButton"))
        self.horizontalLayout_2.addWidget(self.RepacketButton)
        self.FilterButton = QtGui.QPushButton(self.centralwidget)
        self.FilterButton.setEnabled(True)
        self.FilterButton.setObjectName(_fromUtf8("FilterButton"))
        self.horizontalLayout_2.addWidget(self.FilterButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.MainTable = QtGui.QTableWidget(self.centralwidget)
        self.MainTable.setAccessibleName(_fromUtf8(""))
        self.MainTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.MainTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.MainTable.setAlternatingRowColors(False)
        self.MainTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.MainTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.MainTable.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.MainTable.setColumnCount(2)
        self.MainTable.setObjectName(_fromUtf8("MainTable"))
        self.MainTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 0, 0))
        self.MainTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, item)
        self.MainTable.horizontalHeader().setDefaultSectionSize(80)
        self.MainTable.horizontalHeader().setSortIndicatorShown(True)
        self.MainTable.horizontalHeader().setStretchLastSection(True)
        self.MainTable.verticalHeader().setVisible(False)
        self.MainTable.verticalHeader().setHighlightSections(True)
        self.horizontalLayout.addWidget(self.MainTable)
        self.DetailViewer = QtGui.QTextBrowser(self.centralwidget)
        self.DetailViewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DetailViewer.setObjectName(_fromUtf8("DetailViewer"))
        self.horizontalLayout.addWidget(self.DetailViewer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Capture.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Capture)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Capture.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Capture)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Capture.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Capture)
        self.toolBar.setStyleSheet(_fromUtf8("Capture{background-color:rgb(0, 170, 0);}"))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Capture.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.label_2.setBuddy(self.NIChooser)

        self.retranslateUi(Capture)
        QtCore.QObject.connect(self.CaptureButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.NIChooser.setDisabled)
        QtCore.QObject.connect(self.CaptureButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.FilterButton.setDisabled)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Capture.close)
        QtCore.QObject.connect(self.CaptureButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.SearchButton.setDisabled)
        QtCore.QObject.connect(self.CaptureButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.RepacketButton.setDisabled)
        QtCore.QObject.connect(self.CaptureButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.saveButton.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Capture)
        Capture.setTabOrder(self.FilterButton, self.exitButton)
        Capture.setTabOrder(self.exitButton, self.NIChooser)
        Capture.setTabOrder(self.NIChooser, self.CaptureButton)
        Capture.setTabOrder(self.CaptureButton, self.RepacketButton)
        Capture.setTabOrder(self.RepacketButton, self.saveButton)
        Capture.setTabOrder(self.saveButton, self.MainTable)
        Capture.setTabOrder(self.MainTable, self.DetailViewer)
        Capture.setTabOrder(self.DetailViewer, self.SearchButton)

    def retranslateUi(self, Capture):
        Capture.setWindowTitle(_translate("Capture", "MainWindow", None))
        self.label_2.setText(_translate("Capture", "choose NIC", None))
        self.Ctime.setText(_translate("Capture", "TextLabel", None))
        self.saveButton.setText(_translate("Capture", "&save", None))
        self.exitButton.setText(_translate("Capture", "&exit", None))
        self.CaptureButton.setText(_translate("Capture", "begin", None))
        self.DetailButton.setText(_translate("Capture", "show &detail", None))
        self.label_3.setText(_translate("Capture", "Copyright@ 简夏 & 杰宝", None))
        self.SearchButton.setText(_translate("Capture", "search", None))
        self.RepacketButton.setText(_translate("Capture", "&IpRecombine", None))
        self.FilterButton.setText(_translate("Capture", "&Filter", None))
        self.MainTable.setSortingEnabled(True)
        item = self.MainTable.horizontalHeaderItem(0)
        item.setText(_translate("Capture", "no", None))
        item = self.MainTable.horizontalHeaderItem(1)
        item.setText(_translate("Capture", "Packet Captured", None))
        self.DetailViewer.setHtml(_translate("Capture", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.toolBar.setWindowTitle(_translate("Capture", "toolBar", None))

