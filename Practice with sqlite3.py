#Practice with sqlite3


import sqlite3

# Connect to the SQLite database (create a new database if it doesn't exist)
conn = sqlite3.connect('tutorial.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Update data in the table
cursor.execute("UPDATE contacts SET LastName = ? WHERE FirstName = ?", ('McFray', 'John Doe'))
conn.commit()

# Delete data from the table
cursor.execute("DELETE FROM employees WHERE name = ?", ('Jane Smith',))
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Close the cursor and the connection
cursor.close()
conn.close()
