from bottle import route, get, post, request, response

import hashlib

import random
import json
import sys
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
import time
import requests




#database.database_setup()

print("!!! ")
api_url = 'http://localhost:8082/api/'


# Initialise our views, all arguments are defaults
page_view = view.View()
port = sys.argv[2]
if len(sys.argv) == 8:
    port = sys.argv[2]
    api_host = sys.argv[5]
    api_port = sys.argv[6]
    api_url = 'http://' + api_host + ':' + api_port + '/api/'
    page_view.template_path = sys.argv[7]

for _ in range(10):
    try:
        a = requests.post(api_url + 'setup/' + port)
        break
    except:
        time.sleep(1)
print(a.content.decode())

def check_cookie():

    h = hashlib.md5()
    s = 'yinggaishiyan'

    try:
        print("ac")
        username = request.get_cookie("username")
        hashvalue = request.get_cookie("hashvalue")
        hasloginvalue = request.get_cookie("logged_in")
        print("accc")
        hashinput = username + s + hasloginvalue
        print (hashinput)
        if hashinput is None:
            return "False"
        h.update(hashinput.encode('utf-8'))
        print(h.hexdigest())
        if hashvalue == h.hexdigest():
            return "True"
        else:
            return "False"
    except:
        return "True"
    return "False"

def checkheader():
    print("start")
    try:

        hasloginvalue = request.get_cookie("logged_in")
        print("value", hasloginvalue)
        if "True" == hasloginvalue:
            haslogin = True
            if request.get_cookie("username") == "adminnewnameaaa":
                print(request.get_cookie("username"))
                isadmin = True
            else:
                print("fail",request.get_cookie("username"))
                isadmin = False
        else:
            haslogin = False
    except:
        print("except")
        haslogin = False
    if haslogin:
        if isadmin:
            return "headeradmin"
        else:
            return "headerloggedin"

    else:
        return "header"

def register_page():
    return page_view("register")


def error_page(err_str):
    if check_cookie() == "False":
        return page_view("invalid", "header", reason=err_str)
    return page_view("invalid", checkheader(), reason=err_str)
#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index_page():
    try:
        request.get_cookie("username")
        print("aha")
        haslogin = request.get_cookie("logged_in")
    except:
        print("haa")
        haslogin = "False"

    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")

    if haslogin == "True":
        #print(theuser.logged_in)
        return page_view("index", checkheader())
    else:
        #print(theuser.logged_in)
        return page_view("index", checkheader())

#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def login_page():
    return page_view("login")

#-----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    print(username, password)
    a = requests.post(api_url + 'check_credentials/'+ port + '/' + username + '/' + password)

    #if database.check_credentials(username, password):
    if a.content.decode() == "Valid username and password":
        login = True
    else:
        login = False
        err_str = "Incorrect Username or Password"

    #if username != "admin": # Wrong Username
    #    err_str = "Incorrect Username"
    #    login = False

    #if password != "password": # Wrong password
    #    err_str = "Incorrect Password"
    #    login = False

    if login:
        response.set_cookie("username", username, path="/")
        response.set_cookie("logged_in", "True", path="/")
        h2 = hashlib.md5()
        s = 'yinggaishiyan'
        hashinput = username + s + "True"
        h2.update(hashinput.encode('utf-8'))
        response.set_cookie("hashvalue", h2.hexdigest(), path="/")
        time.sleep(1)
        #print(request.getcookie("logged_in"))
        r = request.get_cookie("logged_in")
        print("the new cookie is", r)
        if username == "admin":

            return page_view("index", "headerloggedin")
        else:

            return page_view("index", "headerloggedin")
    else:
        return page_view("invalid", checkheader(), reason=err_str)



def create_account(username, password):

    r = requests.post(api_url + 'add_user/' + port + '/' + username + '/' + password)
    r = r.content.decode()
    if r != "The user is added":
        return page_view("invalid", "header", reason="Please use another username")
    return login_page()




def insert_message(recipientname, massage_content):

    massage_content=massage_content.replace("<","< ")

    requests.post(api_url + 'insert_message/' + port + '/' + request.get_cookie("username") + '/' + recipientname + '/' + massage_content)
    #database.insert_message(request.get_cookie("username"), recipientname, massage_content)


    return send_message()

#-----------------------------------------------------------------------------
# About
#-----------------------------------------------------------------------------

def about_page():
    return page_view("about", garble=about_garble())

def send_message():

    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")

    a = requests.post(api_url + 'check_muted/' + port + '/' + request.get_cookie("username"))
    #if database.check_muted(request.get_cookie("username")):
    if a.content.decode() == 'True':
        return page_view("sendmessage", checkheader())
    else:
        return page_view("invalid", checkheader(), reason="You have been banned")
        #return page_view("index", checkheader())

def message_box():

    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")

    data = requests.post(api_url + 'get_all_message/' + port + '/' + request.get_cookie("username"))
    data = json.loads(data.content)
    #data = database.get_all_message(request.get_cookie("username"))
    print(data)
    #return page_view("sendmessage", "headerloggedin")
    return page_view.with_table( "messagebox", checkheader(), "tailer", data)
    #return page_view("messagebox")

def allmessages():

    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")

    data = requests.post(api_url + 'get_allmessages/' + port)
    data = json.loads(data.content)
    #data = database.get_allmessages()

    return page_view.with_table( "allmessages", checkheader(), "tailer", data)

def banuser():

    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")

    return page_view("banuser", checkheader())

def ban(username):
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    requests.post(api_url + 'ban/' + port + '/' + username)

    #database.ban(username)
    return page_view("banuser", checkheader())

def lift(username):
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    requests.post(api_url + 'lift/' + port + '/' + username)
    #database.lift(username)
    return page_view("banuser", checkheader())


def logout():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")

    response.set_cookie("logged_in", "False", path="/")

    h = hashlib.md5()
    s = 'yinggaishiyan'
    username = request.get_cookie("username")
    hashinput = username + s + "False"
    h.update(hashinput.encode('utf-8'))
    response.set_cookie("hashvalue", h.hexdigest(), path="/")

    time.sleep(1)
    return page_view("index", "header")



def profile():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view.profile(request.get_cookie("username"),checkheader())


def frontend():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("Front-end", checkheader())

def backend():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("Back-end", checkheader())

def thedatabase():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("Database", checkheader())

def html_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("HTML-int", checkheader())

def html_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("HTML-tut", checkheader())

def css_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("CSS-int", checkheader())

def css_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("CSS-tut", checkheader())

def js_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("JS-int", checkheader())

def js_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("JS-tut", checkheader())

def php_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("PHP-int", checkheader())

def php_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("PHP-tut", checkheader())

def pb_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("PB-int", checkheader())

def pb_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("PB-tut", checkheader())

def sql_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("SQL-int", checkheader())

def sql_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("SQL-tut", checkheader())

def sqlite_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("SQLite-int", checkheader())

def sqlite_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("SQLite-tut", checkheader())

def mysql_int():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("Mysql-int", checkheader())

def mysql_tut():
    if check_cookie() == "False":
        return page_view("invalid", "header", reason="stop attacking our website")
    return page_view("Mysql-tut", checkheader())







# Returns a random string each time
def about_garble():
    garble = ["leverage agile frameworks to provide a robust synopsis for high level overviews.",
    "iterate approaches to corporate strategy and foster collaborative thinking to further the overall value proposition.",
    "organically grow the holistic world view of disruptive innovation via workplace diversity and empowerment.",
    "bring to the table win-win survival strategies to ensure proactive domination.",
    "ensure the end of the day advancement, a new normal that has evolved from generation X and is on the runway heading towards a streamlined cloud solution.",
    "provide user generated content in real-time will have multiple touchpoints for offshoring."]
    return garble[random.randint(0, len(garble) - 1)]

#-----------------------------------------------------------------------------
