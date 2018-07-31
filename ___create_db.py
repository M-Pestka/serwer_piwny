import sqlite3



def ___init():

    conn = sqlite3.connect('chuj.db')
    
    c = conn.cursor()

    # tworzenie juserow
    try:
        c.execute('''CREATE TABLE USERS(
                    ID INTEGER NOT NULL PRIMARY KEY ASC,
                    NAME TEXT NOT NULL,
                    LOGIN TEXT NOT NULL
        )''')

        c.execute('INSERT INTO USERS(NAME, LOGIN) VALUES ("Michał", "Pestka");')
        conn.commit()
    except:
        pass

    # tworzenie tabeli piwek
    try:
        c.execute('''CREATE TABLE PIWKAHEHE(
                    FROM INT,
                    TO INT
        )''')
        c.execute('INSERT INTO USERS(FROM, TO) VALUES (1, 1);')
        conn.commit()
    except:
        pass
    
    conn.close()

if(__name__=='__main__'):
    ___init()

