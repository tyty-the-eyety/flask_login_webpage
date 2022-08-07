#!/usr/bin/python  
  
import sqlite3  
  
conn = sqlite3.connect('sqlite.db')  ;
print ("Opened database successfully");  
  
conn.execute('''CREATE TABLE USRNAMES 
       (ID INT PRIMARY KEY     NOT NULL, 
       USERNAME           TEXT    NOT NULL,  
       PASSWD         TEXT);''')  
print ("Table created successfully");  
  
conn.close()  