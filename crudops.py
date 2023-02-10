import mysql.connector
import creds

from _mysql_connector import Error
from sql import create_con
from sql import execute_query
from sql import execute_read_query

#crreate connection to mysql database
myCreds = creds.Creds()
connection =create_con(myCreds.connectionstring, myCreds.username,myCreds.passwd,myCreds.dataBase)

#CRUD - Create, Read, Update and Delete

#create a new entry into use table 
# query ='insert into users(firstname, lastname, email) values('test','testlastname','test@uh.edu)'
#excute_query(connection,query)

#addtional options create new data
fname = 'abc'
lname = 'pqr'
myemail = 'xyz@uh.edu'


query ="insert into users(firstname,lastname,email) values('%s','%s', '%s')" % (fname,lname,myemail)
execute_query(connection, query)

#read all users data in users table
query ='select* from users'
users = execute_read_query(connection,query)

for users in users:
    print(user['fristname'],'', user['lastname'])

#update a user in user table
uid = 2
query ="update users set email='testlast@uh.edu' where id = %s"%(uid)

execute_query(connection,query)

#delete a user in user table 
uid =2
query ="delete from users where id = %s" % (uid)
execute_query(connection, query)

#addtional options with delete

