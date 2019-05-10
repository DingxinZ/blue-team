import sqlite3

# This class is a simple handler for all of our SQL database actions
# Practicing a good separation of concerns, we should only ever call
# These functions from our models

# If you notice anything out of place here, consider it to your advantage and don't spoil the surprise

class SQLDatabase():

    # Get the database running
    def __init__(self, database_arg="database.db"):
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            try:
                out = self.cur.execute(string)
            except:
                pass
        print('out:',out)
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()


    def count_user(self):
        sql_cmd = """
                SELECT count(*)
                FROM Users;
            """
        self.cur.execute(sql_cmd)
        num_of_users = self.cur.fetchone()
        return num_of_users[0]

    #-----------------------------------------------------------------------------

    # Sets up the database
    # Default admin password
    def database_setup(self, admin_password='admin'):

        # Clear the database if needed
        self.execute("""DROP TABLE IF EXISTS Users;
        DROP TABLE IF EXISTS Messages
        """)
        self.commit()

        # Create the users table
        self.execute("""CREATE TABLE Users(
            Id INTEGER,
            username TEXT,
            password TEXT,
            admin INTEGER DEFAULT 0,
            Muted INTEGER DEFAULT 0
        );
        CREATE TABLE Messages(
        Sender TEXT,
        Recipient TEXT,
        Content TEXT,
        SendDate DATE
        )""")

        self.commit()

        # Add our admin user
        self.add_user('admin', admin_password, admin=1, muted=0)



    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, username, password, admin=0, muted = 0):
        a = self.count_user()
        sql_cmd = """
                INSERT INTO Users
                VALUES({id}, '{username}','{password}', {admin}, {muted})
            """.format(id = a,username=username, password=password, admin=admin, muted=muted)

        self.execute(sql_cmd)
        self.commit()
        print(sql_cmd)
        return True

    #-----------------------------------------------------------------------------

    # Check login credentials
    def check_credentials(self, username, password):
        print(username, password)
        sql_query = """
                SELECT *
                FROM Users
                WHERE username = '{username}' AND password = '{password}'
            """.format(username=username, password=password)
        self.cur.execute(sql_query)
        # If our query returns

        if self.cur.fetchone():
            print('true')
            return True
        else:
            print('false')
            return False


    def getdate(self):
        sql_cmd = """
                SELECT datetime('now','+10 hours')
            """
        self.cur.execute(sql_cmd)
        currentdate = self.cur.fetchone()
        return currentdate[0]

    def insert_message(self, username, recipientname, massage_content):
        currentdate = self.getdate()
        sql_cmd = """
                INSERT INTO Messages
                 VALUES('{sender}','{recipientname}', '{massage_content}', '{currentdate}' )
            """.format(sender=username, recipientname=recipientname, massage_content=massage_content, currentdate=currentdate)
        self.cur.execute(sql_cmd)
        print(username, currentdate)
        return True

    def get_all_message(self, username):
        sql_cmd = """
                SELECT Sender, Content, SendDate
                FROM Messages
                WHERE Recipient = '{username}'
            """.format(username=username)
        self.cur.execute(sql_cmd)

        return self.cur.fetchall()

    def get_allmessages(self):
        sql_cmd = """
                SELECT *
                FROM Messages
            """
        self.cur.execute(sql_cmd)

        return self.cur.fetchall()

    def ban(self, username):
        sql_cmd = """
                UPDATE Users
                SET Muted = 1
                WHERE username = '{username}'
            """.format(username=username)

        self.execute(sql_cmd)
        self.commit()
        sql_cmd = """
                SELECT *
                FROM Users
                WHERE username = '{username}'
            """.format(username=username)
        self.cur.execute(sql_cmd)
        print(self.cur.fetchone())
        return True

    def lift(self, username):
        sql_cmd = """
                UPDATE Users
                SET Muted = 0
                WHERE username = '{username}'
            """.format(username=username)
        self.execute(sql_cmd)
        self.commit()
        return True

    def check_muted(self,username):
        sql_cmd = """
                SELECT *
                FROM Users
                WHERE username = '{username}'
            """.format(username=username)
        self.cur.execute(sql_cmd)
        print(self.cur.fetchone())

        sql_query = """
                SELECT *
                FROM Users
                WHERE username = '{username}' AND Muted = 0
            """.format(username=username)
        self.cur.execute(sql_query)
        # If our query returns
        print(username)
        if self.cur.fetchone():
            return True
        else:
            return False
