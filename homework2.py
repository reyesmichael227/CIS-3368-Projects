# Michael Reyes 
# PSID: 2011032
import flask 
from flask import jsonify
from flask import request

from sql import create_connection #creating connection to mysql database
from sql import execute_read_query
from sql import execute_query

import creds #imports datbase creditinals to log in database

#setting up an application name
app = flask.Flask(__name__)
app.config["DEBUG"] = True #allow to show errors in browser

# Enter readable data to be used in GET request in local memorey
snowboard =[
    {'Id':1,
     'Boardtype':'Freestyle',
     'Brand':'Slash Happy Place ',
     'MSRP':'399',
     'Size':'141'}
]
#default url without any routing as GET request 
@app.route('/', methods=['GET'])
def home():
    return "<h1> WELCOME to API class</h1>"

#create endpoint to get all snowboards in local memory: http://127.0.0.1:5000/api/snowboard/all using this link will open webpage displaying all data
@app.route('/api/snowboard/all', methods=['GET'])
def api_all_snowboards():
    return jsonify (snowboard)
#create a endpoint to get a single snowboard: 
def api_id():
    if 'id' in request.args: #only if id is provided as an argument, proceed
        id = int(request.args['id'])
    else:
        return 'Error: No ID provided!'
    results = [] #resulting snowboards to return
    for snowboards in snowboard:
        if snowboards['id'] == id:
            results.append(snowboards)
    return jsonify (results)

#create endpoint to connect it to database on mysql
@app.route('/api/DB/snowboard/all', methods=['GET']) # create endpoint to get all snowboards in database: http://127.0.0.1:5000/api/DB/snowboard/all sing this link will open webpage displaying all data
def api_snowboard_allDB():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) #creates
    sql ="select * from snowboard"
    snowboard = execute_read_query(conn, sql)
    return jsonify(snowboard)

#add a snowboard as POST method local memory
@app.route('/api/snowboard', methods=['POST']) #create endpoint to be able to add another snowboard in database using this http: http://127.0.0.1:5000/api/snowboard so api can be tested in postman
def api_add_snowboard():
    request_data = request.get_json()
    newId = request_data['Id']
    newBoardtype = request_data['Boardtype']
    newBrand = request_data['Brand']
    newMSRP = request_data['MSRP']
    newSize = request_data['Size']

    snowboard.append({'Id':newId, 'Boardtype': newBoardtype, 'Brand': newBrand, 'MSRP':newMSRP, 'Size':newSize})
    return 'Add request successful!'

#add a snowboard as POST method in datbase can be tested using mysql
@app.route('/api/DB/snowboard', methods=['POST']) # use this link on postman to establish api to database http://127.0.0.1:5000/api/DB/snowboard
def api_add_snowboardDB():
    request_data = request.get_json()
    newBoardtype = request_data['Boardtype']
    newBrand = request_data['Brand']
    newMSRP = request_data['MSRP']
    newSize = request_data['Size']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "insert into snowboard (Boardtype, Brand, MSRP, Size) values ('%s','%s',%s,%s)" % (newBoardtype, newBrand, newMSRP, newSize)

    execute_query(conn, sql)
    return 'Add user request successful!'

#delete a snowboard as DELETE method in local memory
@app.route('/api/snowboard', methods=['DELETE']) #create endpoint to be able to delete snowboard based on ID in database using this http: http://127.0.0.1:5000/api/snowboard so api can be tested in postman
def api_delete_snowboard():
    request_data = request.get_json()
    Idtodelete = request_data['Id']
    
    for i in range(len(snowboard)-1, -1, -1): #start, stop, step size
        if snowboard[i]['Id'] == Idtodelete:
            del(snowboard[i])
        
    return "Delete request successful!"

# Delete a user with DELETE method inside database can be tested using mysql
@app.route('/api/DB/snowboard', methods=['DELETE']) # use this link on postman to establish api to database http://127.0.0.1:5000/api/DB/snowboard
def api_delete_snowboard_byIDDB():
    request_data = request.get_json()
    Idtodelete = request_data['Id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "delete from snowboard where Id = %s" % (Idtodelete)
    execute_query(conn, sql)
        
    return "Delete request successful!"


#use PUT method in snowboard database
@app.route('/api/DB/snowboard', methods=['PUT'])#create endpoint to be able to update snowboard based on ID in database using this http: http://127.0.0.1:5000/api/snowboard so api can be tested in postman
def api_update_snowboardDB(): # Defining the function
    request_data = request.get_json()
    Idtoupdate = request_data['Id']
    updateBoardtype = request_data['Boardtype']
    updateBrand = request_data['Brand']
    updateMSRP = request_data['MSRP']
    updateSize = request_data['Size']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "update snowboard set Boardtype = '%s',Brand = '%s', MSRP = %s, Size = %s where Id = %s" % (updateBoardtype,updateBrand,updateMSRP,updateSize,Idtoupdate)
    execute_query(conn, sql)
        
    return 'Update request Successful' # Once everything runs it prints a successful message
    

app.run()

# refrences
# Had a teams meeting with professor and he explained the code for PUT method and fixing other code
# code provide by professor Suresh Kumar Peddoju via blackboard and in class
# https://www.tutorialspoint.com/how-to-create-a-put-request-in-postman provide information for PUT method
# https://www.geeksforgeeks.org/put-method-python-requests/
# https://www.w3schools.com/tags/ref_httpmethods.asp#:~:text=The%20PUT%20Method,always%20produce%20the%20same%20result.
# https://stackoverflow.com/questions/630453/what-is-the-difference-between-post-and-put-in-http provide information for PUT method
# https://www.tutorialspoint.com/postman/postman_delete_requests.htm#:~:text=Postman%20DELETE%20request%20deletes%20a,updating%20data%20on%20the%20server.

