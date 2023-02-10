import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, pwd,dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = pwd,
            database = dbname
        )
        print("success")
    except Error as e:
        print("the error occured at : ", e)
    return connection

conn = create_con('cis3368spring.cjmfjeja717r.us-east-1.rds.amazonaws.com','admin','Admin2398','cis3368springdb')
cursor = conn.cursor(dictionary = True)
sql = 'select * from users'
cursor.execute(sql)
rows = cursor.fetchall()
for user in rows:
    print(user)
    print('first name : ', user['firstname'])