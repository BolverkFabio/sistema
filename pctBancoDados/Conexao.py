import sqlite3

class conexaoBanco():
    def __init__(self, db_file: str = "sistema.db"):
        self.banco = sqlite3.connect(db_file)
        self.cursor = self.banco.cursor()
        
    @property
    def cursor(self):
         return self._cursor
     
    @cursor.setter
    def cursor(self, cursor):
        if cursor != " ":
            self._cursor = cursor
            
            
    @property
    def banco(self):
         return self._banco
     
    @banco.setter
    def banco(self, banco):
        if banco != " ":
            self._banco = banco
        
        
    
    def desconecta(self):
        try:
            self.banco.close()
        except sqlite3.Error as e:
            print(f"Erro ao desconectar do banco de dados: {e}")