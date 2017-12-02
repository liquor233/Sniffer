# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/firsttry.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../learn/PyQt/icon/mask.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.NIChooser = QtGui.QComboBox(self.centralwidget)
        self.NIChooser.setObjectName(_fromUtf8("NIChooser"))
        self.NIChooser.addItem(_fromUtf8(""))
        self.NIChooser.addItem(_fromUtf8(""))
        self.NIChooser.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.NIChooser)
        self.ShowCapture = QtGui.QTextBrowser(self.centralwidget)
        self.ShowCapture.setAutoFillBackground(True)
        self.ShowCapture.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ShowCapture.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ShowCapture.setObjectName(_fromUtf8("ShowCapture"))
        self.horizontalLayout.addWidget(self.ShowCapture)
        self.SScapture = QtGui.QPushButton(self.centralwidget)
        self.SScapture.setObjectName(_fromUtf8("SScapture"))
        self.horizontalLayout.addWidget(self.SScapture)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        MainWindow.setAccessibleName(_translate("MainWindow", "Main_Window", None))
        self.NIChooser.setItemText(0, _translate("MainWindow", "ens33", None))
        self.NIChooser.setItemText(1, _translate("MainWindow", "ens38", None))
        self.NIChooser.setItemText(2, _translate("MainWindow", "lo", None))
        self.SScapture.setText(_translate("MainWindow", "START", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
