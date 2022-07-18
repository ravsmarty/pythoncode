import mysql.connector as conn 
mydb = conn.connect(host="localhost",user="root",passwd="8979552178Uma@")
#print(mydb)
cursor=mydb.cursor()


mydb.commit()
cursor.execute("select *  from smarty.clean")

l=[]
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))


