from mysql.connector import connect
Connection=connect(host='localhost',user='root',password='root',charset='utf8',db="python")
#for submeting the quary we use cursor obj
Cursor=Connection.cursor()
sql_quary="insert into employee values(%s,%s,%s,%s)"
#insert value through user
eid=int(input("enter employee id "))
ename=input("enter employee name ")
eadd=(input("enter employee address "))
eage=(int(input("enter emloyee age ")))
#valuetuple=(eid,ename,eadd)1]IndexError: tuple index out of range, 2]Cursor.execute(sql_quary,valuetuple)#raise errors.ProgrammingError(mysql.connector.errors.ProgrammingError: Not enough parameters for the SQL statement
valuetuple=(eid,ename,eadd,eage)
Cursor.execute(sql_quary,valuetuple)
print("data enter suceffuly")
Connection.commit()
