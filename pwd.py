import sqlite3
import os.path

#Connection to the DB
#try:
    # Make sure to find the file.db in the script directory
    #BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    #db_path = os.path.join(BASE_DIR, "sqlite.db")
    #conn = sqlite3.connect(db_path)
#    conn = sqlite3.connect("sqlite.db")

#except sqlite3.Error as error:
#    print("Failed to read data from sqlite table", error)



# Execute query on the sqlite DB
#cur = conn.cursor()
#cur.execute("SELECT * FROM USRNAMES")

# Print everything from a table
#rows = cur.fetchall()
#for row in rows:
#        print(row)
    
# Update field 
#conn.execute("""UPDATE tasks SET name = \'jhon\'
# where id = 1""")

# close the DB connection 
#conn.close() 



def  check_usr_pwd(usr , passwd) :
    try: 
        conn = sqlite3.connect("sqlite.db")
        cur = conn.cursor()
        i = cur.execute("SELECT COUNT(*) FROM USRNAMES WHERE USERNAME = 'usr' AND PASSWD = 'passwd'").fetchall()
        if len(i) == 1 :
            return True
        else:
            return False

    except sqlite3.Error as error:
       print("Failed to read data from sqlite table", error)

    conn.close() 

    
check_usr_pwd ('Tyron' , 'password')
