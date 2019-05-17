from bottle import route, get, post, request, redirect, static_file

import hashlib

import model
import requests
import sys

waf_url = 'http://localhost:8081/waf/'
port = sys.argv[2]
if len(sys.argv) == 8:
    port = sys.argv[2]
    waf_host = sys.argv[3]
    waf_port = sys.argv[4]
    waf_url = 'http://' + waf_host + ':' + waf_port + '/waf/'
def send_request(path, input_from, string_in):
    r = requests.post(waf_url + path + port + ':' + input_from + string_in)
    r = r.content.decode()
    return r


# sql.SQLDatabase

#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    return static_file(picture, root='img/')

#-----------------------------------------------------------------------------

# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')

#-----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    return static_file(js, root='js/')

#-----------------------------------------------------------------------------
# Pages
#-----------------------------------------------------------------------------

# Redirect to login
@get('/')
@get('/home')
def get_index():
    return model.index_page()

#-----------------------------------------------------------------------------

# Display the login page
@get('/login')
def get_login_controller():
    return model.login_page()

#-----------------------------------------------------------------------------

# Attempt the login
@post('/login')
def post_login():
    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')

    a = send_request('detectunandpw/', 'login_username/', username)
    b = send_request('detectunandpw/', 'login_password/', password)

    #print(a.content.decode())
    if a != "True":
        return model.error_page(a)
    if b != "True":
        return model.error_page(b)

    # Call the appropriate method
    return model.login_check(username, password)

@post('/register')
def post_register():
    # Handle the form processing
    #a = requests.post('http://localhost:8081/waf/detect'+)

    username = request.forms.get('username')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    a = send_request('detectunandpw/', 'register_username/', username)
    b = send_request('detectunandpw/', 'register_password/', password)

    c = send_request('password/', 'register_password/', password)

    #print(a.content.decode())
    if a != "True":
        return model.error_page(a)
    if b != "True":
        return model.error_page(b)
    if c != "True":
        return model.error_page(c)

    if password == password2:
        return model.create_account(username, password)
    else:
        return model.error_page("Two passwords not same")
    # Call the appropriate method

@post('/send')
def post_message():
    # Handle the form processing
    recipientname = request.forms.get('recipientname')
    massage_content = request.forms.get('massage_content')

    a = send_request('detectunandpw/', 'post_message_recipientname_from_user: ' + request.get_cookie("username") + '/', recipientname)
    b = send_request('detect/', 'post_message_massage_content_from_user: '+ request.get_cookie("username") + '/', massage_content)
    c = send_request('detectunandpw/', 'post_message_recipientname_from_user: ' + request.get_cookie("username") + '/', request.get_cookie("username"))
    if a != "True":
        return model.error_page(a)
    if b != "True":
        return model.error_page(b)
    if c != "True":
        return model.error_page(c)

    # Call the appropriate method
    return model.insert_message(recipientname, massage_content)








#-----------------------------------------------------------------------------

@get('/about')
def get_about():
    return model.about_page()


#-----------------------------------------------------------------------------


@get('/register')
def get_register_controller():
    return model.register_page()

@get('/sendmessage')
def get_send_message():
    return model.send_message()

@get('/messagebox')
def get_message_box():
    return model.message_box()

@get('/allmessages')
def get_allmessages():
    return model.allmessages()

@get('/messagecontent')
def get_messagecontent():
    return model.messagecontent()

@get('/logout')
def get_logout():
    return model.logout()

@get('/banuser')
def get_banuser():
    return model.banuser()

@post('/ban')
def post_banuser():
    username = request.forms.get('username')
    a = send_request('detectunandpw/', 'banuser_username/', username)
    if a != "True":
        return model.error_page(a)
    return model.ban(username)

@post('/Lift')
def post_liftuser():
    username = request.forms.get('username')
    a = send_request('detectunandpw/', 'liftuser_username/', username)
    if a != "True":
        return model.error_page(a)
    return model.lift(username)


@get('/user')
def get_user():
    return model.profile()



@get('/Front-end')
def get_HTML_int():
    return model.frontend()

@get('/Back-end')
def get_HTML_int():
    return model.backend()

@get('/Database')
def get_HTML_int():
    return model.thedatabase()

@get('/HTML-int')
def get_HTML_int():
    return model.html_int()

@get('/HTML-tut')
def get_HTML_tut():
    return model.html_tut()

@get('/CSS-int')
def get_CSS_int():
    return model.css_int()

@get('/CSS-tut')
def get_CSS_tut():
    return model.css_tut()

@get('/JS-int')
def get_JS_tut():
    return model.js_int()

@get('/JS-tut')
def get_JS_tut():
    return model.js_tut()

@get('/PHP-int')
def get_PHP_tut():
    return model.php_int()

@get('/PHP-tut')
def get_PHP_tut():
    return model.php_tut()

@get('/PB-int')
def get_PB_tut():
    return model.pb_int()

@get('/PB-tut')
def get_PB_tut():
    return model.pb_tut()

@get('/SQL-int')
def get_SQL_tut():
    return model.sql_int()

@get('/SQL-tut')
def get_SQL_tut():
    return model.sql_tut()

@get('/SQLite-int')
def get_SQL_tut():
    return model.sqlite_int()

@get('/SQLite-tut')
def get_SQL_tut():
    return model.sqlite_tut()

@get('/Mysql-int')
def get_SQL_tut():
    return model.mysql_int()

@get('/Mysql-tut')
def get_SQL_tut():
    return model.mysql_tut()
