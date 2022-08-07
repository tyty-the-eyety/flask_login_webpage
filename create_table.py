#!/usr/bin/python  
  
import sqlite3
  
conn = sqlite3.connect('sqlite.db')
print ("Opened database successfully"); 

conn.execute('''DROP TABLE Users;''')
  
conn.execute('''CREATE TABLE Users 
       (ID INT PRIMARY KEY     NOT NULL, 
       USERNAME           TEXT    NOT NULL,  
       FIRSTNAME     TEXT NOT NULL,
       LASTNAME      TEST NOT NULL,
       PASSWD         TEXT,
       EMAIL  TEXT NOT NULL);''')  
print ("Table created successfully");  
  
conn.close()  