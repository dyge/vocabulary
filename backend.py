import mysql.connector
from datetime import datetime,timedelta
import configparser

config = configparser.ConfigParser()
config.read("/Users/sinaandreas/Desktop/MeinOrder/Meine_Projekte/Lernprogramm/myconf.ini") #/Users/sinaandreas/Desktop/Projekte/Lernprogramm/myconf.ini

def ConfigSectionMap(section):
    dict1={}
    options=config.options(section)
    for option in options:
        try:
            dict1[option]=config.get(section,option)
            if dict1[option]==-1:
                DebugPrint("skip: %s" %option)
        except:
            print("exception on %s!" %option)
            dict1[option]=None
    return dict1

user = ConfigSectionMap("Database")['user']
password = ConfigSectionMap("Database")['password']
host = ConfigSectionMap("Database")['host']
database = ConfigSectionMap("Database")['database']

conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
cur = conn.cursor(buffered=True)

def alle_del(c):
    try:
        if c == "Englisch":
            cur.execute("DROP TABLE IF EXISTS engvoc")
            neuetab("Englisch")
        elif c == "Latein":
            cur.execute("DROP TABLE IF EXISTS latvoc")
            neuetab("Latein")
    except:
        print("error alle_del")

def neuetab(c):
    try:
        if c == "Englisch":
            cur.execute("""CREATE TABLE IF NOT EXISTS engvoc(id INT AUTO_INCREMENT PRIMARY KEY, eng TEXT, de1 TEXT, de2 TEXT, de3 TEXT, de4 TEXT, de5 TEXT, zeit DATE, pos TINYINT)""")
            conn.commit()
        elif c == "Latein":
            cur.execute("""CREATE TABLE IF NOT EXISTS latvoc(id INT AUTO_INCREMENT PRIMARY KEY, la TEXT, de1 TEXT, de2 TEXT, de3 TEXT, de4 TEXT, de5 TEXT, zeit DATE, pos TINYINT)""")
            conn.commit()
    except:
        print("error neuetab")

def neu(de1,de2,de3,de4,de5,en,c):
    if c == "Englisch":
        cur.execute("""SELECT * FROM engvoc WHERE eng=%s AND de1=%s AND de2=%s AND de3=%s AND de4=%s AND de5=%s""", (en,de1,de2,de3,de4,de5))
        exist = cur.fetchone()
        if not exist:
            cur.execute("""INSERT INTO engvoc(eng,de1,de2,de3,de4,de5,zeit,pos) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", (en,de1,de2,de3,de4,de5,datetime.now().date(),1))
            conn.commit()
    elif c == "Latein":
        cur.execute("""SELECT * FROM latvoc WHERE la=%s AND de1=%s AND de2=%s AND de3=%s AND de4=%s AND de5=%s""", (en,de1,de2,de3,de4,de5))
        exist = cur.fetchone()
        if not exist:
            cur.execute("""INSERT INTO latvoc(la,de1,de2,de3,de4,de5,zeit,pos) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", (en,de1,de2,de3,de4,de5,datetime.now().date(),1))
            conn.commit()

def delrow(de1,de2,de3,de4,de5,en,c):
    try:
        if c == "Englisch":
            cur.execute("""DELETE FROM engvoc WHERE eng=%s AND de1=%s AND de2=%s AND de3=%s AND de4=%s AND de5=%s""", (en,de1,de2,de3,de4,de5))
            conn.commit()
        elif c == "Latein":
            cur.execute("""DELETE FROM latvoc WHERE la=%s AND de1=%s AND de2=%s AND de3=%s AND de4=%s AND de5=%s""", (en,de1,de2,de3,de4,de5))
            conn.commit()
    except:
        conn.rollback()
        print("error delrow")

def alle(c):
    try:
        if c == "Englisch":
            cur.execute("SELECT * FROM engvoc WHERE pos=1")
            return cur
        elif c == "Latein":
            cur.execute("SELECT * FROM latvoc WHERE pos=1")
            return cur
    except:
        print("error alle")

def a(c):
    try:
        if c == "Englisch":
            cur.execute("""SELECT * FROM engvoc WHERE zeit <= %s""", (datetime.now().date(),))
            return cur
        elif c == "Latein":
            cur.execute("""SELECT * FROM latvoc WHERE zeit <= %s""", (datetime.now().date(),))
            return cur
    except:
        print("error a")

def change(en,de1,de2,de3,de4,de5,p,z,c):
    try:
        if c == "Englisch":
            cur.execute("""UPDATE engvoc SET pos=%s, zeit=%s WHERE eng=%s AND de1=%s AND de2=%s AND de3=%s AND de4=%s AND de5=%s""", (p,z,en,de1,de2,de3,de4,de5))
        elif c == "Latein":
            cur.execute("""UPDATE latvoc SET pos=%s, zeit=%s WHERE la=%s AND de1=%s AND de2=%s AND de3=%s AND de4=%s AND de5=%s""", (p,z,en,de1,de2,de3,de4,de5))
    except:
        print("error change")

def all(c):
    try:
        if c == "Englisch":
            cur.execute("""SELECT * FROM engvoc""")
            return cur
        elif c == "Latein":
            cur.execute("""SELECT * FROM latvoc""")
            return cur
    except:
        print("error a")

def up_row(en,de1,de2,de3,de4,de5,c):
    try:
        if c == "Englisch":
            cur.execute("""UPDATE engvoc SET eng=%s,de1=%s,de2=%s,de3=%s,de4=%s,de5=%s,pos=1,zeit=%s WHERE eng=%s""", (en,de1,de2,de3,de4,de5,datetime.now().date(),en))
        elif c == "Latein":
            cur.execute("""UPDATE latvoc SET la=%s,de1=%s,de2=%s,de3=%s,de4=%s,de5=%s,pos=1,zeit=%s WHERE la=%s""", (en,de1,de2,de3,de4,de5,datetime.now().date(),en))
    except:
        print("error up_row")

def zeit_ber(p):
    werte = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':10,'8':15,'9':30,'10':50}
    return datetime.now().date()+timedelta(days=werte[p])

def s2(t,c):
    try:
        if c == "Englisch":
            cur.execute("""SELECT * FROM engvoc WHERE de1=%s OR de2=%s OR de3=%s OR de4=%s OR de5=%s""", (t,t,t,t,t))
            return cur
        elif c == "Latein":
            cur.execute("""SELECT * FROM latvoc WHERE de1=%s OR de2=%s OR de3=%s OR de4=%s OR de5=%s""", (t,t,t,t,t))
            return cur
    except:
        print("error s")

def s1(t,c):
    try:
        if c == "Englisch":
            cur.execute("""SELECT * FROM engvoc WHERE eng=%s""", (t,))
            return cur
        elif c == "Latein":
            cur.execute("""SELECT * FROM latvoc WHERE la=%s""", (t,))
            return cur
    except:
        print("error s")

neuetab("Englisch")
neuetab("Latein")
