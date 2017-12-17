import socket
import os
import struct
import binascii 

def etherHeader(packet):
  IpHeader = struct.unpack("!6s6sH",packet[0:14]) #ipv4==0x0800
  dstMac = binascii.hexlify(IpHeader[0]) #source MAC address. converts binary data into ascii dt looks like hex. MAC address is always in hex format.
  srcMac = binascii.hexlify(IpHeader[1]) #Destination MAC address
  protoType = IpHeader[2] #next protocol (ip/ipv4,arp,icmp,ipv6)
  nextProto = hex(protoType) #hex() returns a string. it a built in finction

  print "*******************ETHER HEADER***********************"
  print "\tDestination MAC: "+dstMac[0:2]+":"+dstMac[0:2]+":"+dstMac[2:4]+":"+dstMac[4:6]+":"+dstMac[6:8]+":"+dstMac[8:10]+":"+dstMac[10:]
  print "\tsource MAC: "+srcMac[0:2]+":"+srcMac[0:2]+":"+srcMac[2:4]+":"+srcMac[4:6]+":"+srcMac[6:8]+":"+srcMac[8:10]+":"+srcMac[10:]

  print "\tNext Protocol: "+nextProto

  if (nextProto == '0x800'): 
     proto = 'IPV4'
  elif (nextProto == '0x806'): 
     proto = 'ARP'
  elif (nextProto == '0x86dd'): 
     proto = 'IPV6'
  else: proto='unsupported ethernet header'

  packet = packet[14:]
  return packet,proto

def ipv4Header(data):
   packet = struct.unpack("!6H4s4s",data[0:20]) #6Unsigned shrt,4bytsOfStirng,4bytsOfString. 2*6byts+4byts+4byts==20byts
   version = packet[0] >> 12 #shift dis byte to d right by 12 bits so that only version field remains and all bits to its left is zero. 
   headerLenght = (packet[0] >> 8) & 0x000F #Removes typ of srvc via logic shift to the right and removes version field via '&'.
   typeOfService = packet[0] & 0x00FF #Removes vrs n headrlen via '&'
   totalLenght = packet[1]
   identification = packet[2]
   flags = (packet[3] >> 13)
   fragOffSet = packet[3] & 0x1FFF
   ttl = packet[4] >> 8
   protocol = packet[4] & 0x00FF
   hdrChkSum = packet[5]
   srcAddress = socket.inet_ntoa(packet[6]) #_ntoa==netwotk to ascii.
   dstAddress = socket.inet_ntoa(packet[7]) #_ntoa==netwotk to ascii.

   print "*******************IPV4 HEADER***********************"
   print "\tVersion: "+str(version)
   print "\tHeader Lenght: "+str(headerLenght)
   print "\tType Of Service: "+str(typeOfService)
   print "\tTotal Lenght: "+str(totalLenght) 
   print "\tIdentification: "+str(identification) 
   print"\tFlags: "+str(flags) 
   print "\tFragment Offset: "+str(fragOffSet) 
   print "\tTll: "+str(ttl)
   print "\tNext Protocol: "+str(protocol) 
   print "\tHeader checksum: "+str(hdrChkSum) 
   print "\tSource Address: "+srcAddress 
   print "\tDestination Address: "+dstAddress 

   if (protocol == 6): #check protocol number documentation
     nextProto = 'TCP'
   elif (protocol == 17):
     nextProto = 'UDP'
   elif (protocol == 1):
     nextProto = 'ICMP'
   elif (protocol == 4):
     nextProto == 'IPV4'
   elif (protocol == 41):
     nextProto = 'IPV6'
   elif (protocol == 2):
     nextProto = 'IGMP'
   elif (protocol ==0):
     nextProto = 'NONE'
   else: nextProto = "unsupported IP protocol type,for type number is: "+str(protocol)

   data = data[headerLenght*4:]
   return data, nextProto
   
def icmp4Header(newPacket):
  packet = struct.unpack("!BBH",newPacket[:4])
  typedict = {'0':'EchoReply','3':'unreachable','5':'redirection','8':'Echo'}
  Type=packet[0]
  if Type in [0,3,5,8]:Type=typedict[str(Type)]
  print "*******************ICMP4 HEADER***********************"
  print "\tType: " + str(Type)
  print "\tCode: " + str(packet[1])
  print "\tchecksum: "+str(packet[2])
  #print "\tidentifier: "+str(packet[3]) 						#because it is optional , so we don't show it	
  #print "\tsequence: "+str(packet[4])
  print "\tdata(if have): "+str(newPacket[4:])

def ipv6(addr):										#because socket does not support ipv6 address parse
    addr = socket.inet_ntop(socket.AF_INET6, addr)
    return addr

def ipv6Header(newPacket):
  packet = struct.unpack("!IHBB16s16s",newPacket[:40])
  protodict = {'0':'HopByHop','60':'DestinationOptional','43':'Routing','44':'Fragment','51':'AH','50':'ESP',
	       '6':'TCP','17':'UDP','58':'ICMP','4':'IPV4','2':'IGMP','41':'IPV6','59':'NoMoreHeader'}
  version = packet[0]>>28
  TC = (packet[0]>>20)&0xFFF
  FlowLabel = packet[0]&0xFFFFF
  payloadLength = packet[1]
  protocol = packet[2]
  ttl = packet[3]
  srcAddress = ipv6(packet[4])
  dstAddress = ipv6(packet[5])
  print "*******************IPV6 HEADER***********************"
  print "\tVersion: "+str(version)
  print "\tTraffic Class: "+str(TC)
  print "\tFlow Label: "+str(FlowLabel)
  print "\tpayloadlength Lenght: "+str(payloadLength)
  print "\tNext Protocol: "+str(protocol)
  print "\tHopLimited: "+str(ttl)
  print "\tSource Address: "+srcAddress
  print "\tDestination Address: "+dstAddress
  if protocol in [0,58,59,2,4,6,17,41,44,43,50,51,60]:nextProto=protodict[str(protocol)]
  else : nextProto='no supported IPV6 protocol type'
  data = newPacket[40:]
  return data, nextProto

def icmp6Header(newPacket):
  packet = struct.unpack("!BBH",newPacket[:4])
  typedict = {'129':'EchoReply','1':'unreachable','2':'oversize packet','3':'timeout','4':'paramerror','128':'Echo'}
  Type=packet[0]
  if Type in [1,2,3,4,128,129]:Type=typedict[str(Type)]
  print "*******************ICMP6 HEADER***********************"
  print "\tType: " + str(Type)
  print "\tCode: " + str(packet[1])
  print "\tchecksum: "+str(packet[2])
  data = newPacket[4:]
  printdata(data)

def igmpHeader(newPacket):
  packet = struct.unpack("!BBH4s",newPacket[8:])
  print "*******************IGMP HEADER***********************"
  print "\tType: " + hex(packet[0])
  print "\tMaxRespTime: " + str(packet[1])
  print "\tchecksum: " + str(packet[2])
  print "\tgroupID: " + socket.inet_ntoa(packet[3])					#group ID is an IP

def tcpHeader(newPacket):
   packet = struct.unpack("!2H2I4H",newPacket[0:20]) 
   srcPort = packet[0]
   dstPort = packet[1]
   sqncNum = packet[2]
   acknNum = packet[3]
   dataOffset = packet[4] >> 12
   reserved = (packet[4] >> 6) & 0x003F 
   tcpFlags = packet[4] & 0x003F 
   urgFlag = tcpFlags & 0x0020  
   ackFlag = tcpFlags & 0x0010  
   pushFlag = tcpFlags & 0x0008 
   resetFlag = tcpFlags & 0x0004 
   synFlag = tcpFlags & 0x0002  
   finFlag = tcpFlags & 0x0001  
   window = packet[5]
   checkSum = packet[6]
   urgPntr = packet[7]
   

   print "*******************TCP HEADER***********************"
   print "\tSource Port: "+str(srcPort)
   print "\tDestination Port: "+str(dstPort)
   print "\tSequence Number: "+str(sqncNum)
   print "\tAck. Number: "+str(acknNum)
   print "\tData Offset: "+str(dataOffset)
   print "\tReserved: "+str(reserved)
   print "\tTCP Flags: "+str(tcpFlags)

   if(urgFlag == 32):
     print "\tUrgent Flag: Set"
   if(ackFlag == 16):
     print "\tAck Flag: Set"
   if(pushFlag == 8):
     print "\tPush Flag: Set"
   if(resetFlag == 4):
     print "\tReset Flag: Set"
   if(synFlag == 2):
     print "\tSyn Flag: Set"
   if(finFlag == True):
     print "\tFin Flag: Set"
   
   print "\tWindow: "+str(window)
   print "\tChecksum: "+str(checkSum)
   print "\tUrgent Pointer: "+str(urgPntr)

   packet = packet[20:]
   return packet

def udpHeader(newPacket):
  packet = struct.unpack("!4H",newPacket[0:8])
  srcPort = packet[0]
  dstPort = packet[1]
  lenght = packet[2]
  checkSum = packet[3]

  print "*******************UDP HEADER***********************"
  print "\tSource Port: "+str(srcPort)
  print "\tDestination Port: "+str(dstPort)
  print "\tLenght: "+str(lenght)
  print "\tChecksum: "+str(checkSum)
  
  packet = packet[8:]
  return packet

def error(message): 									#handling error when parse error
  print "*******************Parse ERROR***********************"
  print message+'\n'

def printdata(message):
  print "*******************Data***********************"
  print message

def ipv4Decoder(Packet):
  #for the circumstance of ip in ip,we should have the ipv4decoder function
  newPacket,nextProto = ipv4Header(Packet)
  if (nextProto == 'TCP'):
    remainingPacket = tcpHeader(newPacket)
  elif (nextProto == 'UDP'):
    remainingPacket = udpHeader(newPacket)
  elif (nextProto == 'ICMP'):
    icmp4Header(newPacket)
  elif (nextProto == 'IPV4'):
    ipv4Decoder(newPacket)
  elif (nextProto == 'IGMP'):
    igmpHeader(newPacket)
  elif (nextProto == 'IPV6'):
    ipv6Decoder(newPacket)
  elif (nextProto == 'NONE'):
    printdata(newPacket)
  else:
    error(nextProto) 

def ipv6Decoder(Packet):
  newPacket,nextProto = ipv6Header(Packet)
  if (nextProto == 'TCP'):
    remainingPacket = tcpHeader(newPacket)
  elif (nextProto == 'UDP'):
    remainingPacket = udpHeader(newPacket)
  elif (nextProto == 'ICMP'):
    icmp6Header(newPacket)
  elif (nextProto == 'IPV4'):
    ipv4Decoder(newPacket)
  elif (nextProto == 'IGMP'):
    igmpHeader(newPacket)
  elif (nextProto == 'IPV6'):
    ipv6Decoder(newPacket)
  elif (nextProto == 'NoMoreHeader'):
    printdata(newPacket)
  else:
    error(nextProto)

if __name__ == '__main__':
 while(True):
  newPacket,nextProto = '',''
  #os.system('clear')
  packet = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x003))
  receivedRawPacket = packet.recv(2048)
  resultingPacket,proto = etherHeader(receivedRawPacket)

  if (proto=='IPV4'):
    ipv4Decoder(resultingPacket)
  #elif (proto=='ARP'):
  # newPacket,nextProto = arpHeader(resultingPacket)
  elif (proto=='IPV6'):
   ipv6Decoder(resultingPacket)
  else:error(proto)

