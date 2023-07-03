#U07A1 


#Create a SELECT statement that contains only FirstName, LastName, and EmailAddress from the contacts table.
#Create an UPDATE statement that updates a contacts EmailAddress and PhoneNumber.
#Delete the information for the last contact added to the contacts table.
#Execute a SELECT statement to retrieve all the columns of data from your contacts table.

#Created by Chris Misch

import sqlite3 as sq

conn = sq.connect('Contacts.db')
curs = conn.cursor()

# Update data in the table
#curs.execute("INSERT INTO contacts (FirstName, LastName, PhoneNumber, EmailAddress) VALUES (?, ?, ?, ?)", ('Peter', 'Filez', '999-562-7531', 'pfilez@gmail.com'))
#conn.commit()
#
## Update data in the table
#curs.execute("UPDATE contacts SET LastName = ? WHERE FirstName = ?", ('Smith', 'Mary'))
#conn.commit()
#
#Retrieve database and set # Retrieve data from the table
curs.execute("SELECT * FROM contacts")
rows = curs.fetchall()
for row in rows:
    print(f"ID: {row[0]}, \tName: {row[1]}, \tLast: {row[2]}, \tPhone: {row[3]}, \tEmail: {row[4]}")
    
print("")
#Use a select statment that contains only FirstName, LastName, and EmailAddress
curs.execute("SELECT FirstName, LastName, EmailAddress FROM contacts")
rows = curs.fetchall()
for row in rows:
    print(f"Name: {row[0]},\tLast: {row[1]},\tEmail: {row[2]}")

curs.close()
conn.close()