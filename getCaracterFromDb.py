<<<<<<< HEAD
import pymysql
from caracter import Caracter



db= pymysql.connect(host="localhost",user="root",  
    password="",db="fire_emblem_db")

def getName(n):
    cur = db.cursor()
    sql = "select nom from armes where id = %s"
    cur.execute(sql, n)
    result = cur.fetchone()

    return result[0]

  
cur = db.cursor()
features = []
 
sql = "select * from personnage where id = %s"  
try:  
    cur.execute(sql, 1)      
  
    results = cur.fetchall()    
  
    for row in results :
        for i in range(len(row)):
            if i == 10 or i ==11 :
                features.append(getName(row[i]))
            else :
                features.append(row[i])
    person = Caracter(features[0],features[1],features[2],features[3],features[4],features[5],
                      features[6],features[7],features[8],features[9],features[10],
                      features[11],features[12],features[13],features[14],features[15])
    person.display()
except Exception as e:  
    raise e  
finally:  
    db.close()
=======
import pymysql
from caracter import Caracter



db= pymysql.connect(host="localhost",user="root",  
    password="",db="fire_emblem_db")

def getName(n):
    cur = db.cursor()
    sql = "select nom from armes where id = %s"
    cur.execute(sql, n)
    result = cur.fetchone()

    return result[0]

  
cur = db.cursor()
features = []
 
sql = "select * from personnage where id = %s"  
try:  
    cur.execute(sql, 1)      
  
    results = cur.fetchall()    
  
    for row in results :
        for i in range(len(row)):
            if i == 10 or i ==11 :
                features.append(getName(row[i]))
            else :
                features.append(row[i])
    person = Caracter(features[0],features[1],features[2],features[3],features[4],features[5],
                      features[6],features[7],features[8],features[9],features[10],
                      features[11],features[12],features[13],features[14],features[15])
    person.display()
except Exception as e:  
    raise e  
finally:  
    db.close()
>>>>>>> 1a15999596ac823658c80ab41022570fae79ad63
