from mysql.connector import connect
connection=connect(host="localhost",user="root",password="root",charset="utf8",db="python")
print(connection.is_connected())#to check whether the connection is connect or not to mysql
Cursor=connection.cursor()
#s_quary="create table stu (rollno int(30),name varchar(30),addr varchar(30))"
#Cursor.execute(s_quary)

args=Cursor.callproc('insert1',(2,'xyz','pqr'))
print(args)
connection.commit()

'''DELIMITER $$

DROP PROCEDURE IF EXISTS `insert1` $$
CREATE PROCEDURE `python`.`insert1`(IN rollno INT,IN name varchar(25),IN addr varchar(25))
BEGIN
insert into stu values(rollno,name,addr);
END $$

DELIMITER ;'''
