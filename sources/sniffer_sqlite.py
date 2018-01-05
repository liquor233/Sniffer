#coding:utf-8 #initial_db()                                 初始化建立或链接数据库
#sqlite_start()                                             清空已有数据库中表格数据，每次抓包开始前调用
#insert_db(no,packet,srcip,dstip,sport,dport,ptype,stack)   抓包的同时调用，将数据存入数据库
#filter_db(srcip,dstip,sport,proco)                         显示过滤函数（源地址，目的地址，源端口，协议类型）返回的是表格中每行数据的序号，【】格式
#detail_packet(no)                                          输入序号，返回packet
#save_txt(file_name)                                        将数据库中除packet外的具体信息输出至指定文件名文件中，raw_input()函数获取用户输入文件名
#msg_find(msg)												输入查找的字符串，返回包含字符串的包的序号
#另外增加的函数
#information_packet                                         从数据库中读取相应packet的详细字段，包括端口号和ip号，用于在报文显示界面显示报文的简略信息
import sqlite3 as sq
from prettytable import PrettyTable

def initial_db():

    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    conn_db.text_factory=str

    cursor_db.execute('''CREATE TABLE IF NOT EXISTS pcap
                    (no int NOT NULL,
                    packet none NOT NULL,
                    srcip none NOT NULL,
                    dstip none NOT NULL,
                    sport none,
                    dport none,
                    ptype none NOT NULL);''')

    cursor_db.execute('''CREATE TABLE IF NOT EXISTS stack
                    (no int NOT NULL,
                    layer_first char NOT NULL,
                    layer_second char NOT NULL,
                    layer_third char NOT NULL,
                    layer_fourth char NOT NULL);''')

    cursor_db.execute('''CREATE TABLE ip
                    (no int NOT NULL,
                    identification none NOT NULL,
                    header int NOT NULL,
                    DF none NOT NULL,
                    MF none NOT NULL,
                    flagoffset int NOT NULL);''')

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def sqlite_start():

    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    conn_db.text_factory=str

    #cursor_db.execute('''DROP TABLE pcap''')
    cursor_db.execute('''CREATE TABLE pcap
                    (no int NOT NULL,
                    packet none NOT NULL,
                    srcip none NOT NULL,
                    dstip none NOT NULL,
                    sport none,
                    dport none,
                    ptype none NOT NULL);''')

    #cursor_db.execute('''DROP TABLE stack''')
    cursor_db.execute('''CREATE TABLE stack
                    (no int NOT NULL,
                    layer_first char NOT NULL,
                    layer_second char NOT NULL,
                    layer_third char NOT NULL,
                    layer_fourth char NOT NULL);''')

    cursor_db.execute('''CREATE TABLE ip
                    (no int NOT NULL,
                    identification none NOT NULL,
                    header none NOT NULL,
                    DF none NOT NULL,
                    MF none NOT NULL,
                    flagoffset none NOT NULL);''')


    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def insert_db(sno,spacket,ssrcip,sdstip,ssport,sdport,sptype,sstack):

    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    conn_db.text_factory=str

    cursor_db.execute("INSERT INTO pcap VALUES (?,?,?,?,?,?,?)",(sno,spacket,ssrcip,sdstip,ssport,sdport,sptype))
    cursor_db.execute("INSERT INTO stack VALUES (?,?,?,?,?)",(sno,sstack[0],sstack[1],sstack[2],sstack[3]))

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def filter_db(fsrcip,fdstip,fdport,fproco):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    conn_db.text_factory=str

    sort=[1,1,1,1]
    if(fsrcip=='-1'):
        sort[0]=0
    else: sort[0]=1
    if(fdstip=='-1'):
        sort[1]=0
    else: sort[1]=1
    if(fdport=='-1'):
        sort[2]=0
    else: sort[2]=1
    if(fproco=='-1'):
        sort[3]=0
    else: sort[3]=1

    result=[]

    if(sort==[0,0,0,0]):
        result=[]

    elif(sort==[1,0,0,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip",{"fsrcip":fsrcip})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[0,1,0,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE dstip=:fdstip",{"fdstip":fdstip})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[0,0,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE sport=:fdport",{"fdport":fdport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[0,0,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:fno",{"fno":row[0]})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[1,1,0,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND dstip=:fdstip",{"fsrcip":fsrcip,"fdstip":fdstip})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[1,0,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND sport=:fdport",{"fsrcip":fsrcip,"fdport":fdport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[1,0,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:fno AND srcip=:fsrcip",{"fno":row[0],"fsrcip":fsrcip})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[0,1,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE dstip=:fdstip AND sport=:fdport",{"fdstip":fdstip,"fdport":fdport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[0,1,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:fno AND dstip=:fdstip",{"fno":row[0],"fdstip":fdstip})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[0,0,1,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:fno AND sport=:fdport",{"fno":row[0],"fdport":fdport})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[1,1,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND dstip=:fdstip AND sport=:fdport",{"fsrcip":fsrcip,"fdstip":fdstip,"fdport":fdport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[1,1,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:fno AND srcip=:fsrcip AND dstip=:fdstip",{"fno":row[0],"fsrcip":fsrcip,"fdstip":fdstip})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[1,0,1,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND sport=:fdport AND no=:fno",{"fsrcip":fsrcip,"fdport":fdport,"fno":row[0]})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[0,1,1,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE dstip=:fdstip AND sport=:fdport AND no=:fno",{"fdstip":fdstip,"fdport":fdport,"fno":row[0]})
            for row in result_no.fetchall():
                result.append(row[0])

    else:
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2 OR layer_fourth=:fproco3",{"fproco1":fproco,"fproco2":fproco,"fproco3":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND dstip=:fdstip AND sport=:fdport AND no=:fno",{"fsrcip":fsrcip,"fdstip":fdstip,"fdport":fdport,"fno":row[0]})
            for row in result_no.fetchall():
                result.append(row[0])

    cursor_db.close()
    conn_db.close()

    return result


def detail_packet(sno):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()
    conn_db.text_factory=str

    reserch=cursor_db.execute("SELECT packet FROM pcap WHERE no=:sno",{"sno":sno})
    result=reserch.fetchone()
    cursor_db.close()
    conn_db.close()

    return result

def save_txt(file_name):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()
    conn_db.text_factory=str

    #file_name=raw_input()
    f=open(file_name,"w")

    reserch=cursor_db.execute("SELECT * FROM pcap")
    result=reserch.fetchall()

    x = PrettyTable(["number", "source_ip", "destination_ip", "source_port","destination_port","protocol"])
    x.align["number"] = "l"
    x.padding_width = 1

    for row in result:
        x.add_row([row[0],row[2], row[3], row[4],row[5],row[6]])

    print >>f,x

    f.close()
    cursor_db.close()
    conn_db.close()

def msg_find(msg):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()
    conn_db.text_factory=str

    result=[]

    reserch=cursor_db.execute("SELECT no,packet FROM pcap")
    reserch_no=reserch.fetchall()

    for row in reserch_no:
        if(row[1].find(msg)!=-1):
            result.append(row[0])

    cursor_db.close()
    conn_db.close()


    return result

def insert_ip(ino,iidentification,iheader,iDF,iMF,ioffset):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    conn_db.text_factory=str

    cursor_db.execute("INSERT INTO ip VALUES (?,?,?,?,?,?)",(ino,iidentification,iheader,iDF,iMF,ioffset))

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def ip_recombine(rno):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    conn_db.text_factory=str

    reserch=cursor_db.execute("SELECT * FROM ip WHERE no=:rno",{"rno":rno})
    result=reserch.fetchone()
    if result==None:
        return (-1)

    reserch1=cursor_db.execute("SELECT identification FROM ip WHERE no=:rno",{"rno":rno})
    reserch_id=reserch1.fetchone()
    result_id=reserch_id[0]

    reserch2=cursor_db.execute("SELECT * FROM ip WHERE identification=:result_id",{"result_id":result_id})
    reserch_ip=reserch2.fetchall()
    
    array_length=0
    for row in reserch_ip:
        reserch=cursor_db.execute("SELECT packet FROM pcap WHERE no=:row0",{"row0":row[0]})
        reserch_packet=reserch.fetchone()
        
        result=reserch_packet[0]
        header=row[2]
        
        if row[5]==0 :
            length=len(result)
        else:
            length=len(result[header-1:])
        
        array_length+=length
        
    packet_recombine=['0']*array_length
        
    for row in reserch_ip:
        reserch=cursor_db.execute("SELECT packet FROM pcap WHERE no=:row0",{"row0":row[0]})
        reserch_packet=reserch.fetchone()
        result=reserch_packet[0]

        header=row[2]
        packet=result[header-1:]
        length=len(packet)
        offset=row[5]*8

        if(row[5]==0):
            packet_recombine[0:(header+length-1)]=result
        else:
            packet_recombine[offset:(offset+length-1)]=packet

    packet_recombine_result=''
    for row in packet_recombine:
        packet_recombine_result=packet_recombine_result+row


    conn_db.commit()
    cursor_db.close()
    conn_db.close()

    return packet_recombine_result

def information_packet(sno):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()
    conn_db.text_factory=str

    reserch=cursor_db.execute("SELECT srcip,dstip,sport,dport,ptype FROM pcap WHERE no=:sno",{"sno":sno})
    result=reserch.fetchone()
    cursor_db.close()
    conn_db.close()

    return result

