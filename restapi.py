import flask 
from flask import jsonify
from flask import request 

from sql import create_connection
from sql import execute_read_query
from sql import execute_query

import creds

#setting up an application name
app = flask.Flask(__name__)
app.config["DEBUG"] = True #allow to show errors in browser

#put some stuff in memory
fruits = [
    {'id': 0,
     'name': 'orange',
     'color': 'orange'
     },
     {'id': 1,
     'name': 'apple',
     'color': 'red'
     },
]

#default url without any routing as GET request
@app.route('/', methods=['GET'])
def home():
    return "<h1> WELCOME to API class</h1>"

# /////////////// API's for accessing Memory object fruits

#create endpoint to get all fruits
@app.route('/api/fruits/all', methods=['GET'])
def api_all_fruits():
    return jsonify (fruits)

#create a endpoint to get a single fruit : http://127.0.0.1:5000/api/fruits?id=1
@app.route('/api/fruits', methods=['GET'])
def api_id():
    if 'id' in request.args: #only if id is provided as an argument, proceed
        id = int(request.args['id'])
    else:
        return 'Error: No ID provided!'
    results = [] #resulting fruits to return
    for fruit in fruits:
        if fruit['id'] == id:
            results.append(fruit)
    return jsonify (results)

#add a fruit as POST method
@app.route('/api/fruits', methods=['POST'])
def api_add_fruit():
    request_data = request.get_json()
    newid = request_data['id']
    newname = request_data['name']
    newcolor = request_data['color']

    fruits.append({'id':newid, 'name': newname, 'color': newcolor})
    return 'Add request successful!'

#delete a fruit as DELETE method
@app.route('/api/fruits', methods=['DELETE'])
def api_delete_fruit():
    request_data = request.get_json()
    idtodelete = request_data['id']
    
    for i in range(len(fruits)-1, -1, -1): #start, stop, step size
        if fruits[i]['id'] == idtodelete:
            del(fruits[i])
        
    return "Delete request successful!"

# ///////////// API's for DATABASE access ///////////////
#     
#create a endpoint to get a single user from DB : http://127.0.0.1:5000/api/users?id=1
@app.route('/api/users', methods=['GET'])
def api_users_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No ID is provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase)
    sql ="select * from users"
    users = execute_read_query(conn, sql)
    results = []
    for user in users:
        if user['id']== id:
            results.append(user)
    return jsonify(results)

#get all users 
@app.route('/api/users/all', methods=['GET'])
def api_users_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase)
    sql ="select * from users"
    users = execute_read_query(conn, sql)
    return jsonify(users)

#add a user as POST method
@app.route('/api/users', methods=['POST'])
def api_add_users():
    request_data = request.get_json()
    newfname = request_data['firstname']
    newlname = request_data['lastname']
    newemail = request_data['email']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase)
    sql = "insert into users(firstname, lastname, email) values ('%s','%s','%s')" % (newfname, newlname, newemail)

    execute_query(conn, sql)
    return 'Add user request successful!'

# Delete a user with DELETE method
@app.route('/api/users', methods=['DELETE'])
def api_delete_user_byID():
    request_data = request.get_json()
    idtodelete = request_data['id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase)
    sql = "delete from users where id = %s" % (idtodelete)
    execute_query(conn, sql)
        
    return "Delete request successful!"

app.run()
