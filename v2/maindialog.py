from ui_SDialog import Ui_SDialog
from ui_FDialog import Ui_FDialog
from PyQt4.QtGui import *
import re
class SDialog(QDialog,Ui_SDialog):
	def __init__(self,parent=None):
               	super(SDialog, self).__init__(parent)
               	self.setupUi(self)
	def searchtext(self):
		return str(self.lineEdit.text())
class FDialog(QDialog,Ui_FDialog):
        def __init__(self,parent=None):
                super(FDialog, self).__init__(parent)
                self.setupUi(self)
	def GetCondition(self):
		sip,dip,sport,ptype=('-1','-1','-1','-1')
		if self.Sourceip.text()!='' : 
			sip = str(self.Sourceip.text())
			sip = self.ipaddress(sip)
		if self.Destinationip.text()!='' :
			dip = str(self.Destinationip.text())
			dip = self.ipaddress(dip)
		if self.Destinationport.text()!='':
			try:
				sport = int(self.Destinationport.text())
			except ValueError:
				sport = '0'
		if self.TypeChooser.currentText()!='':ptype = str(self.TypeChooser.currentText())
		return sip,dip,sport,ptype
	def ipaddress(self,message):
		re_ip4 = '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'
		re_ip6 = '''^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$'''
                try:
			if re.match(re_ip4,message):
                		loc = re.match(re_ip4,message).span()
                       	 	return message[loc[0]:loc[1]]
                	elif re.match(re_ip6,message):
                        	loc = re.match(re_ip6,message).span()
                        	return message[loc[0]:loc[1]]
			else: return '0'
		except AttributeError:
			return '0'

if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        form = FDialog()
        form.show()
	if form.exec_():
		print form.GetCondition()
        app.exec_()
