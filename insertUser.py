#!/usr/bin/python  
  
import sqlite3  
  
conn = sqlite3.connect('sqlite.db')  ;
print ("Opened database successfully");  
user = 'Tyron';
passs = 'password';

conn.execute('INSERT INTO Users (ID, USERNAME , FIRSTNAME, LASTNAME, PASSWD, EMAIL  ) VALUES(1 ,"LouwEtienne","Etienne","Louw","password","louwetienne@gmail.com")'  );
print ("Table inserted successfully");  
cur = conn.cursor()
cur.execute("SELECT * FROM USERS")

# Print everything from a table
rows = cur.fetchall()
for row in rows:
        print(row)
conn.commit()
  
conn.close()  