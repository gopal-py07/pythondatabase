from mysql.connector import connect
Conection=connect(host='localhost',user='root',password='root',charset='utf8',db='python')
#creating cursor obj
Cursor=Conection.cursor()
print(Cursor)
sql_select_quary='select * from employee'
#print(sql_select_quary)#take it as string
Cursor.execute(sql_select_quary)
#for fetching data we use fetchall()
record=Cursor.fetchall()
#print(record) data is in list format==>> [(101, 'gopAL', 'vilegaon', 25), (101, 'gopAL', 'vilegaon', 25), (102, 'parth', 'karanja', 12), (103, 'smarth', 'karanja', 8)]

for value in record:
    #print(value)
    print('emp_id :',value[0])
    print('emp_name :',value[1])
    print('emp_add :',value[2])
    print('emp_age :',value[3])
