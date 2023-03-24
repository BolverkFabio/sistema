import sqlite3


class AtualizarCampos:
    
    def __init__(self, db_file: str = "sistema.db"):
        self.banco = sqlite3.connect(db_file)
        self.cursor = self.banco.cursor()
     
    
    def atualizarApartamentoMorador(self, numero, andar, bloco, morador): 
        try:
           self.cursor.execute(   
                """
                 UPDATE  Apartamento SET morador = ? where numero = ? AND andar = ? AND bloco = ?
                        
                """,(numero, andar, bloco, morador,)
                )
           self.banco.commit()
            
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}") 
            
    def atualizarApartamentoDependente(self, dependente): 
        try:
           self.cursor.execute(   
                """
                 UPDATE  Apartamento SET dependente = ?
                        
                """,(dependente)
                )
           self.banco.commit()
            
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}") 
            
    def atualizarApartamentoVeiculo(self, veiculo): 
        try:
           self.cursor.execute(   
                """
                 UPDATE  Apartamento SET veiculo = ?
                        
                """,(veiculo)
                )
           self.banco.commit()
            
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}") 
            
    ######### FIM APARTAMENTO #############
