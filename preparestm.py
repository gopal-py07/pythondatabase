from mysql.connector import connect
Connection = connect(host="localhost",user="root",password="root",charset="utf8",db="python")
print(Connection.is_connected())
Cursor=Connection.cursor()
print(Cursor)
#print("creattable for employee first")
#sql_quary_for_cratetable="create table employee(e_id int(30),e_name char(30),e_add char(30),emp_age int(30))"
#Cursor.execute(sql_quary_for_cratetable)
print("inserting value for emlployee by using prparestatement")
sql_quary="insert into employee values(%s,%s,%s,%s)"
#for preapre statement we have to send values in tupal formate
valuetupal=(101,'gopAL','vilegaon',25)
Cursor.execute(sql_quary,valuetupal)
#if i given 4value ans i used %s 3time in sql_quary==>  raise errors.ProgrammingError(mysql.connector.errors.ProgrammingError: Not all parameters were used in the SQL statement

Connection.commit()
