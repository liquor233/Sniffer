# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SDialog.ui'
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

class Ui_SDialog(object):
    def setupUi(self, SDialog):
        SDialog.setObjectName(_fromUtf8("SDialog"))
        SDialog.resize(400, 246)
        self.buttonBox = QtGui.QDialogButtonBox(SDialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 160, 176, 33))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(SDialog)
        self.widget.setGeometry(QtCore.QRect(80, 70, 221, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(SDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SDialog)

    def retranslateUi(self, SDialog):
        SDialog.setWindowTitle(_translate("SDialog", "SearchDialog", None))
        self.label.setWhatsThis(_translate("SDialog", "<html><head/><body><p>输入查询字符串</p></body></html>", None))
        self.label.setText(_translate("SDialog", "search:", None))

