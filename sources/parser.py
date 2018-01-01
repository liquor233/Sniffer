import socket
import os
import struct
import binascii 

#for format output
star='*'*20
fmt = star+"{0:^18}"+star
tag='\r\n'

def etherHeader(packet):
  IpHeader = struct.unpack("!6s6sH",packet[0:14]) #ipv4==0x0800
  dstMac = binascii.hexlify(IpHeader[0]) #source MAC address. converts binary data into ascii dt looks like hex. MAC address is always in hex format.
  srcMac = binascii.hexlify(IpHeader[1]) #Destination MAC address
  protoType = IpHeader[2] #next protocol (ip/ipv4,arp,icmp,ipv6)
  nextProto = hex(protoType) #hex() returns a string. it a built in finction

  message=fmt.format("ETHER HEADER")+tag
  message+= "\tDestination MAC: "+dstMac[0:2]+":"+dstMac[0:2]+":"+dstMac[2:4]+":"+dstMac[4:6]+":"+dstMac[6:8]+":"+dstMac[8:10]+":"+dstMac[10:]+tag
  message+= "\tsource MAC: "+srcMac[0:2]+":"+srcMac[0:2]+":"+srcMac[2:4]+":"+srcMac[4:6]+":"+srcMac[6:8]+":"+srcMac[8:10]+":"+srcMac[10:]+tag

  message+= "\tNext Protocol: "+nextProto+tag

  if (nextProto == '0x800'): 
     proto = 'IPV4'
  elif (nextProto == '0x806'): 
     proto = 'ARP'
  elif (nextProto == '0x86dd'): 
     proto = 'IPV6'
  else: proto='unsupported ethernet header'

  packet = packet[14:]
  return packet,proto,message

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

   message=fmt.format("IPV4 HEADER")+tag
   message+= "\tVersion: "+str(version)+tag
   message+= "\tHeader Lenght: "+str(headerLenght)+tag
   message+= "\tType Of Service: "+str(typeOfService)+tag
   message+= "\tTotal Lenght: "+str(totalLenght) +tag
   message+= "\tIdentification: "+str(identification) +tag
   message+="\tFlags: "+str(flags) +tag
   message+= "\tFragment Offset: "+str(fragOffSet) +tag
   message+= "\tTll: "+str(ttl)+tag
   message+= "\tNext Protocol: "+str(protocol) +tag
   message+= "\tHeader checksum: "+str(hdrChkSum) +tag
   message+= "\tSource Address: "+srcAddress +tag
   message+= "\tDestination Address: "+dstAddress +tag

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
   return data, nextProto,message
   
def icmp4Header(newPacket):
  packet = struct.unpack("!BBH",newPacket[:4])
  typedict = {'0':'EchoReply','3':'unreachable','5':'redirection','8':'Echo'}
  Type=packet[0]
  if Type in [0,3,5,8]:Type=typedict[str(Type)]
  message= fmt.format("ICMP4 HEADER")+tag
  message+= "\tType: " + str(Type)+tag
  message+= "\tCode: " + str(packet[1])+tag
  message+= "\tchecksum: "+str(packet[2])+tag
  #message+= "\tidentifier: "+str(packet[3]) 						#because it is optional , so we don't show it	+tag
  #message+= "\tsequence: "+str(packet[4])+tag
  message+= "\tdata(if have): "+str(newPacket[4:])+tag
  return message

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
  message= fmt.format("IPV6 HEADER")+tag
  message+= "\tVersion: "+str(version)+tag
  message+= "\tTraffic Class: "+str(TC)+tag
  message+= "\tFlow Label: "+str(FlowLabel)+tag
  message+= "\tpayloadlength Lenght: "+str(payloadLength)+tag
  message+= "\tNext Protocol: "+str(protocol)+tag
  message+= "\tHopLimited: "+str(ttl)+tag
  message+= "\tSource Address: "+srcAddress+tag
  message+= "\tDestination Address: "+dstAddress+tag
  if protocol in [0,58,59,2,4,6,17,41,44,43,50,51,60]:nextProto=protodict[str(protocol)]
  else : nextProto='no supported IPV6 protocol type'
  data = newPacket[40:]
  return data, nextProto,message

def icmp6Header(newPacket):
  packet = struct.unpack("!BBH",newPacket[:4])
  typedict = {'129':'EchoReply','1':'unreachable','2':'oversize packet','3':'timeout','4':'paramerror','128':'Echo'}
  Type=packet[0]
  if Type in [1,2,3,4,128,129]:Type=typedict[str(Type)]
  message= fmt.format("ICMP6 HEADER")+tag
  message+= "\tType: " + str(Type)+tag
  message+= "\tCode: " + str(packet[1])+tag
  message+= "\tchecksum: "+str(packet[2])+tag
  data = newPacket[4:]
  message+=printdata(data)
  return message

def igmpHeader(newPacket):
  packet = struct.unpack("!BBH4s",newPacket[8:])
  message= fmt.format("IGMP HEADER")+tag
  message+= "\tType: " + hex(packet[0])+tag
  message+= "\tMaxRespTime: " + str(packet[1])+tag
  message+= "\tchecksum: " + str(packet[2])+tag
  message+= "\tgroupID: " + socket.inet_ntoa(packet[3])					#group ID is an IP+tag
  return message

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
   

   message=fmt.format("TCP HEADER")+tag
   message+= "\tSource Port: "+str(srcPort)+tag
   message+= "\tDestination Port: "+str(dstPort)+tag
   message+= "\tSequence Number: "+str(sqncNum)+tag
   message+= "\tAck. Number: "+str(acknNum)+tag
   message+= "\tData Offset: "+str(dataOffset)+tag
   message+= "\tReserved: "+str(reserved)+tag
   message+= "\tTCP Flags: "+str(tcpFlags)+tag

   if(urgFlag == 32):
     message+= "\tUrgent Flag: Set"+tag
   if(ackFlag == 16):
     message+= "\tAck Flag: Set"+tag
   if(pushFlag == 8):
     message+= "\tPush Flag: Set"+tag
   if(resetFlag == 4):
     message+= "\tReset Flag: Set"+tag
   if(synFlag == 2):
     message+= "\tSyn Flag: Set"+tag
   if(finFlag == True):
     message+= "\tFin Flag: Set"+tag
   
   message+= "\tWindow: "+str(window)+tag
   message+= "\tChecksum: "+str(checkSum)+tag
   message+= "\tUrgent Pointer: "+str(urgPntr)+tag

   packet = newPacket[20:]
   message+=printdata(packet)
   return message

def udpHeader(newPacket):
  packet = struct.unpack("!4H",newPacket[0:8])
  srcPort = packet[0]
  dstPort = packet[1]
  lenght = packet[2]
  checkSum = packet[3]

  message= fmt.format("UDP HEADER")+tag
  message+= "\tSource Port: "+str(srcPort)+tag
  message+= "\tDestination Port: "+str(dstPort)+tag
  message+= "\tLenght: "+str(lenght)+tag
  message+= "\tChecksum: "+str(checkSum)+tag
  
  message+=printdata(newPacket[8:])
  return message

def error(message): 									#handling error when parse error
  returnmessage= fmt.format("PARSER ERROR")+tag
  returnmessage+= message+tag
  return returnmessage

def printdata(message):
  returnmessage= fmt.format("DATA")+tag
  returnmessage+= message+tag
  return returnmessage

def ipv4Decoder(Packet):
  #for the circumstance of ip in ip,we should have the ipv4decoder function
  newPacket,nextProto,message = ipv4Header(Packet)
  if (nextProto == 'TCP'):
    message+=tcpHeader(newPacket)
  elif (nextProto == 'UDP'):
    message+=udpHeader(newPacket)
  elif (nextProto == 'ICMP'):
    message+=icmp4Header(newPacket)
  elif (nextProto == 'IPV4'):
    message+=ipv4Decoder(newPacket)
  elif (nextProto == 'IGMP'):
    message+=igmpHeader(newPacket)
  elif (nextProto == 'IPV6'):
    message+=ipv6Decoder(newPacket)
  elif (nextProto == 'NONE'):
    message+=printdata(newPacket)
  else:
    message+=error(nextProto)
  return message 

def ipv6Decoder(Packet):
  newPacket,nextProto,message = ipv6Header(Packet)
  if (nextProto == 'TCP'):
    message+=tcpHeader(newPacket)
  elif (nextProto == 'UDP'):
    message+=udpHeader(newPacket)
  elif (nextProto == 'ICMP'):
    message+=icmp6Header(newPacket)
  elif (nextProto == 'IPV4'):
    message+=ipv4Decoder(newPacket)
  elif (nextProto == 'IGMP'):
    message+=igmpHeader(newPacket)
  elif (nextProto == 'IPV6'):
    message+=ipv6Decoder(newPacket)
  elif (nextProto == 'NoMoreHeader'):
    message+=printdata(newPacket)
  else:
    message+=error(nextProto)
  return message

def arpHeader(Packet):
  packet = struct.unpack("!2H2BH6s4s6s4s",Packet)
  hardtype = packet[0]
  prototype = packet[1]
  hardaddresslen = packet[2]
  protocollen = packet[3]
  opercode = packet[4]
  srcMac = binascii.hexlify(packet[5])
  srcAddress = socket.inet_ntoa(packet[6])
  dstMac = binascii.hexlify(packet[7])
  dstAddress = socket.inet_ntoa(packet[8])
  message= fmt.format("ARP HEADER")+tag
  message+= "\thardware type is: "+str(hardtype)+tag
  message+= "\tprotocol type is: "+str(prototype)+tag
  message+= "\thardware address length is: "+str(hardaddresslen)+tag
  message+= "\tprotocol length is: "+str(protocollen)+tag
  message+= "\topercode is: "+str(opercode)+tag
  message+= "\tsource MAC: "+srcMac[0:2]+":"+srcMac[0:2]+":"+srcMac[2:4]+":"+srcMac[4:6]+":"+srcMac[6:8]+":"+srcMac[8:10]+":"+srcMac[10:]+tag
  message+= "\tSource Address: "+srcAddress +tag
  message+= "\tDestination MAC: "+dstMac[0:2]+":"+dstMac[0:2]+":"+dstMac[2:4]+":"+dstMac[4:6]+":"+dstMac[6:8]+":"+dstMac[8:10]+":"+dstMac[10:]+tag
  message+= "\tDestination Address: "+dstAddress +tag
  return message


    

def GetDetail(receivedRawPacket):
  resultingPacket,proto,message=etherHeader(receivedRawPacket)
  if (proto=='IPV4'):
    message+=ipv4Decoder(resultingPacket)
  elif (proto=='ARP'):
    message += arpHeader(resultingPacket)
  elif (proto=='IPV6'):
    message+=ipv6Decoder(resultingPacket)
  else:
    message+=error("unsupported proto! num is\t"+proto)
  return message

if __name__ == '__main__':
  sniffer=socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
  while(True):
    packet,_=sniffer.recvfrom(65565)
    print GetDetail(packet)
