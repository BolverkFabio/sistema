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
   
    fabio = Morador("fabio","1111","2222","fab@","3333","4444")
    aptFb = Apartamento("01","4","BL01")
    
    fb = FuncaoMorador()
    fbApt = FuncaoApartamento()
    
    #fb.cadastroMorador(fabio.nome,fabio.cel1,fabio.cel2,fabio.email,fabio.cpf,fabio.rg)
    #fbApt.cadastroApt(aptFb.numero,aptFb.andar,aptFb.bloco)
    
    #fbApt.vincularMorador(aptFb.numero,aptFb.andar,aptFb.bloco,fabio.cpf)
    
    cesar = Morador("cesar","7777","8888","ces@","9999","666")
    aptCs = Apartamento("02","8","BL09")
    
    cs = FuncaoMorador()
    csApt = FuncaoApartamento()
    
    cs.cadastroMorador(cesar.nome,cesar.cel1,cesar.cel2,cesar.email,cesar.cpf,cesar.rg)
    csApt.cadastroApt(aptCs.numero,aptCs.andar,aptCs.bloco)
    
    csApt.vincularMorador(aptCs.numero,aptCs.andar,aptCs.bloco,cesar.cpf)
   
   
   
   
   
    
   
    
    
    
   
    
    
    
    
    
  
   
    
   