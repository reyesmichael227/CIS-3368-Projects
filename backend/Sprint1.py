# Michael Reyes 
# 2011032
# Smart Patel
# 1967227
import flask
from flask import jsonify, request, redirect
from sql import create_connection
from sql import execute_read_query
from sql import execute_query
import creds

# setting up application
app = flask.Flask(__name__)
app.config['DEBUG'] = True # allow to show error in browser


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Endpoint APIs for Captain table

@app.route('/api/captain', methods=['GET'])# create endpoint to get all data from captain in database: http://127.0.0.1:5000/api/captain/all using this link will open webpage displaying all data
def get_all_captain():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "select * from captain"
    captains = execute_read_query(conn, sql)
    return jsonify(captains)

#add a Enpoint for POST  to add JSON request to Captain table inside datbase can be tested using mysql
@app.route('/api/captain/post', methods=['POST'])# use this link on postman to establish api to database 
def add_captain():
    request_data = request.get_json()
    new_firstname= request_data['firstname']
    new_lastname = request_data['lastname']
    new_captainrank = request_data['captainrank']
    new_homeplanet = request_data['homeplanet']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName) # establish connection to database
    sql = "insert into captain (firstname, lastname, captainrank, homeplanet) values ('%s','%s','%s','%s')" % (new_firstname,new_lastname,new_captainrank,new_homeplanet)
    execute_query(conn, sql)
    return 'Add new captain successful.'

# endpoint to delete a captain by id using DELETE method
@app.route('/api/captain/delete', methods=['DELETE'])
def delete_captain():
    request_data = request.get_json()
    idToDelete = request_data['id']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "delete from captain where id = %s" % (idToDelete)
    execute_query(conn, sql)
    return 'Delete captain successful.'

# endpoint to update a captain record using PUT method
@app.route('/api/captain/put', methods=['PUT'])
def update_captain():
    request_data = request.get_json()
    idToUpdate = request_data['id']
    update_firstname = request_data['firstname']
    update_lastname = request_data['lastname']
    update_captainrank = request_data['captainrank']
    update_homeplanet = request_data['homeplanet']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "update captain set firstname = '%s', lastname = '%s', captainrank = '%s', homeplanet = '%s' where id = %s" % (update_firstname, update_lastname,  update_captainrank, update_homeplanet, idToUpdate)
    execute_query(conn, sql)
    return 'Update captain successful.'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# routes for CRUD operations on spaceship table
# endpoint to retrieve all spaceship record using GET method
@app.route('/api/spaceship', methods=['GET'])
def get_all_spaceships():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "select * from spaceship"
    spaceships = execute_read_query(conn, sql)
    return jsonify(spaceships)

#endpoint to add a spaceship using POST method
@app.route('/api/spaceship/post', methods=['POST'])
def add_spaceship():
    request_data = request.get_json()
    new_maxweight = request_data['maxweight']
    new_captainid = request_data['captainid']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "insert into spaceship (maxweight, captainid) VALUES (%s, %s)" % (new_maxweight, new_captainid)
    execute_query(conn, sql)
    return 'Add spaceship successful.'

# endpoint to delete a spaceship by id using DELETE method
@app.route('/api/spaceship/delete', methods=['DELETE'])
def delete_spaceship():
    request_data = request.get_json()
    idToDelete = request_data['id']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "delete from spaceship where id = %s" % (idToDelete)
    execute_query(conn, sql)
    return 'Delete spaceship successful.'


# endpoint to update a spaceship by id using PUT method
@app.route('/api/spaceship/put', methods=['PUT'])
def update_spaceship():
    request_data = request.get_json()
    Idtoupdatespaceship = request_data['id']
    update_maxweight = request_data['maxweight']
    update_captainid = request_data['captainid']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "update spaceship set maxweight = %s, captainid = %s WHERE id = %s" % (update_maxweight, update_captainid, Idtoupdatespaceship)
    execute_query(conn, sql)
    return 'Update spaceship successful.'

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoint APIs for cargo table
@app.route('/api/cargo', methods=['GET']) # create endpoint to get all cargo in database: http://127.0.0.1:5000/api/cargo/all  using this link will open webpage displaying all data
def get_current_cargo():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)# establish connection to database 
    sql = "select * from cargo where arrival is null or arrival = '0000-00-00';" #edited post sprint 1
    current_cargo = execute_read_query(conn, sql)
    return jsonify(current_cargo)



@app.route('/api/cargo/post', methods=['POST'])
def add_cargo():
    request_data = request.get_json()
    new_weight = request_data['weight']
    new_cargotype = request_data['cargotype']
    new_departure = request_data['departure']
    new_arrival = request_data['arrival']
    new_shipid = request_data['shipid']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)# establish connection to database 
    sql = "insert into cargo (weight, cargotype, departure, arrival, shipid) VALUES (%s, '%s', '%s', '%s', %s)" % (new_weight, new_cargotype, new_departure, new_arrival, new_shipid)
    execute_query(conn, sql)
    return 'Add cargo successful.'
    
@app.route('/api/cargo/delete', methods=['DELETE'])
def delete_cargo():
    request_data = request.get_json()
    idToDelete = request_data['id']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "DELETE FROM cargo WHERE id = %s" % (idToDelete)
    execute_query(conn, sql)
    return 'Delete cargo successful.'

@app.route('/api/cargo/put', methods=['PUT'])
def update_cargo():
    request_data = request.get_json()
    idToUpdate = request_data['id']
    update_weight = request_data['weight']
    update_cargotype = request_data['cargotype']
    update_departure = request_data['departure']
    update_shipid = request_data['shipid']

    
    if 'arrival' in request_data and request_data['arrival']:
        update_arrival = request_data['arrival']
        sql = "UPDATE cargo SET weight = %s, cargotype = '%s', departure = '%s', arrival = '%s', shipid = %s WHERE id = %s" % (update_weight, update_cargotype, update_departure, update_arrival, update_shipid, idToUpdate)
    else:
        sql = "UPDATE cargo SET weight = %s, cargotype = '%s', departure = '%s', shipid = %s WHERE id = %s" % (update_weight, update_cargotype, update_departure, update_shipid, idToUpdate)

    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    execute_query(conn, sql)
    return 'Update cargo successful.'  

app.run()

# Refrences
# I had a meeting with professor Suresh Kumar Peddoju  who explained the code 
# used secruity.api provide in CIS3368 for lines 27-37
# https://www.w3schools.com/sql/sql_dates.asp used this to understand date data type
# https://www.w3schools.com/sql/sql_foreignkey.asp used this to create FOREIGN KEYS in SQL workbench 
# https://www.w3schools.com/sql/sql_primarykey.asp used this to create Primary KEYS in SQL workbench
# https://www.geeksforgeeks.org/hashlib-module-in-python/ this link taught me hashlib  function
# https://developers.liveperson.com/login-service-api-overview.html used this to understand what is and how to create a simple log in api
# https://www.youtube.com/watch?v=xLbmcMVtfKE used this video to push code on github 
