# Sniffer
**now is the vision 2, so please go into the folder v2 to check all the source code**
This is the curriculum design of computer network——a sniffer with complete GUI in python for Linux

##requirements.txt
**this is about the required python module**
python == 2.7.12
pyqt==4.12.1
Qt==4.8.7
sip==4.19.6
prettytable==0.7.2
##the structure of version 2
sniffer_sqlite: to store and filter database
mainwindow.py:the main window
ui_mainwindow.py:the main window designed by qt designer
parser.py:to show the detailed message of a packet
mthread.py:to capture and parse basical information of a packet to store in the database
interfaces:to get the list of reacheable network interfaces
##headerimg
headerimg folder is the protocol header's graphical explanation
