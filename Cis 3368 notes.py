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

conn = create_con('cis-3368-spring-2023.cvsqlbhm5w1r.us-east-2.rds.amazonaws.com','admin','admin2398','cis3368')
cursor = conn.cursor(dictionary = True)
sql = 'select * from users'
cursor.execute(sql)
rows = cursor.fetchall()
for user in rows:
    print(user)
    print('first name : ', user['firstname'])