from create_db import initialize
import logging
import sqlite3
import cgi

class Piwna_baza:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh = logging.FileHandler('kurwa.log')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.info('########### NOWE ODPALENIE ###########')
        try:
            initialize()
            self.logger.info('Stworzono bazę danych')
        except Exception as e:
            print(str(e))
        
        try:
            self.conn = sqlite3.connect('chuj.db')
        except Exception as e:
            self.logger.error('Nie udało się połączyć')
            self.logger.debug(str(e))
            return None

        self.c = self.conn.cursor()
        
        self.logger.info('Koniec otwierania piwnej bazy')

    def add_user(self, name: str, login: str):
        n = name
        l = login
        name = cgi.escape(name)
        login = cgi.escape(login)

        if(l != login or n != name):
            self.logger.warn('USERS HAS TRIED TO MAKE SQL INJECTION CREDENTIALS OF ADDED USER:')

        juzerzy = self.c.execute('SELECT * FROM USERS WHERE LOGIN = "{}"'.format(login)).fetchall()
        if(len(juzerzy) != 0):
            self.logger.warn('user login already existed; login: {}'.format(login))
            raise ValueError('User already exists')

        self.logger.info('Adding new user NAME: {}   LOGIN: {}'.format(name, login))
        self.c.execute('INSERT INTO USERS(NAME, LOGIN) VALUES {0}, {1}'.format(name, login))
        self.logger.info('added')
        self.conn.commit()

        self.logger('dodano!')
        return 0


    def get_piwka_ktore_ci_wisza(self, ID : int):
        if(type(ID) != int):
            self.logger.warn('ktos probowal SQL injction w get_piwka_ktore_ci_wisza ID: %s', str(ID))
            return
        try:
            
            self.logger.info('odczytanie wlasnych piwek ID: %s', str(ID))
            self.c.execute('''SELECT NAME, LOGIN 
                                FROM PIWKAHEHE p 
                                LEFT JOIN USERS u
                                ON u.ID = p.TO_ID
                                WHERE ID = {}; '''.format(ID))
            piwka = self.c.fetchall()
            self.logger.info('piwka pomyślnie odczytane')
            return piwka
        except Exception as e:
            self.logger.warn('Problem with connection, unable to get piwka ktore ci wisza, ID:%s', str(ID))
            self.logger.debug('exception: %s', str(e))
            return 


    def get_piwka_ktore_wisisz(self, ID: int):
        if(type(ID) != int):
            self.logger.warn('ktos probowal SQL injction w get_piwka_ktore_wisisz ID: %s', str(ID))
            return 1
        try:
            
            self.logger.info('odczytanie piwek ktore wisi ID: %s', str(ID))
            self.c.execute('''SELECT NAME, LOGIN 
                                FROM PIWKAHEHE p 
                                LEFT JOIN USERS u
                                ON u.ID = p.FROM_ID
                                WHERE ID = {}; '''.format(ID))
            piwka = self.c.fetchall()
            self.logger.info('piwka pomyślnie odczytane')
            return piwka
        except Exception as e:
            self.logger.warn('Problem with connection, unable to get piwka ktore wisisz, ID:%s', str(ID))
            self.logger.debug('exception: %s', str(e))
            return 1
        return 0

    def add_piwko_ID(self, ID_from: int, ID_to: int):
        if(type(ID_from)!= int or type(ID_to) != int):
            self.logger.warn('ktos probowal SQL injction w add_piwko_ID ID: %s', str(ID))
            return
        
        self.logger('dodawanie piwka od: {0}     do: {1}'.format(ID_from, ID_to))

        self.c.execute('INSERT INTO PIWKAHEHE(FROM_ID, TO_ID) VALUES {0}, {1}'.format(ID_from, ID_to))
        self.conn.commit()

        self.logger.info('dodano piwerko')
        return 0

    def get_user_ID(self, login: str):
        l = login
        login = cgi.escape(login)

        if(l != login):
            self.logger.warn('USERS HAS TRIED TO MAKE SQL INJECTION LOGIN: {}'.format(login))
        
        jusers = self.c.execute('SELECT ID FROM USERS u WHERE u.LOGIN = "{}" LIMIT 2'.format(login)).fetchall()

        if(len(jusers)==0):
            self.logger.warn('user doesnt exist login: {}'.format(login))
            raise ValueError('user doesnt exist')

        return jusers[0]
        

    def close(self):
        self.logger.info('zamykanie bazy...')
        try:
            self.conn.commit()
            self.conn.close()
            self.logger.info('udało sie zamknąć bazę')
        except Exception as e:
            self.logger.debug(str(e))
            self.logger.error('Nie udało się zamknąć bazy')
        

if(__name__ == '__main__'):
    p = Piwna_baza()
    print('piwka: ', p.get_piwka_ktore_ci_wisza(1))
    p.add_user('piotr', 'malina')
    id = p.get_user_ID('Pestka')
    print(id)
    p.close()