from mysql.connector import connect
Connection=connect(host='localhost',user='root',password='root',charset='utf8',db='python')
print(Connection.is_connected())
Cursor=Connection.cursor()
sql_quary='insert into employee'
n=int(input("how many data do you want to add into employee table :"))
emp_list=[]
i=0
while i<n:
    eid=int(input("enter employee id :"))
    ename=input("enter employee name :")
    eadd=input("enter emplpoyee address :")
    eage=int(input("enter employee age :"))
    valuetuple=(eid,ename,eadd,eage)
    emp_list.append(valuetuple)
    i=i+1

Cursor.executemany(sql_quary,emp_list)
Connection.commit()

