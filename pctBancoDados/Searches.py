import sqlite3


class Buscas:
    
    def __init__(self, db_file: str = "sistema.db"):
             self.banco = sqlite3.connect(db_file)
             self.cursor = self.banco.cursor()
             
    ###### VERIFICAR LOGIN ########         
    def Autenticacao(self, login, senha):
        try:
            self.cursor.execute(
                """
                    SELECT * FROM Usuario;
                """
            )
            for linha in self.cursor.fetchall():
                if linha[1] == login and linha[2] == senha:
                     print('sao iguais')
                     
                break 
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
            
    
    def buscarMorador(self, cpf):
        try:
            self.cursor.execute(
                """
                    SELECT * FROM Morador;
                """
            )
            for linha in self.cursor.fetchall():
                if linha[4] == cpf:
                     #print('sao iguais')
                     return linha[0] 
                break 
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
            
    def buscarVeiculo(self, placa):
        try:
            self.cursor.execute(
                """
                    SELECT * FROM Veiculo;
                """
            )
            for linha in self.cursor.fetchall():
                if linha[3] == placa:
                     print('sao iguais')
                     
                break 
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
            
    def buscarDependente(self, cpf):
        try:
            self.cursor.execute(
                """
                    SELECT * FROM Dependentes;
                """
            )
            for linha in self.cursor.fetchall():
                if linha[1]== cpf:
                     print('sao iguais')
                     
                break 
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
            
    def buscarApartamento(self, numero, andar, bloco):
        try:
            self.cursor.execute(
                """
                    SELECT * FROM Apartamento;
                """
            )
            for linha in self.cursor.fetchall():
                if linha[0]== numero and linha[1] == andar and linha[2] == bloco:
                     return True
                break 
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
            
            