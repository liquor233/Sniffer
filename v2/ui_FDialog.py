# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FDialog.ui'
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

class Ui_FDialog(object):
    def setupUi(self, FDialog):
        FDialog.setObjectName(_fromUtf8("FDialog"))
        FDialog.resize(400, 272)
        self.verticalLayout = QtGui.QVBoxLayout(FDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(FDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.TypeChooser = QtGui.QComboBox(FDialog)
        self.TypeChooser.setObjectName(_fromUtf8("TypeChooser"))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.setItemText(0, _fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.TypeChooser.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.TypeChooser)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(FDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Sourceip = QtGui.QLineEdit(FDialog)
        self.Sourceip.setObjectName(_fromUtf8("Sourceip"))
        self.horizontalLayout_2.addWidget(self.Sourceip)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(FDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.Destinationip = QtGui.QLineEdit(FDialog)
        self.Destinationip.setObjectName(_fromUtf8("Destinationip"))
        self.horizontalLayout_3.addWidget(self.Destinationip)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(FDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.Destinationport = QtGui.QLineEdit(FDialog)
        self.Destinationport.setObjectName(_fromUtf8("Destinationport"))
        self.horizontalLayout.addWidget(self.Destinationport)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(FDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.TypeChooser)
        self.label_2.setBuddy(self.Sourceip)
        self.label_3.setBuddy(self.Destinationip)
        self.label_4.setBuddy(self.Destinationport)

        self.retranslateUi(FDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FDialog)

    def retranslateUi(self, FDialog):
        FDialog.setWindowTitle(_translate("FDialog", "FilterDialog", None))
        self.label.setText(_translate("FDialog", "ProtolType", None))
        self.TypeChooser.setItemText(1, _translate("FDialog", "ip6", None))
        self.TypeChooser.setItemText(2, _translate("FDialog", "ip4", None))
        self.TypeChooser.setItemText(3, _translate("FDialog", "arp", None))
        self.TypeChooser.setItemText(4, _translate("FDialog", "icmp6", None))
        self.TypeChooser.setItemText(5, _translate("FDialog", "icmp4", None))
        self.TypeChooser.setItemText(6, _translate("FDialog", "tcp", None))
        self.TypeChooser.setItemText(7, _translate("FDialog", "udp", None))
        self.TypeChooser.setItemText(8, _translate("FDialog", "DNS", None))
        self.TypeChooser.setItemText(9, _translate("FDialog", "HTTP", None))
        self.TypeChooser.setItemText(10, _translate("FDialog", "FTP", None))
        self.TypeChooser.setItemText(11, _translate("FDialog", "POP3", None))
        self.TypeChooser.setItemText(12, _translate("FDialog", "SSH", None))
        self.TypeChooser.setItemText(13, _translate("FDialog", "TELNET", None))
        self.TypeChooser.setItemText(14, _translate("FDialog", "HTTPS", None))
        self.TypeChooser.setItemText(15, _translate("FDialog", "SMTP", None))
        self.label_2.setText(_translate("FDialog", "Source Ip:", None))
        self.label_3.setText(_translate("FDialog", "Destination Ip", None))
        self.label_4.setText(_translate("FDialog", "Source tcp/udp Port", None))

