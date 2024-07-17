import mysql.connector

def start_connection():
    try:
        conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='root')
        if conn.is_connected():
            print('Connection is successful')
        else:
            print('Connection is not established')
    except:
        exit()

    return conn

def close_connection(connection):
    connection.close()

def show(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('select * from emp')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except:
        exit()
    finally:
        cursor.close()
        conn.close()

def insert(conn,id,name,salary):
    str = "insert into emp (id, name, sal) values(%d, '%s', %d)"
    args = (id,name,salary)
    try:
        cursor = conn.cursor()
        cursor.execute(str % args)
        conn.commit()
        print('Data inserted')
    except:
        print('Data not inserted')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def delete(conn,id):
    str = "delete from emp where id=%d"
    args = (id)
    try:
        cursor = conn.cursor()
        cursor.execute(str % args)
        conn.commit()
        print('Data deleted')
    except:
        print('Data not deleted')
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

conn = start_connection()
show(conn)

emp_id = int(input('Enter the employee id want to insert'))
emp_name = input('Enter the employee name want to insert')
emp_salary = int(input('Enter the employee salary want to insert'))
conn = start_connection()

insert(conn,emp_id,emp_name,emp_salary)

conn = start_connection()
show(conn)

conn = start_connection()
id = int(input('Which emp id details want to delete'))
delete(conn,id)

conn = start_connection()
show(conn)


