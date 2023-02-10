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

def execute_query(conn,query):
    cursor = conn.cursor()
    try:
        cursor.excute(query)
        conn.commit()
        print('Query excuted successfully')
    except Error as e:
            print('Error occured is',e)

def execute_read_query(conn,query):
     cursor =conn.cursor(dictionary = True)
     rows = None
     try:
          cursor.excute(query)
          rows = cursor.fecthall()
          return rows
     except Error as e:
          print('Error occured is : ', e)

            
        
