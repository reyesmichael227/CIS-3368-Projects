import hashlib
import datetime
import time
import flask
from flask import jsonify
from flask import request, make_response

# 5316911983139663491615228241121400000 GUID/UUID
# 80658175170943878571660636856403766975289505440883277824000000000000   52!
# 115792089237316195423570985008687907853269984665640564039457584007913129639936  SHA256, 2^256

# Setting up an application name
app = flask.Flask(__name__) # Sets up the application
app.config["DEBUG"] = True # Allow to show errors in browser


masterPassword = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # Hash value of Password 'password' 
masterUsername = 'username'

validTokens = {
    "100", "200", "300", "400"
}

# basic http authentication, prompts username and password upon contacting the endpoint

# 'password' as plaintext should not be used to verify authorization to access. 
# the password should be hashed and the hash should be compared to the stored password hash in the database
@app.route('/authenticatedroute', methods=['GET'])
def auth_test():
    if request.authorization:
        encoded = request.authorization.password.encode() #unicode encoding
        hasedResult = hashlib.sha256(encoded) #hashing
        if request.authorization.username == masterUsername and hasedResult.hexdigest() == masterPassword:
            return '<h1> Authorized user access </h1>'
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

# token submission as part of the url, similar to how personal tokens (OTP) were part of SMS code
@app.route('/api/token/<sometoken>', methods=['GET'])
def auth_token(sometoken):
    for eachvalidtoken in validTokens:
        if eachvalidtoken == sometoken: #check if token is valid, ideally compare against a set of valid tokens in a database table
            return '<h1> Authentication successful ! </h1>'
    return 'INVALID ACCESS TOKEN !'

# token submission that has expiration date and authorization is given only if token is not expired yet

# for instance, time token valid until Jan 1 2030 (still valid): 1893456000
# for instance, time token valid until Jan 1 2022 (no longer valid): 1640995200
# we can create time ticks easily with:
# date = datetime.datetime(2022, 1, 1)
# dateInSeconds = date.timestamp() #returns time in seconds since Jan 1 1970
@app.route('/api/timetoken/<sometimetoken>', methods=['GET'])
def auth_timetoken(sometimetoken):
    if float(sometimetoken) > time.time():
        return '<h1> Time Token still valid </h1>'
    return 'Time Token expired !'

# route to authenticate with username and password against a dataset (ideally from database and also hashed, not clear strings for passwords)
# test in postman by creating header parameters 'username' and 'password' and pass in credentials

authorizedusers = [
    {
        #default user
        'username': 'username',
        'password': 'password',
        'role': 'default',
        'token': '0',
        'admininfo': None
    },
    {
        #Admin user
        'username': 'suresh',
        'password': 'admin',
        'role': 'admin',
        'token': '123456',
        'admininfo': 'This is admin user info'
    }
]

@app.route('/api/userpwdroute', methods=['GET'])
def auth_userpwd():
    username = request.headers['username'] #get the header parameters.
    passwd = request.headers['password']

    for authuser in authorizedusers:
        if authuser['username'] == username and authuser['password'] == passwd :  #if authorized user found
            sessiontoken = authuser['token']
            admininfo = authuser['admininfo']
            role = authuser['role']
            results = []
            results.append(sessiontoken)
            results.append(admininfo)
            results.append(role)
            return jsonify(results)
    return 'Something went wrong!!'



app.run()