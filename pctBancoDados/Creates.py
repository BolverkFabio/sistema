from pctBancoDados.Conexao import conexaoBanco
import sqlite3


class Tabelas:
    
        def __init__(self, db_file: str = "sistema.db"):
             self.banco = sqlite3.connect(db_file)
             self.cursor = self.banco.cursor()
            

        def criar_tabelas(self):
                try:
                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS Morador(
                                nome TEXT NOT NULL,
                                cel1 TEXT NOT NULL,
                                cel2 TEXT,
                                email TEXT NOT NULL,
                                cpf TEXT NOT NULL,
                                rg TEXT NOT NULL
                            )
                        """
                    )
                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS Apartamento(
                                numero TEXT NOT NULL,
                                andar TEXT NOT NULL,
                                bloco TEXT NOT NULL,
                                morador TEXT,
                                dependente TEXT,
                                veiculo TEXT
                            )
                        """
                    )

                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS Dependentes(
                                nome TEXT NOT NULL,
                                cpf TEXT NOT NULL
                            )
                        """
                    )

                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS Visitante(
                                nome TEXT NOT NULL,
                                cpf TEXT NOT NULL,
                                rg TEXT NOT NULL,
                                bloco TEXT,
                                apt TEXT
                             )
                        """
                    )
                    
                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS Veiculo(
                                marca TEXT NOT NULL,
                                modelo TEXT NOT NULL,
                                cor TEXT NOT NULL,
                                placa TEXT NOT NULL
                            )
                        """
                    )
                    
                    
                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS Usuario(
                                nome TEXT NOT NULL,
                                login TEXT NOT NULL,
                                senha TEXT NOT NULL                          
                            )
                        """
                    )
                    
                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS UsuarioLogado(
                                nome TEXT NOT NULL
                               
                            )
                        """
                    )
                    
                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS RegistroData(
                                data TEXT NOT NULL
                            )
                        """
                    )
                    
                    self.cursor.execute(
                        """
                            CREATE TABLE IF NOT EXISTS RegistroUsuario(
                                UserSistema TEXT NOT NULL     
                            )
                        """
                    )
                    
                    
                    
                    

                    self.banco.commit()
                except sqlite3.Error as e:
                    print(f"Erro ao criar tabela: {e}") 
                    
                    