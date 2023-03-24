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
    funcaoM2 = FuncaoMorador()
    funcaoA = FuncaoApartamento()
    funcaoB = FuncaoApartamento()
    up = AtualizarCampos()   #teste
   
    #morador = Morador("nome", "cel1", "cel2", "email", "cpf", "rg")
    #apartamento = Apartamento("numero","andar","bloco")
    
    #funcaoM.cadastroMorador(morador.nome,morador.cel1,morador.cel2,morador.email,morador.cpf,morador.rg)
    #funcaoA.cadastroApt(apartamento.numero,apartamento.andar,apartamento.bloco)
    
    #print ("nome:", morador.nome)
    
    #funcaoA.vincularMorador("numero","andar","bloco",morador.cpf)
    
    
    morador2 = Morador("cesar","333","4444","wer@","88888","2222222")
    apt2 = Apartamento("01","1","bl1")
    
    funcaoM2.cadastroMorador(morador2.nome,morador2.cel1,morador2.cel2,morador2.email,morador2.cpf,morador2.rg)
    funcaoB.cadastroApt(apt2.numero,apt2.andar,apt2.bloco)
    funcaoA.vincularMorador("1","1","bl1",morador2.cpf)
    
    #up.atualizarApartamentoMorador(mor2.nome) #teste
    print("morador2", morador2.cpf)
   
    
   
    
    
    
   
    
    
    
    
    
  
   
    
   