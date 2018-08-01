import sqlite3
import logging
import os


def initialize():
    if(os.path.exists('chuj.db')):
        return 
    conn = sqlite3.connect('chuj.db')
    
    c = conn.cursor()
    
    # tworzenie juserow
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS USERS(
                    ID INTEGER NOT NULL PRIMARY KEY ASC,
                    NAME TEXT NOT NULL,
                    LOGIN TEXT NOT NULL UNIQUE);''')

        conn.commit()

        c.execute('''INSERT INTO USERS(NAME, LOGIN) VALUES ("Michał", "Pestka");''')
        
        conn.commit()
        
    except Exception as e:
        print(str(e))

    # tworzenie tabeli piwek
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS PIWKAHEHE(
                    FROM_ID INT,
                    TO_ID INT);''')

        conn.commit()

        c.execute('''INSERT INTO PIWKAHEHE(FROM_ID, TO_ID) VALUES (1, 1);''')
        conn.commit()
    except Exception as e :
        print(str(e))
    
    conn.close()





