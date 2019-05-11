from bottle import run, request, post, get
import string
import requests
import sys
import json
# Important globals
host = "localhost"
port = "8082"
database = "8083"

log_file = "apilog.txt"
# Debug mode to check whether or not attacks are working
# Start with it as "True", try the attack, flip it to false, try the attack again and see if your WAF blocked it
# Debug should be set to false when launching the final version

def log(from_port, function_name, input, output):
    f = open(log_file, "a")
    f.write("From_port: %s\n" % from_port)
    f.write("Function_name: %s\n" % function_name)
    f.write("Input: %s\n" % input)
    f.write("Output: %s\n" % output)
    f.write("\n")
    f.close()
    return "logged"

def decode(string):
    string = string.content.decode()
    return string

@post('/api/setup/<port:path>')
def setup(port):
    output = requests.post(db_url + '/db/setup')
    print(output.content)
    output = decode(output)

    log(port, "setup", "None", output)
    return output

@post('/api/add_user/<port:path>/<username:path>/<password:path>')
def add_user(port, username, password):
    output = requests.post(db_url + '/db/add_user/' + username + '/' + password)
    output = decode(output)

    log(port, "add_user", username + ', ' + password, output)
    return output

@post('/api/check_credentials/<port:path>/<username:path>/<password:path>')
def check_credentials(port, username, password):
    output = requests.post(db_url + '/db/check_credentials/' + username + '/' + password)
    output = decode(output)

    log(port, "check_credentials", username + ', ' + password, output)
    return output

@post('/api/insert_message/<port:path>/<username:path>/<recipientname:path>/<massage_content:path>')
def insert_message(port, username, recipientname, massage_content):
    output = requests.post(db_url + '/db/insert_message/' + username + '/' + recipientname + '/' + massage_content)
    output = decode(output)

    log(port, "insert_message", username + ', ' + recipientname + ',' + massage_content, output)
    return output

@post('/api/get_all_message/<port:path>/<username:path>')
def get_all_message(port, username):
    output = requests.post(db_url + '/db/get_all_message/' + username)
    data = json.loads(output.content)
    #print(output)
    #print(output.json())
    #output = json.loads(output)

    log(port, "get_all_message", username, data)
    #a = []
    return output.content

@post('/api/get_allmessages/<port:path>')
def get_allmessages(port):
    output = requests.post(db_url + '/db/get_allmessages')
    data = json.loads(output.content)
    #output = decode(output)

    log(port, "get_allmessages", "Admin", data)
    #a = []
    return output.content

@post('/api/ban/<port:path>/<username:path>')
def ban(port, username):
    output = requests.post(db_url + '/db/ban/' + username)
    output = decode(output)

    log(port, "ban", username, output)
    #a = []
    return output

@post('/api/lift/<port:path>/<username:path>')
def lift(port, username):
    output = requests.post(db_url + '/db/lift/' + username)
    output = decode(output)

    log(port, "lift", username, output)
    #a = []
    return output

@post('/api/check_muted/<port:path>/<username:path>')
def check_muted(port, username):
    output = requests.post(db_url + '/db/check_muted/' + username)
    output = decode(output)

    log(port, "check_muted", username, output)
    #a = []
    return output


if len(sys.argv) == 5:
    host = sys.argv[1]
    port = sys.argv[2]
    database = sys.argv[3]
    log_file = sys.argv[4]

db_url = 'http://' + host + ':' + database
# Run the server
run(host=host, port=port)
