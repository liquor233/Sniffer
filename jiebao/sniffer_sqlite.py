#coding:utf-8
import sqlite3 as sq

def sqlite_start():

    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()
    conn_db.text_factory=str
    cursor_db.execute('''DROP TABLE pcap''')
    cursor_db.execute('''CREATE TABLE pcap
                    (no int NOT NULL,
                    packet none NOT NULL,
                    srcip none NOT NULL,
                    dstip none NOT NULL,
                    sport none,
                    dport none,
                    ptype none NOT NULL);''')

    cursor_db.execute('''DROP TABLE stack''')
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
#    cursor_db.execute("INSERT INTO pcap VALUES (?,?,?,?,?,?,?)",(sno,unicode(spacket),unicode(ssrcip),unicode(sdstip),ssport,sdport,unicode(sptype)))
    cursor_db.execute("INSERT INTO stack VALUES (?,?,?,?)",(sno,sstack[0],sstack[1],sstack[2]))

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def filter_db(fsrcip,fdstip,fsport,fproco):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

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

    if(sort==[0,0,0,0]):
        result=0
    elif(sort==[1,0,0,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip==fsrcip")
        result=reserch.fetchall()
    elif(sort==[0,1,0,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE dstip==fdstip")
        result=reserch.fetchall()
    elif(sort==[0,0,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE sport==fsport")
        result=reserch.fetchall()
    elif(sort==[0,0,0,1]):
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT　no FROM pcap WHERE no==reserch_no")
        result=reserch.fetchall()
    elif(sort==[1,1,0,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip==fsrcip AND dstip==fdstip")
        result=reserch.fetchall()
    elif(sort==[1,0,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip==fsrcip AND sport==fsport")
        result=reserch.fetchall()
    elif(sort==[1,0,0,1]):
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE no==reserch_no AND srcip==fsrcip")
        result=reserch.fetchall()
    elif(sort==[0,1,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE dstip==fdstip AND sport==fsport")
        result=reserch.fetchall()
    elif(sort==[0,1,0,1]):
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE no==reserch_no AND dstip==fdstip")
        result=reserch.fetchall()
    elif(sort==[0,0,1,1]):
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE no==reserch_no AND sport==fsport")
        result=reserch.fetchall()
    elif(sort==[1,1,1,0]):
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip==fsrcip AND dstip==fdstip AND sport==fsport")
        result=reserch.fetchall()
    elif(sort==[1,1,0,1]):
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE no==reserch_no AND srcip==fsrcip AND dstip==fdstip")
        result=reserch.fetchall()
    elif(sort==[1,0,1,1]):
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip==fsrcip AND sport==fsport AND no==reserch_no")
        result=reserch.fetchall()
    elif(sort==[0,1,1,1]):
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE dstip==fdstip AND sport==fsport AND no==reserch_no")
        result=reserch.fetchall()
    else:
        reserch_no=cursor_db.execute("SELECT no FROM stack WHERE layer_second==fproco OR layer_third==fproco")
        reserch=cursor_db.execute("SELECT no FROM pcap WHERE srcip==fsrcip AND dstip==fdstip AND sport==fsport AND no==reserch_no")
        result=reserch.fetchall()
