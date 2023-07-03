#Updates the contact table with primary key data

import sqlite3 as sq
# Connect to the SQLite database (create a new database if it doesn't exist)
conn = sq.connect('Contacts.db')

# Create a cursor object to execute SQL commands
curs = conn.cursor()

#delete a table
curs.execute("DROP TABLE IF EXISTS contacts")

#commit changes
conn.commit()

# Close the cursor and the connection
curs.close()
conn.close()

