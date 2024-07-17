import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='root')
if conn.is_connected():
    print('Connected to mysql db')
else:
    print('Not connected to mysql db')

cursor = conn.cursor()
cursor.execute('select * from emp')
'''row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()
'''
rows = cursor.fetchall()
print(cursor.rowcount)

for row in rows:
    print('Details', row)

cursor.close()

cursor = conn.cursor()
try:
    cursor.execute("insert into emp values(3,'Ben',30000)")
    conn.commit()
    print('Record inserted')
except:
    conn.rollback()

cursor.close()
conn.close()