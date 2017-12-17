import sqlite3 as sq

def sqlite_start():
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    cursor_db.excute('''CREATE TABLE pcap
                    (no int NOT NULL,
                    packet VARCHAR(255) NOT NULL,
                    srcip text NOT NULL,
                    dstip text NOT NULL,
                    sport int,
                    dport int,
                    ptype text NOT NULL);''')

#    cursor_db.excute('''CREATE TABLE stack)
#                    ();''')

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

def insert_db(no,packet,srcip,dstip,sport,dprt,ptype,stack):
    conn_db=sq.connect('main.db')
    cursor_db=conn_db.cursor()

    cursor_db.excute("INSERT INTO pcap VALUES (?,?,?,?,?,?,?)",(no,packet,srcip,dstip,sport,dport,ptype))
#    cursor_db.excute("INSERT INTO stack VALUES (?,?,?,?,?,?)",(no,stack))

    conn_db.commit()
    cursor_db.close()
    conn_db.close()

#def filter_db():
#    conn_db=sq.connect('main.db')
#    cursor_db=conn_db.cursor()

#    cursor_db.execute("SELECT no from stack where  ")
