from pctBancoDados.Conexao import conexaoBanco
import sqlite3


class InserirDados:
    
    def __init__(self, db_file: str = "sistema.db"):
        self.banco = sqlite3.connect(db_file)
        self.cursor = self.banco.cursor()
        
            
    def inserirMorador(self, nome, cel1, cel2, email, cpf, rg): 
        try:
           self.cursor.execute(   
                """
                 INSERT INTO Morador
                        (nome, cel1, cel2, email, cpf, rg) VALUES(?, ?, ?, ?, ?, ?)
                """,(nome, cel1, cel2, email, cpf, rg)
                )
           self.banco.commit()
            
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")  
            
    
    
    def inserirDependentes(self, nome):
        try:
            self.cursor.execute(
                """
                 INSERT INTO Dependentes
                        (nome) VALUES(?)
                """,(nome))
            self.banco.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")   
    
    def inserirVisitantes(self, nome, cpf, rg):
        try:
            self.cursor.execute(
                """
                 INSERT INTO Visitantes
                        (nome, cpf, rg, data, userSistema) VALUES(?, ?, ?)
                """,(nome, cpf, rg))
            self.banco.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}") 
    
    def inserirApartamento(self, numero, andar, bloco):
        try:
            self.cursor.execute(
                """
                 INSERT INTO Apartamento
                        (numero, andar, bloco) VALUES(?, ?, ?)
                """,(numero, andar, bloco))
            self.banco.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}") 
            
    ##### AUTENTICACAO #######
    
    def inserirNovoUsuario(self, nome):
        try:
            self.cursor.execute(
                """
                 INSERT INTO Usuario
                        (nome) VALUES(?)
                """,(nome,))
            self.banco.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}") 
            
    def inserirNovoLogin(self,login, senha):
        try:
            self.cursor.execute(
                """
                 INSERT INTO Usuario
                        (login, senha) VALUES(?, ?)
                """,(login, senha))
            self.banco.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}") 
            
     ### USUARIO PADRAO #######
            
    def AutenticadoUserPadrao(self): ##loginPadrão
        try:
            self.cursor.execute(
                """
                 INSERT INTO Usuario
                        (nome, login, senha) VALUES('fabio', 'Master', 'qos123')
                """,#(nome, login, senha)
                )
            self.banco.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")  
    ###### FIM AUTENTICAÇÃO #######
    
    def inserirDataRegistro(self, data):
        try:
           self.cursor.execute(   
                """
                 INSERT INTO RegistroData
                        (data) VALUES(?)
                """,(data,)
                )
           self.banco.commit()
            
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")  
            
    
    