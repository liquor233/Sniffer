#coding:utf-8 #initial_db()                                               初始化建立或链接数据库
#sqlite_start()                                             清空已有数据库中表格数据，每次抓包开始前调用
#insert_db(no,packet,srcip,dstip,sport,dport,ptype,stack)   抓包的同时调用，将数据存入数据库
#filter_db(srcip,dstip,sport,proco)                         查询过滤函数，返回的是表格中每行数据的序号，【】格式
#detail_packet(no)                                          输入序号，返回packet
#save_txt()                                                 将数据库中除packet外的具体信息输出至指定文件名文件中，raw_input()函数获取用户输入文件名
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
                    layer_third char NOT NULL);''')

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
                    layer_third char NOT NULL);''')

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def insert_db(sno,spacket,ssrcip,sdstip,ssport,sdport,sptype,sstack):

    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    conn_db.text_factory=str

    cursor_db.execute("INSERT INTO pcap VALUES (?,?,?,?,?,?,?)",(sno,spacket,ssrcip,sdstip,ssport,sdport,sptype))
    cursor_db.execute("INSERT INTO stack VALUES (?,?,?,?)",(sno,sstack[0],sstack[1],sstack[2]))

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def filter_db(fsrcip,fdstip,fsport,fproco):
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
    if(fsport=='-1'):
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
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE sport=:fsport",{"fsport":fsport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[0,0,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT　no FROM pcap WHERE no=:reserch",{"reserch":row[0]})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[1,1,0,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND dstip=:fdstip",{"fsrcip":fsrcip,"fdstip":fdstip})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[1,0,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND sport=:fsport",{"fsrcip":fsrcip,"fsport":fsport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[1,0,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:sno AND srcip=:fsrcip",{"sno":row[0],"fsrcip":fsrcip})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[0,1,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE dstip=:fdstip AND sport=:fsport",{"fdstip":fdstip,"fsport":fsport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[0,1,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:sno AND dstip=:fdstip",{"sno":row[0],"fdstip":fdstip})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[0,0,1,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:sno AND sport=:fsport",{"sno":row[0],"fsport":fsport})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[1,1,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND dstip=:fdstip AND sport=:fsport",{"fsrcip":fsrcip,"fdstip":fdstip,"fsport":fsport})
        for row in reserch.fetchall():
            result.append(row[0])

    elif(sort==[1,1,0,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE no=:sno AND srcip=:fsrcip AND dstip=:fdstip",{"sno":row[0],"fsrcip":fsrcip,"fdstip":fdstip})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[1,0,1,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND sport=:fsport AND no=:sno",{"fsrcip":fsrcip,"fsport":fsport,"sno":row[0]})
            for row in result_no.fetchall():
                result.append(row[0])

    elif(sort==[0,1,1,1]):
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE dstip=:fdstip AND sport=:fsport AND no=:sno",{"fdstip":fdstip,"fsport":fsport,"sno":row[0]})
            for row in result_no.fetchall():
                result.append(row[0])

    else:
        reserch=cursor_db.execute("SELECT no FROM stack WHERE layer_second=:fproco1 OR layer_third=:fproco2",{"fproco1":fproco,"fproco2":fproco})
        reserch_no=reserch.fetchall()
        for row in reserch_no:
            result_no=cursor_db.execute("SELECT no FROM pcap WHERE srcip=:fsrcip AND dstip=:fdstip AND sport=:fsport AND no=:sno",{"fsrcip":fsrcip,"fdstip":fdstip,"fsport":fsport,"sno":row[0]})
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
