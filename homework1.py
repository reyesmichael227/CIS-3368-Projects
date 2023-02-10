# Michael Reyes 
# PSID: 2011032
import mysql.connector
from mysql.connector import Error
#uses mysql.connector import to start establishing connecting between vscode and mysql
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
# provides the username, password, database name, and host link, the databse uses was the AWS learner lab
cursor = conn.cursor()
# fully establish vs code and mysql connection

# main menu function
def displayMainMenu():
    print(' Main MENU ')
    print('(a) Add cases')
    print('(o) Output all cases in console')
    print('(q) Quit')

  
displayMainMenu()
option = input('Please enter an option')
# interactive menu with queries
while option != 'q':
    if option == 'a':
        countryname = input('Enter Country name:' )
        years = int(input('Enter year: '))
        totalcases = int(input('Enter total amount of cases: '))
        deaths = int(input('Enter total amount of deaths: '))
        recovered =int(input('Enter total amount of recovered: '))
        sql = 'INSERT INTO covidcases (countryname, year,totalcases,deaths,recovered)'
        val = (countryname, years, totalcases, deaths, recovered)
        cursor.execute(sql,val)
        conn.commit()
        print(' — — — SUCCESS — — — \n')
        exit()
        rows = cursor.fetchall()
        # inserts and updates table
    elif option =='o':
         sql = 'select * from covidcases'
         cursor.execute(sql)
         rows = cursor.fetchall()
         print(rows)
         exit()
         #displays all cases inside the covid cases table
    elif option =='q':
         print('You haved exited the program')
         exit() 
        # gives the user the ability to exit the program   
    else:
        print('Invaild option')
    # present error and exits


displayMainMenu()
option = input('Please enter an option')

# References
# Code in lines 3 -21 where copied off the lecture notes and more information was found via these websites 
# Lecture video: https://uofh.sharepoint.com/sites/Section_H_20231_CIS_3368_25450/_layouts/15/stream.aspx?id=%2Fsites%2FSection%5FH%5F20231%5FCIS%5F3368%5F25450%2FShared%20Documents%2FGeneral%2FRecordings%2FView%20Only%2FGeneral%2D20230201%5F165207%2DMeeting%20Recording%2Emp4&referrer=OfficeHome&referrerScenario=EDGEWORTH
# Website 1: https://dev.mysql.com/doc/connector-python/en/
# Website 2: https://www.w3schools.com/python/python_mysql_getstarted.asp
# This youtube video provide the basics for the python menu implementation
# Youtube video: https://www.youtube.com/watch?v=63nw00JqHo0
# This youtube video below shows how to use sql code in menu using pyhton 
# Youtube video: https://www.youtube.com/watch?v=DxTJ8l3CMMk 
