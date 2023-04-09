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
    s = Buscas()
   
    a = Morador("santos","555", "666","es@","6666","444")
    a2 = FuncaoMorador()
    a2.cadastroMorador(a.nome,a.cel1,a.cel2,a.email,a.cpf,a.rg)
    s.buscarMorador(a.cpf)
    
    #s.buscarMorador("9999")
    
    
    
    
    

   
   
   
   
   
    
   
    
    
    
   
    
    
    
    
    
  
   
    
   