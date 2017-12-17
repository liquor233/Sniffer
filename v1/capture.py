# this is for capture all the data
from socket import *
from struct import *
import sys,binascii
import thread

from mainwindow1 import *

#define ETH_P_ALL 0X0003

class Capture:
	def __init__(self):
		self.type =0
		self.src_ip=0
		self.dst_ip=0
	
	def capture_packet(self):
		if(self._running):
			self.type=0
			self.src_ip=0
			self.dst_ip=0
			packet,_ = self.sniffer.recvfrom(65565)
			self.parse_eth(packet)
			if self.type or self.src_ip or self.dst_ip :
				self.packet_store.append(packet)
				self.index+=1
				return ((self.index,self.type,self.src_ip,self.dst_ip),1)
			if(self.index==100):
				self.stop_capture()
			return ((0,0,0,0),0)
		else: 
			return ((0,0,0,0),0)

	def parse_eth(self,packet):
		eth_header=packet[:14]
                frame = packet[14:]
                eth = unpack("!6s6s2s",eth_header)
                #dst_mac = eth[0].encode('hex')
                #src_mac = eth[1].encode('hex')
                eth_type = binascii.hexlify(eth[2])
                if(eth_type=='0800'):
                        self.parse_ip(frame)
                #elif (eth_type=='0806'):
                #        self.arp_parse(frame)
                #else: error('unknown eth type')
	
	def parse_ip(self,packet):
		version = ord(packet[0]) >> 4
                if (version==4):
                        self.ip4_parse(packet)
                #elif (version==6):
                #        self.ip6_parse(packet)

	def ip4_parse(self,packet):
                iph_main = unpack("!BBHHHBBH4s4s",packet[0:20])
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

	
	def stop_capture(self):
		self._running = False
		self.sniffer.close()

	def begin_capture(self,nic):
		self.sniffer=socket(AF_PACKET,SOCK_RAW,htons(0x0003))
		self.sniffer.bind((nic,0))

		self.index=0
		self.packet_store=[]
		self._running = True
