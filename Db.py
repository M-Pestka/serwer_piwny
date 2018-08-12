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

    def sanitize(input_str):
        return input_str

    def add_user(self, name: str, login: str):
        
        #raise Exception('zaipleentuj sanitacje chuju')

        name = name.capitalize()
        login = login.capitalize()
        juzerzy = self.c.execute('SELECT * FROM USERS WHERE LOGIN = (?)',(login,)).fetchall()
        if(len(juzerzy) != 0):
            self.logger.warn('user login already existed; login: {}'.format(login))
            raise ValueError('User already exists')
        
        self.logger.info('Adding new user NAME: {}   LOGIN: {}'.format(name, login))
        self.c.execute('INSERT INTO USERS(NAME, LOGIN) VALUES (?, ?)',(name, login))
        self.logger.info('added')
        self.conn.commit()

        self.logger.info('dodano!')
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
                                ON u.ID = p.FROM_ID
                                WHERE p.TO_ID = (?); ''',(ID,))
            piwka = self.c.fetchall()
            print(piwka)
            self.logger.info('piwka pomyślnie odczytane')
            return piwka
        except Exception as e:
            self.logger.warn('Problem with connection, unable to get piwka ktore ci wisza, ID:%s', str(ID))
            self.logger.debug('exception: %s', str(e))
            return 

    def get_piwka_ktore_wisisz(self, ID: int):
        if(type(ID) != int):
            self.logger.warn('SQL injection ID: {}'.format(str(ID)))
        try:
            
            self.logger.info('odczytanie piwek ktore wisi ID: %s', str(ID))
            self.c.execute('''SELECT NAME, LOGIN
                                FROM PIWKAHEHE p 
                                LEFT JOIN USERS u
                                ON u.ID = p.TO_ID
                                WHERE FROM_ID = (?); ''',(ID,))
            piwka = self.c.fetchall()
            self.logger.info('piwka pomyślnie odczytane')
            return piwka
        except Exception as e:
            self.logger.warn('Problem with connection, unable to get piwka ktore wisisz, ID:%s', str(ID))
            self.logger.debug('exception: %s', str(e))
            return 1
        return 0

    def add_piwko(self, ID_from: int, ID_to: int):
        if(type(ID_from) != int or type(ID_to) != int):
            self.logger.warn('SQL injection ID: {}'.format(str(ID)))
        
        self.logger.info('dodawanie piwka od: {0}     do: {1}'.format(ID_from, ID_to))

        self.c.execute('INSERT INTO PIWKAHEHE(FROM_ID, TO_ID) VALUES (?, ?)',(ID_from, ID_to))
        self.conn.commit()

        self.logger.info('dodano piwerko')
        return 0

    def get_user_ID(self, login: str) -> int:
        raise Exception('zaimplementuj sanitacje chuju')
        self.logger.debug('getowanie ID jusera: {}'.format(login))
        
        login = login.capitalize()
        jusers = self.c.execute('SELECT ID FROM USERS u WHERE u.LOGIN = (?) LIMIT 2', (login,)).fetchone()

        if(jusers is None or len(jusers)==0):
            self.logger.warn('user doesnt exist login: {}'.format(login))
            raise ValueError('user doesnt exist')

        return jusers[0]
        
    def count_users(self):
        a = self.c.execute('SELECT COUNT(*) FROM USERS').fetchone()
        self.logger.info('policzono juserow')
        return a

    def count_all_piwka(self):
        a = self.c.execute('SELECT COUNT(*) FROM USERS').fetchone()
        self.logger.info('policzono piwka')
        return a 

    def oddaj_piwko(self, ID_kto_oddaje, ID_kto_przyjmuje):
        if(type(ID_kto_oddaje) != int or type(ID_kto_przyjmuje) != int):
            self.logger.warn('SQL injection ID: {}'.format(str(ID)))
            raise ValueError('no i chuj')
        self.logger.info('proba oddania piwkaod: {}    do:{} '.format(ID_kto_oddaje, ID_kto_przyjmuje))
        a = self.c.execute('SELECT * FROM PIWKAHEHE WHERE FROM_ID = (?) AND TO_ID = (?);''',(ID_kto_oddaje, ID_kto_przyjmuje)).fetchall()
        print(a)
        if(a is None or a == list()):
            self.logger.warn('OSZUKUJOOOOOOO od: {}    do:{} '.format(ID_kto_oddaje, ID_kto_przyjmuje))
            raise ValueError('chuje oszukujo nie ma takiego piwka')
        self.logger.info('oddawanie piwka od: {}    do:{} '.format(ID_kto_oddaje, ID_kto_przyjmuje))
        self.c.execute('''DELETE FROM PIWKAHEHE WHERE TRANS_ID = 
                    (SELECT MIN(TRANS_ID) FROM PIWKAHEHE 
                        WHERE FROM_ID = (?) AND TO_ID = (?));''',(ID_kto_oddaje, ID_kto_przyjmuje))
        self.conn.commit()
        self.logger.info('piwko oddane :3')

    def remove_user(self, user_ID: int):
        if(type(user_ID) != int):
            self.logger.warn('SQL injection ID: {}'.format(str(user_ID)))
            raise ValueError('noi chuj')
        self.logger.warn('trying to delete user ID:{}'.format(user_ID))
        a = self.c.execute('select name, login from users where ID = (?)',(user_ID,))

    def get_all_users(self):
        all_users = self.c.execute('SELECT LOGIN FROM USERS').fetchall()
        return all_users

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
    p.oddaj_piwko(1,2)