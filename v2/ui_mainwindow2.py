# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
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

class Ui_Capture2(object):
    def setupUi(self, Capture2):
        Capture2.setObjectName(_fromUtf8("Capture2"))
        Capture2.resize(1061, 770)
        Capture2.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(Capture2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.openFButton = QtGui.QPushButton(self.centralwidget)
        self.openFButton.setObjectName(_fromUtf8("openFButton"))
        self.horizontalLayout_3.addWidget(self.openFButton)
        self.saveFButton = QtGui.QPushButton(self.centralwidget)
        self.saveFButton.setObjectName(_fromUtf8("saveFButton"))
        self.horizontalLayout_3.addWidget(self.saveFButton)
        self.TimeL = QtGui.QLabel(self.centralwidget)
        self.TimeL.setObjectName(_fromUtf8("TimeL"))
        self.horizontalLayout_3.addWidget(self.TimeL)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.NIChooser = QtGui.QComboBox(self.centralwidget)
        self.NIChooser.setEditable(False)
        self.NIChooser.setObjectName(_fromUtf8("NIChooser"))
        self.horizontalLayout_2.addWidget(self.NIChooser)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.CaptureButton = QtGui.QPushButton(self.centralwidget)
        self.CaptureButton.setCheckable(True)
        self.CaptureButton.setChecked(False)
        self.CaptureButton.setObjectName(_fromUtf8("CaptureButton"))
        self.horizontalLayout_2.addWidget(self.CaptureButton)
        self.DetailButton = QtGui.QPushButton(self.centralwidget)
        self.DetailButton.setObjectName(_fromUtf8("DetailButton"))
        self.horizontalLayout_2.addWidget(self.DetailButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.FilterButton = QtGui.QPushButton(self.centralwidget)
        self.FilterButton.setEnabled(True)
        self.FilterButton.setObjectName(_fromUtf8("FilterButton"))
        self.horizontalLayout_2.addWidget(self.FilterButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.MainTable = QtGui.QTableWidget(self.centralwidget)
        self.MainTable.setAccessibleName(_fromUtf8(""))
        self.MainTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.MainTable.setObjectName(_fromUtf8("MainTable"))
        self.MainTable.setColumnCount(0)
        self.MainTable.setRowCount(0)
        self.MainTable.horizontalHeader().setDefaultSectionSize(230)
        self.MainTable.horizontalHeader().setSortIndicatorShown(True)
        self.MainTable.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.MainTable)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        Capture2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Capture2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Capture2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Capture2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Capture2.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Capture2)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Capture2.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.label_2.setBuddy(self.NIChooser)

        self.retranslateUi(Capture2)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.menubar.close)
        QtCore.QObject.connect(self.CaptureButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.NIChooser.setDisabled)
        QtCore.QObject.connect(self.CaptureButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.FilterButton.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Capture2)

    def retranslateUi(self, Capture2):
        Capture2.setWindowTitle(_translate("Capture2", "MainWindow", None))
        self.openFButton.setText(_translate("Capture2", "&open", None))
        self.saveFButton.setText(_translate("Capture2", "&save", None))
        self.TimeL.setText(_translate("Capture2", "TextLabel", None))
        self.exitButton.setText(_translate("Capture2", "&exit", None))
        self.label_2.setText(_translate("Capture2", "choose NIC", None))
        self.CaptureButton.setText(_translate("Capture2", "begin", None))
        self.DetailButton.setText(_translate("Capture2", "show &detail", None))
        self.FilterButton.setText(_translate("Capture2", "&Filter", None))
        self.MainTable.setSortingEnabled(True)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Capture2", "hu", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolBar.setWindowTitle(_translate("Capture2", "toolBar", None))

