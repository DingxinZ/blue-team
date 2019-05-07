from bottle import run

#-----------------------------------------------------------------------------
# Get our components
# You may eventually wish to put these in their own directories and then load
# Each file separately
# For the template, we will keep them together
import model
import view
import controller
import userid
#-----------------------------------------------------------------------------

'''
    This file is the one to run to start your webserver
    Keep it clean and keep it simple, you're going to have
    Up to 5 people running around breaking this constantly
    If it's all in one file, then things are going to be hard to fix

    If in doubt, `import this`
'''

#-----------------------------------------------------------------------------
# It might be a good idea to move the following settings to a config file and then load them
# Change this to your IP address or 0.0.0.0 when actually hosting
host = '10.83.65.37'

# Test port, change to the appropriate port to host
port = 8080

# Turn this off for production
debug = True
#-----------------------------------------------------------------------------

#Run the server
run(host=host, port=port, debug=debug)
