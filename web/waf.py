from bottle import run, request, post, get
import re
import string
import sys

# Important globals
host = "localhost"
port = "8081"

# Debug mode to check whether or not attacks are working
# Start with it as "True", try the attack, flip it to false, try the attack again and see if your WAF blocked it
# Debug should be set to false when launching the final version
debug = False
reprot_file = "report.txt"


def report_attack(input_from, attack_word, string_in):
    f = open(reprot_file, "a")
    f.write("Input string from: %s\n" % input_from)
    f.write("Attack word: %s\n" % attack_word)
    f.write("Input string: %s\n" % string_in)
    f.write("\n")
    f.close()
    return

@post('/waf/detect/<input_from:path>/<string_in:path>')
def detect_attack(input_from, string_in):
    origininput = string_in
    string_in.lower()
    if not debug:
        attacks = ['\' +or','\' +and', '\' *\) *;', '< *script','and','delete','or',';',',','-','\+','\*','scr','admin','>','<','drop','script', '\\\\','/','alert']
        for attack in attacks:
            if re.search(attack, string_in) is not None:
                report_attack(input_from, attack, origininput)
                return "Stop attacking our website."

        return "True"
    return "False"

@post('/waf/detectunandpw/<input_from:path>/<string_in:path>')
def detect_attack_from_usrname_and_pw(input_from, string_in):
    origininput = string_in
    string_in.lower()
    print(string_in)
    if not debug:
        attacks = ['\' +or','\' +and', '\' *\) *;', '< *script','and','delete','or',';',',','-','\+','\*','scr','admin','>','<','drop','script', '\\\\','/','alert']
        for attack in attacks:
            if re.search(attack, string_in) is not None:
                report_attack(input_from, attack, origininput)
                return "Stop attacking our website."

        return "True"
    return "False"

@post('/waf/password/<input_from:path>/<password:path>')
def verify_password(input_from, password):
    if len(password) < 8:
        print("Password is too short")
        return "Password is too short"

    if not any(c in string.ascii_lowercase for c in password):
        print("Password must contain at least one lowercase character")
        return "Password must contain at least one lowercase character"

    if not any(c in string.ascii_uppercase for c in password):
        print("Password must contain at least one uppercase character")
        return "Password must contain at least one uppercase character"

    inj_str = ['\'', '-', ' ', '<','>','script']
    for word in inj_str:
        if word in password:
            print(word)
            #report_attack(input_from, word, origininput)
            return "Don't include \'" + word + "\' in your username or password."

    print("password valid")
    return 'True'

# droped function
@post('/waf/originstring/<string_in:path>')
def get_origin_string(string_in):
    print("get_origin_string")
    print(string_in)

    if not debug:
        inj_str = ['\'','-']
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
    host = sys.argv[1]
    port = sys.argv[2]
    reprot_file = sys.argv[3]



# Run the server
run(host=host, port=port)
