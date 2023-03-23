from pctBancoDados.Creates import Tabelas
from pctBancoDados.Inserts import *
from Modelos.Morador import *
from Modelos.Usuario import *
from Modelos.Auntenticacao import *
from pctBancoDados.Searches import *
from Modelos.Data import *
from pctBancoDados.Updates import *
from Modelos.Apartamento import *
from pctBancoDados.Searches import *
from Modelos.FuncApartamento import *
from Modelos.FuncMorador import *
from Modelos.FuncApartamento import FuncaoApartamento





if __name__ == "__main__":
    criarTab = Tabelas()
    criarTab.criar_tabelas()
    funcaoM = FuncaoMorador()
    funcaoA = FuncaoApartamento()
    up = AtualizarCampos()   #teste
   
    morador = Morador("nome", "cel1", "cel2", "email", "cpf", "rg")
    apartamento = Apartamento("numero","andar","bloco")
    
    
    
    funcaoM.cadastroMorador(morador.nome,morador.cel1,morador.cel2,morador.email,morador.cpf,morador.rg)
    funcaoA.cadastroApt(apartamento.numero,apartamento.andar,apartamento.bloco)
    
    
    
    funcaoA.vincularMorador("numero","andar","bloco",morador.cpf)
    
    
    mor2 = Morador("cesar","333","4444","wer@","88888","2222222")
    apt2 = Apartamento("01","1","bl1")
    funcaoM.cadastroMorador(mor2.nome,mor2.cel1,mor2.cel2,mor2.email,mor2.cpf,mor2.rg)
    funcaoA.cadastroApt(apt2.numero,apt2.andar,apt2.bloco)
    funcaoA.vincularMorador("01","1","bl1","cesar")
    
    #up.atualizarApartamentoMorador(mor2.nome) #teste
   
    
   
    
    
    
   
    
    
    
    
    
  
   
    
   