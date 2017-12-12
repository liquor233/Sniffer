# this is for capture all the data
from socket import *
from struct import *
import sys,binascii

from mainwindow1 import *

packet_store=[]
class capture:
	def __init__(self):
		self.type =0
		self.src_ip=0
		self.dst_ip=0
		self.index=0
		self.sniffer=socket(AF_PACKET,SOCK_RAW,htons(ETH_P_ALL))
		self.capture_packet()
	
	def capture_packet(self):
		while(True):
			self.type=0
			self.src_ip=0
			self.dst_ip=0
			packet,_ = sniffer.recvfrom(MTU)
			self.parse_eth(packet)
			if self.type and self.src_ip and self.dst_ip :
				form.Display.setRowCount(self.index+1)
				packet_store.append(packet)
				form.DisplayTable.setItem(index,0,QTableWidgetItem(str(self.type)))
				form.DisplayTable.setItem(index,i,QTableWidgetItem(str(self.src_ip)))
				form.DisplayTable.setItem(index,0,QTableWidgetItem(str(self.src_ip)))
				index+=1
			if(index==100):break

	def parse_eth(packet)
		eth_header=self.packet[:14]
                frame = packet[14:]
                eth = unpack("!6s6s2s",eth_header)
                #dst_mac = eth[0].encode('hex')
                #src_mac = eth[1].encode('hex')
                eth_type = binascii.hexlify(eth[2])
                if(eth_type=='0800'):
                        self.ip_parse(frame)
                #elif (eth_type=='0806'):
                #        self.arp_parse(frame)
                #else: error('unknown eth type')
	
	def parse_ip(packet)
		version = ord(ipframe[0]) >> 4
                if (version==4):
                        self.ip4_parse(ipframe)
                #elif (version==6):
                #        self.ip6_parse(ipframe)

	def ip4_parse(self,ipframe):
                iph_main = unpack("!BBHHHBBH4s4s",ipframe[0:20])
                protocol = iph_main[6]
                self.src_ip = inet_ntoa(iph_main[8])
                self.dst_ip = inet_ntoa(iph_main[9])
                if(protocol==1):
                        self.type = 'icmp'
                elif(protocol==2):
                        self.type = 'igmp'
                elif(protocol==6):
                        self.type = 'tcp'
                elif(protocol==17):
                        self.type = 'udp'
                else:
                        self.type = 'unknown'

	def clear_packet(self):
		packet[]=[]
		form.DisplayTable.clearContents()
		self.index=0
