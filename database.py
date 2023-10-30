import sqlite3

# Create a connection to the database (this will create the database file)
conn = sqlite3.connect("Database/login.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the "loginData" table with the specified columns
cursor.execute('''
    CREATE TABLE loginData (
        user_entry TEXT,
        name_entry TEXT,
        pass_entry TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
