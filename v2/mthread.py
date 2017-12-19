from socket import *
#from sniffer_sqlite import *
import struct

class CountdownTask:
  def __init__(self):
    self._running = True

  def terminate(self):
    self._running = False

  def run(self,nic,pp):
    self._running = True
    sniffer=socket(AF_PACKET,SOCK_RAW,htons(0x0003))
    if nic != 'any':sniffer.bind((nic,0))
    while(self._running):
      packet,_=sniffer.recvfrom(65565)
      pp.put(packet)

def GetProtoType(Packet):
  #this is a function to get proto type
  #it will return a stack of proto type which is in use in the pakcet
  #not consider the situation ip in ip
  pstack = []
  ethtype=struct.unpack("!H",Packet[12:14])
  Packet=Packet[14:]

  tcpdict={'110':'POP3','21':'FTP','22':'SSH','23':'TELNET','25':'SMTP','80':'HTTP','8008':'HTTP','443':'HTTPS'}
  tcpport=[21,22,23,25,110,80,443,8008]
  udpdict={'53':'DNS'}
  udpport=[53]

  srcport,dstport=('-1','-1')

  pstack.append('ethernet');ptype=0
  if ethtype[0]==0x800:
    pstack.append('ip4')
    iproto=struct.unpack("!B",Packet[9])
    if iproto[0]==6:
      pstack.append('tcp')
      srcport,dstport=struct.unpack("!2H",Packet[20:24])
      if dstport in tcpport:
        pstack.append(tcpdict[str(dstport)])
      elif srcport in tcpport:
        pstack.append(tcpdict[str(srcport)])
      else : pstack.append('-1');ptype='tcp'
    elif iproto[0]==17:
      pstack.append('udp')
      srcport,dstport=struct.unpack("!2H",Packet[20:24])
      if dstport in udpport:
        pstack.append(udpdict[str(dstport)])
      elif srcport in udpport:
        pstack.append(udpdict[str(srcport)])
      else : pstack.append('-1');ptype='udp'
    elif iproto[0]==2:
      pstack.append('igmp');ptype='igmp'
    elif iproto[0]==1:
      pstack.append('icmp');ptype='icmp4'
    else : pstack.append('-1');ptype='ip4'
  elif ethtype[0]==0x806:
    pstack.append('arp')
    pstack.append('-1');ptype='arp'
  elif ethtype[0]==0x86dd:
    pstack.append('ip6')
    iproto=struct.unpack("!B",Packet[6])
    if iproto[0]==6:
      pstack.append('tcp')
      srcport,dstport=struct.unpack("!2H",Packet[40:44])
      if dstport in tcpport:
        pstack.append(tcpdict[str(dstport)])
      elif srcport in tcpport:
        pstack.append(tcpdict[str(srcport)])
      else : pstack.append('-1');ptype='tcp'
    elif iproto[0]==17:
      pstack.append('udp')
      srcport,dstport=struct.unpack("!2H",Packet[40:44])
      if dstport in tcpport:
        pstack.append(tcpdict[str(dstport)])
      elif srcport in udpport:
        pstack.append(udpdict[str(srcport)])
      else : pstack.append('-1');ptype='udp'
    elif iproto[0]==2:   
      pstack.append('igmp');ptype='igmp'
    elif iproto[0]==58:
      pstack.append('icmp');ptype='icmp6'
    else : pstack.append('-1');ptype='ip6'
  else:pstack.append('-1');pstack.append('-1');ptype='ethernet'
  if not ptype:ptype=pstack[-1]
  return pstack[:3],ptype,srcport,dstport

def GetIp(Packet,stack):
  Packet=Packet[14:]
  srcip,dstip=('-1','-1')
  if ('ip6' in stack):
    packet=struct.unpack("!16s16s",Packet[8:40])
    srcip=inet_ntop(AF_INET6, packet[0])
    dstip=inet_ntop(AF_INET6, packet[1])
  elif ('ip4' in stack):
    packet=struct.unpack("!4s4s",Packet[12:20])
    srcip = inet_ntoa(packet[0])
    dstip = inet_ntoa(packet[1])
  return srcip,dstip

if __name__=="__main__":
    from multiprocessing import Pipe,Process
    import os
    pr,ps=Pipe(0)
    w = Process(target=capture,args=('any',ps,))
    w.start()
#database initialize
    no=0
    #sqlite_start()
    while(True):
        packet = pr.recv()
        no=no+1
	stack,ptype,sport,dport = GetProtoType(packet)
 	srcip,dstip=GetIp(packet,stack)
 	message=ptype
	if srcip!='-1':
 	  message+='\tFrom '+srcip
	if sport !='-1':
	  message+=':'+str(sport)
	if dstip != '-1':
	  message+='\tTo: '+dstip
	if dport!='-1':
 	  message+=': '+str(dport)
    	print message
    # here insert your database function
    # those segment should be saved:packet,stack,sport,dport,ptype
    # srcip,dstip
        insert_db(no,packet,srcip,dstip,sport,dprt,ptype,stack)
