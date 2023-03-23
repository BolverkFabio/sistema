from pctBancoDados.Inserts import InserirDados
from pctBancoDados.Searches import*
from pctBancoDados.Updates import *



class FuncaoApartamento:
    def __init__(self):
        self.inserir = InserirDados()
        self.buscar = Buscas()
        self.atualizar = AtualizarCampos()
    

    
    def cadastroApt(self, numero, andar, bloco ):
        self.inserir.inserirApartamento(numero, andar, bloco)
        
        
        
    def vincularMorador(self,numero, andar, bloco, cpf):
        self.buscar.buscarApartamento(numero,andar,bloco)  
        morador = self.buscar.buscarMorador(cpf)
        self.atualizar.atualizarApartamentoMorador(str(morador))
               
                
        
    def vincularVeiculo(self, Veiculo):
                self.Veiculo = Veiculo
                
    def vincularDependente(self, Dependente):
                self.Dependente = Dependente