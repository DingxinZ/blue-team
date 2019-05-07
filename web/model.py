import random
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view
import sql
import userid

database = sql.SQLDatabase()
database.database_setup()
theuser = userid.userid()
print("!!! ")


# Initialise our views, all arguments are defaults
page_view = view.View()


def register_page():
    return page_view("register")
#-----------------------------------------------------------------------------
# Index
#-----------------------------------------------------------------------------

def index_page():
    if theuser.logged_in:
        print(theuser.logged_in)
        return page_view("index", "headerloggedin")
    else:
        print(theuser.logged_in)
        return page_view("index", theuser.userheader)

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
    if database.check_credentials(username, password):
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
        if username == "admin":
            theuser.username = username
            theuser.isadmin = True
            theuser.userheader = "headeradmin"
        else:
            theuser.username = username
            theuser.logged_in = True
            theuser.userheader = "headerloggedin"
        return page_view("index", theuser.userheader)
    else:
        return page_view("invalid", reason=err_str)



def create_account(username, password):

    database.add_user(username, password, 1, 0)

    return login_page()




def insert_message(recipientname, massage_content):
    database.insert_message(theuser.username, recipientname, massage_content)


    return send_message()

#-----------------------------------------------------------------------------
# About
#-----------------------------------------------------------------------------

def about_page():
    return page_view("about", garble=about_garble())

def send_message():
    if database.check_muted(theuser.username):
        return page_view("sendmessage", theuser.userheader)
    else:
        return page_view("index", theuser.userheader)

def message_box():
    data = database.get_all_message(theuser.username)
    print(data)
    #return page_view("sendmessage", "headerloggedin")
    return page_view.with_table( "messagebox", theuser.userheader, "tailer", data)
    #return page_view("messagebox")

def allmessages():
    data = database.get_allmessages()

    return page_view.with_table( "allmessages", theuser.userheader, "tailer", data)

def banuser():
    return page_view("banuser", theuser.userheader)

def ban(username):
    database.ban(username)
    return page_view("banuser", theuser.userheader)

def lift(username):
    database.lift(username)
    return page_view("banuser", theuser.userheader)


def logout():
    theuser.userheader = "header"
    theuser.logged_in = False
    theuser.isadmin = False
    return page_view("index", theuser.userheader)



def profile():
    username = theuser.username
    return page_view.profile(username,theuser.userheader)


def frontend():
    return page_view("Front-end", theuser.userheader)

def backend():
    return page_view("Back-end", theuser.userheader)

def thedatabase():
    return page_view("Database", theuser.userheader)

def html_int():
    return page_view("HTML-int", theuser.userheader)

def html_tut():
    return page_view("HTML-tut", theuser.userheader)
    if theuser.logged_in:
        print(theuser.logged_in)
        return page_view("HTML-tut", theuser.userheader)
    else:
        print(theuser.logged_in)
        return page_view("HTML-tut")

def css_int():
    return page_view("CSS-int", theuser.userheader)

def css_tut():
    return page_view("CSS-tut", theuser.userheader)

def js_int():
    return page_view("JS-int", theuser.userheader)

def js_tut():
    return page_view("JS-tut", theuser.userheader)

def php_int():
    return page_view("PHP-int", theuser.userheader)

def php_tut():
    return page_view("PHP-tut", theuser.userheader)

def pb_int():
    return page_view("PB-int", theuser.userheader)

def pb_tut():
    return page_view("PB-tut", theuser.userheader)

def sql_int():
    return page_view("SQL-int", theuser.userheader)

def sql_tut():
    return page_view("SQL-tut", theuser.userheader)

def sqlite_int():
    return page_view("SQLite-int", theuser.userheader)

def sqlite_tut():
    return page_view("SQLite-tut", theuser.userheader)

def mysql_int():
    return page_view("Mysql-int", theuser.userheader)

def mysql_tut():
    return page_view("Mysql-tut", theuser.userheader)







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
