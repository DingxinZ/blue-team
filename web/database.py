from bottle import run, request, post, get
import sqlite3

import string
import json
import sys
# Important globals
host = "localhost"
port = "8083"
database="database.db"

# Debug mode to check whether or not attacks are working
# Start with it as "True", try the attack, flip it to false, try the attack again and see if your WAF blocked it
# Debug should be set to false when launching the final version
#ebug = False


def execute(sql_string):
    out = None
    for string in sql_string.split(";"):
        try:
            out = cur.execute(string)
        except:
            pass
    print('out:',out)
    return out

def commit():
    conn.commit()

def count_user():
    sql_cmd = """
            SELECT count(*)
            FROM Users;
        """
    cur.execute(sql_cmd)
    num_of_users = cur.fetchone()
    return num_of_users[0]

@post('/db/setup')
def database_setup():

    # Clear the database if needed
    execute("""DROP TABLE IF EXISTS Users;
    DROP TABLE IF EXISTS Messages
    """)
    commit()

    # Create the users table
    execute("""CREATE TABLE IF NOT EXISTS Users(
        Id INTEGER,
        username TEXT,
        password TEXT,
        admin INTEGER DEFAULT 0,
        Muted INTEGER DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS Messages(
    Sender TEXT,
    Recipient TEXT,
    Content TEXT,
    SendDate DATE
    )""")

    commit()
    #execute("""INSERT INTO Users
    #VALUES(1, "b","c", 0, 0)""")
    #commit()
    #execute("""SELECT * FROM Users""")
    #print("fetch:",cur.fetchone())
    # Add our admin user
    add_user('admin', 'admin', admin=1, muted=0)
    return "setup"


@post('/db/add_user/<username:path>/<password:path>')
def add_user(username, password, admin=0, muted = 0):
    a = count_user()
    sql_cmd = """
            INSERT INTO Users
            VALUES({id}, '{username}','{password}', {admin}, {muted})
        """.format(id = a, username=username, password=password, admin=admin, muted=muted)

    execute(sql_cmd)
    commit()
    print(sql_cmd)
    return "The user is added"

@post('/db/check_credentials/<username:path>/<password:path>')
def check_credentials(username, password):
    print(username, password)

    sql_query = """
            SELECT *
            FROM Users
            WHERE username = '{username}' AND password = '{password}'
        """.format(username=username, password=password)
    cur.execute(sql_query)
    # If our query returns

    if cur.fetchone():
        print('true')
        return "Valid username and password"
    else:
        print('false')
        return "Wrong username or password"

def getdate():
    sql_cmd = """
            SELECT datetime('now','+10 hours')
        """
    cur.execute(sql_cmd)
    currentdate = cur.fetchone()
    return currentdate[0]

@post('/db/insert_message/<username:path>/<recipientname:path>/<massage_content:path>')
def insert_message(username, recipientname, massage_content):
    currentdate = getdate()
    sql_cmd = """
            INSERT INTO Messages
             VALUES('{sender}','{recipientname}', '{massage_content}', '{currentdate}' )
        """.format(sender=username, recipientname=recipientname, massage_content=massage_content, currentdate=currentdate)
    cur.execute(sql_cmd)
    print(username, currentdate)
    return "True"

@post('/db/get_all_message/<username:path>')
def get_all_message(username):
    sql_cmd = """
            SELECT Sender, Content, SendDate
            FROM Messages
            WHERE Recipient = '{username}'
        """.format(username=username)
    cur.execute(sql_cmd)
    message_list = json.dumps(cur.fetchall())
    return message_list

@post('/db/get_allmessages')
def get_allmessages():
    sql_cmd = """
            SELECT *
            FROM Messages
        """
    cur.execute(sql_cmd)
    message_list = json.dumps(cur.fetchall())
    return message_list

@post('/db/ban/<username:path>')
def ban(username):
    sql_cmd = """
            UPDATE Users
            SET Muted = 1
            WHERE username = '{username}'
        """.format(username=username)

    execute(sql_cmd)
    commit()
    sql_cmd = """
            SELECT *
            FROM Users
            WHERE username = '{username}'
        """.format(username=username)
    cur.execute(sql_cmd)
    print(cur.fetchone())
    return "True"

@post('/db/lift/<username:path>')
def lift(username):
    sql_cmd = """
            UPDATE Users
            SET Muted = 0
            WHERE username = '{username}'
        """.format(username=username)
    execute(sql_cmd)
    commit()
    return "True"

@post('/db/check_muted/<username:path>')
def check_muted(username):

    sql_query = """
            SELECT *
            FROM Users
            WHERE username = '{username}' AND Muted = 0
        """.format(username=username)
    cur.execute(sql_query)
    # If our query returns
    print(username)
    if cur.fetchone():
        return "True"
    else:
        return "False"






def detect_attack(string_in):
    print("getit")
    print(string_in)
    if not debug:
        inj_str = ['\'','and','exec','insert','select','delete','update','count','*','%','chr','mid','master','truncate','char','declare',';','or','-','+',',','<','>','script']
        for words in inj_str:
            return "False"
        return "True"
    return "False"

@post('/waf/email/<email:path>')
def verify_email(email):
    if '@' in email:
        return 'True'
    else:
        return "Not an email address"

@post('/waf/password/<password:path>')
def verify_password(password):
    if len(password) < 8:
        return "Password is too short"

    if not any(c in string.ascii_lowercase for c in password):
        return "Password must contain at least one lowercase character"

    if not any(c in string.ascii_uppercase for c in password):
        return "Password must contain at least one uppercase character"

    return 'True'


@post('/waf/originstring/<string_in:path>')
def get_origin_string(string_in):
    print("get_origin_string")
    print(string_in)
    if not debug:
        inj_str = ['\'','and','exec','insert','select','delete','update','count','*','%','chr','mid','master','truncate','char','declare',';','or','-','+',',','<','>','script']
        for words in inj_str:
            return "False"
        return "True"
    return "False"


# Rather than using paths, you could throw all the requests with form data filled using the
# requests module and extract it here. Alternatively you could use JSON objects.

# Custom definition waf
@post('/waf/custom/field=<field:path>%20test=<test:path>')
def custom_waf(field, test):
    if re.search(test, field) is not None:
        return "True"
    return "False"

# Debug toggle
@post('/waf/debug')
def enable_debugger():
    global debug
    if debug:
        debug = False
    else:
        debug = True

if len(sys.argv) == 4:
    host = argv[1]
    port = argv[2]
    database = argv[3]



conn = sqlite3.connect(database)
cur = conn.cursor()
# Run the server
run(host=host, port=port)
