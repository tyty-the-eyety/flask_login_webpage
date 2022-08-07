#!/usr/bin/python  
  
import sqlite3  
  
conn = sqlite3.connect('sqlite.db')  ;
print ("Opened database successfully");  
user = 'Tyron';
passs = 'password';

#conn.execute('INSERT INTO USRNAMES  (ID, USERNAME , PASSWD  ) VALUES(1 ,"Tyron" , "password")'  );
print ("Table inserted successfully");  
cur = conn.cursor()
cur.execute("SELECT * FROM USRNAMES")

# Print everything from a table
rows = cur.fetchall()
for row in rows:
        print(row)
conn.commit()
  
conn.close()  