import sqlite3

# Connect to the database
conn = sqlite3.connect("Database/login.db")
cursor = conn.cursor()

# Execute a SELECT query to fetch all entries from the table
cursor.execute("SELECT * FROM loginData")
rows = cursor.fetchall()

# Print the entries
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
