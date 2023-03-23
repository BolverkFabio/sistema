from pctBancoDados.Inserts import InserirDados

class FuncaoMorador:
    
    def __init__(self):
          self.inserir = InserirDados()
    
    def cadastroMorador(self, nome, cel1, cel2, email, cpf, rg ):
        self.inserir.inserirMorador(nome, cel1, cel2, email, cpf, rg)
        
        
        
        