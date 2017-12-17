from socket import *
sniffer=socket(AF_PACKET,SOCK_RAW,htons(0x0003))
while True:
	packet,_=sniffer.recvfrom(65565)
	print packet
