from socket import *
from struct import *
import sys,binascii

class Parser:
	# this is a Parse class to parse IP packet,including TCP and UDP
	def __init__(self,packet):
		
		self.packet=packet

	def StartParser(self):
		eth_length = 14
		self.eth_parse(eth_length)

	def eth_parse(self,hlength):
		eth_header=self.packet[:hlength]
		frame = packet[hlength:]
		eth = unpack("!6s6s2s",eth_header)
		dst_mac = eth[0].encode('hex')
		src_mac = eth[1].encode('hex')
		eth_type = binascii.hexlify(eth[2])
		print '------------------------new line----------------------------------'
		print "Destination MAC:"+self.mac_parse(dst_mac)+"\tSource MAC:"+self.mac_parse(src_mac)+"\tprotocal type:"+eth_type
		if(eth_type=='0800'):
			self.ip_parse(frame)
		elif (eth_type=='0806'):
			self.arp_parse(frame)
		else: print 'you son of bitch'
	
	def mac_parse(self,mac):
		out = ':'.join([mac[i : i + 2] for i in range(0, len(mac), 2)]) 
		return out

	def ip_parse(self,ipframe):
		version = ord(ipframe[0]) >> 4
		if (version==4):
			self.ip4_parse(ipframe)
		elif (version==6):
			self.ip6_parse(ipframe)

	def tcp_parse(self,packet):
            	tcph_main = packet[0:20]
		tcph = unpack('!HHLLBBHHH' , tcph_main)

            	src_port = tcph[0]
            	dst_port = tcph[1]
            	sequence = tcph[2]
            	acknowledgement = tcph[3]
            	doff_reserved = tcph[4]
            	tcph_length = (doff_reserved >> 4)*4
		print 'Source Port : ' + str(src_port) + ' Dest Port : ' + str(dst_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
		data = packet[tcph_length:]
		print 'data:'+data

	def udp_parse(self,packet):
            	udp_header = packet[0:8]
		udp_length = 8
            	udph = unpack('!HHHH' , udp_header)

            	src_port = udph[0]
            	dst_port = udph[1]
            	length = udph[2]
            	checksum = udph[3]
		print 'Source Port : ' + str(src_port) + ' Dest Port : ' + str(dst_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)
		data = packet[udp_length:]
		print 'data:'+data


	def ip4_parse(self,ipframe):
		iph_main = unpack("!BBHHHBBH4s4s",ipframe[0:20])
		version_ihl = iph_main[0]
		version = version_ihl >> 4
		ihl = (version_ihl & 0xF)*4
		ifl = iph_main[2]*4
		ttl = iph_main[5]
		protocol = iph_main[6]
		iph_option = ipframe[20:ihl]
		s_addr=inet_ntoa(iph_main[8])
		d_addr = inet_ntoa(iph_main[9])
		
		print '\tsource address is:'+str(s_addr)+'\tdestination address is:'+str(d_addr)+"\tprotocol is:"+str(protocol)
		
		frame = ipframe[ihl:]
		if(protocol==1):
			self.icmp_parse(frame)
		elif(protocol==2):
			self.igmp_parse(frame)
		elif(protocol==6):
			self.tcp_parse(frame)
		elif(protocol==17):
			self.udp_parse(frame)
		else: 
			print 'not support protocol'
			print 'the payload is ' + frame

	def ip6_parse(self,ipframe):
		print 'you son of bitch'

	def arp_parse(self,ipframe):
		print 'you son of bitch'

	
	def icmp_parse(self,packet):
            	icmph_length = 4
            	icmp_header = packet[0:4]
            	icmph = unpack('!BBH' , icmp_header)
            	icmp_type = icmph[0]
            	code = icmph[1]
            	checksum = icmph[2]

            	print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)
		data = packet[4:]
		print 'data:'+data


	def igmp_parse(self,frame):
		print 'you son of bitch'
		 
		
# some parameter defination
device = 'ens33'
MTU = 65565
ETH_P_ALL = 0X0003

# finally i choose AF_PACKET as the socket domain to capture the ICMP and IGMP
sniffer=socket(AF_PACKET,SOCK_RAW,htons(ETH_P_ALL))
# sniffer.setsockopt(SOL_SOCKET,SO_BINDTODEVICE,device)
while True:
	packet,_ = sniffer.recvfrom(MTU)# tuple unpack use _ 
	c = Parser(packet)
	c.StartParser()
	#break # for debug
