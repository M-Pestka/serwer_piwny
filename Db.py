from ___create_db import ___init



class Piwna_baza:
    def __init__(self):
        self.logger = Logger()
        try:
            ___init()
            self.logger.creation()
        except:
            pass
        
        self.conn = sqlite3.connect('chuj.db')
        self.c = self.conn.cursor()
        
        self.logger.init()

    def add_user(self, name: str, login: str):
        pass

    def get_piwka(self, ID : int):
        pass
    
    def add_piwko(self, ID_from: int, ID_to: int):
        pass

    def __del__(self):
        logger.logout()
        conn.commit()
        conn.close()
        logger.db_closed()

