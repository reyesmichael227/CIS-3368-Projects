# Michael Reyes 
# 2011032
# Smart Patel
# 1967227

import flask 
from flask import jsonify
from flask import request, make_response
import hashlib # creates the hash vaule for password 

from sql import create_connection #creating connection to mysql database
from sql import execute_read_query
from sql import execute_query

import creds #imports datbase creditinals to log in database

# setting up an application name
app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->

#login API
masterPassword = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # Hash value of Password 'password' 
masterUsername = 'username'

@app.route('/authenticatedroute', methods=['GET']) #Use this link to acess the login page http://127.0.0.1:5000/authenticatedroute
def auth_test():
    if request.authorization:
        encoded = request.authorization.password.encode() #unicode encoding
        hasedResult = hashlib.sha256(encoded) #hashing
        if request.authorization.username == masterUsername and hasedResult.hexdigest() == masterPassword:
            return '<h1> Authorized Access Granted </h1>'
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
#Endpoint APIs for Captain table
@app.route('/api/captain/all', methods=['GET']) # create endpoint to get all data from captain in database: http://127.0.0.1:5000/api/captain/all using this link will open webpage displaying all data
def api_captain_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) 
    sql ="select * from captain"
    captain = execute_read_query(conn, sql)
    return jsonify(captain)

#add a Enpoint for POST  to add JSON request to Captain table inside datbase can be tested using mysql
@app.route('/api/captain', methods=['POST']) # use this link on postman to establish api to database 
def api_add_captain():
    request_data = request.get_json()
    new_firstname = request_data['firstname']
    new_lastname = request_data['lastname']
    new_captainrank = request_data['captainrank']
    new_homeplanet = request_data['homeplanet']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "insert into captain (firstname, lastname, captainrank, homeplanet) values ('%s','%s','%s','%s')" % (new_firstname, new_lastname, new_captainrank, new_homeplanet)

    execute_query(conn, sql)
    return 'Add Captain request successful!'


# Delete data with DELETE method inside Captain table can be tested using mysql
@app.route('/api/captain', methods=['DELETE']) # use this link on postman to establish api to database 
def api_delete_captain_byID():
    request_data = request.get_json()
    Idtodelete = request_data['id']
    
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "delete from captain where id = %s" % (Idtodelete)
    execute_query(conn, sql)
        
    return "Delete Captain request successful!"


#use PUT method in captain table
@app.route('/api/captain', methods=['PUT'])#create endpoint to be able to update snowboard based on ID in database using this http: so api can be tested in postman
def api_update_captain(): # Defining the function
    request_data = request.get_json()
    Idtoupdate = request_data['id']
    update_firstname = request_data['firstname']
    update_lastname = request_data['lastname']
    update_captainrank = request_data['captainrank']
    update_homeplanet = request_data['homeplanet']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "update captain set firstname = '%s',lastname = '%s', captainrank = '%s', homeplanet = '%s' where id = %s" % (update_firstname, update_lastname, update_captainrank, update_homeplanet,Idtoupdate)
    execute_query(conn, sql)
        
    return 'Update Captain request Successful' # Once everything runs it prints a successful message

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# End point APIs spaceship tables

@app.route('/api/spaceship/all', methods=['GET']) # create endpoint to get all spaceships in database: http://127.0.0.1:5000/api/spaceship/all  using this link will open webpage displaying all dat
def api_spaceship_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) #creates
    sql ="select * from spaceship"
    captain = execute_read_query(conn, sql)
    return jsonify(captain)


@app.route('/api/spaceship', methods=['POST']) # use this link on postman to establish api to database 
def api_add_spaceship():
    request_data = request.get_json()
    new_maxweight = request_data['maxweight']
    new_captainid= request_data['captainid']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "insert into spaceship (maxweight, captainid) values ('%s', %s)" % (new_maxweight, new_captainid)

    execute_query(conn, sql)
    return 'Add Spaceship request successful!'


# Delete a data with DELETE method inside spaceship table can be tested using mysql
@app.route('/api/spaceship', methods=['DELETE']) # use this link on postman to establish api to database 
def api_delete_spaceship_ID():
    request_data = request.get_json()
    Idtodeletespacehsip = request_data['id']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "delete from Spaceship where id = %s" % (Idtodeletespacehsip)
    execute_query(conn, sql)
        
    return "Delete spaceship request successful!"


#use PUT method in spaceship table 
@app.route('/api/spaceship', methods=['PUT'])#create endpoint to be able to update spaceship based on ID in database using this http:  so api can be tested in postman
def api_update_spaceship(): # Defining the function
    request_data = request.get_json()
    Idtoupdatespaceship = request_data['id']
    update_maxweight = request_data['maxweight']
    update_captainid= request_data['captainid']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "update spaceship set maxweight = '%s',captainid = %s, where id = %s" % (update_maxweight, update_captainid, Idtoupdatespaceship )
    execute_query(conn, sql)
        
    return 'Update Spaceship request Successful' # Once everything runs it prints a successful message

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Endpoint APIs for cargo table
@app.route('/api/cargo/all', methods=['GET']) # create endpoint to get all cargo in database: http://127.0.0.1:5000/api/cargo/all  using this link will open webpage displaying all data
def api_cargo_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) #creates
    sql ="select * from cargo"
    captain = execute_read_query(conn, sql)
    return jsonify(captain)


@app.route('/api/cargo', methods=['POST']) 
def api_add_cargo():
    request_data = request.get_json()
    new_weight = request_data['weight']
    new_cargotype = request_data['cargotype']
    new_departure = request_data['departure']
    new_arrival = request_data['arrival']
    new_shipid = request_data['shipid']

    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "insert into  cargo  (weight, cargotype, departure, arrival, shipid) values (%s, '%s', %s, %s, %s)" % (new_weight, new_cargotype, new_departure, new_arrival, new_shipid)

    execute_query(conn, sql)
    return 'Add Cargo request successful!'


# Delete a cargo data with DELETE method inside database can be tested using mysql
@app.route('/api/cargo', methods=['DELETE']) 
def api_delete_cargo_byID():
    request_data = request.get_json()
    Idtodeletecargo = request_data['id']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = "delete from cargo where id = %s" % (Idtodeletecargo)
    execute_query(conn, sql)
        
    return "Delete Cargo request successful!"


#use PUT method in cargo table within database
@app.route('/api/cargo', methods=['PUT'])
def api_update_cargo(): # Defining the function
    request_data = request.get_json()
    Idtoupdatecargo = request_data['id']
    update_weight = request_data['weight']
    update_cargotype = request_data['cargotype']
    update_departure = request_data['departure']
    update_arrival = request_data['arrival']
    update_shipid = request_data['shipid']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase) # establish connection to database 
    sql = " update cargo set weight = %s, cargotype = '%s' , departure = %s, arrival = %s, shipid = %s" % (update_weight, update_cargotype, update_departure, update_arrival, update_shipid, Idtoupdatecargo)
    execute_query(conn, sql)
        
    return 'Update Cargo request Successful' # Once everything runs it prints a successful message


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
