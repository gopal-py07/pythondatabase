from mysql.connector import connect,Error
Connection=connect(host="localHost",user="root",password="root",charset="utf8",db="python")
print(Connection.is_connected())
Cursor=Connection.cursor()#for submit the quarry
print(Cursor)#1st run=MySQLCursor: (Nothing executed yet)
#Cursor.execute('create table studnet(rollno int(30),name char(30),addr char(30))')
Cursor.execute("insert into studnet values(1,'pqr','karanja')")
#Cursor.execute("insert into studnet values(%s,%s,%s)",(int("2"),"pqr","karanja"))


Connection.commit()#it is compalsary to commite

#Cursor.close()
#Connection.close()
