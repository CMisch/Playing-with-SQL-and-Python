#test of practice with sqlite3.py file


import sqlite3

# Connect to the SQLite database (create a new database if it doesn't exist)
conn = sqlite3.connect('Contacts.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Retrieve data from the table
cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    
# Close the cursor and the connection
cursor.close()
conn.close()
