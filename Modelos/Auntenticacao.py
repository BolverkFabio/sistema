import hashlib
from pctBancoDados.Inserts import InserirDados
from pctBancoDados.Searches import Buscas

class Autenticacao():
    
    
   
    
    def criarNovoLogin(self, nome, login, senha):
        hash = hashlib.md5(senha.encode(encoding='UTF-8'))
        hashSenha = hash.hexdigest()
        dados = InserirDados()
        dados.inserirNovoUsuario(nome,login, hashSenha)
    
      
        
        
    
    def autenticarLogin(self, login, senha):
         hash = hashlib.md5(senha.encode(encoding='UTF-8'))
         hashSenha = hash.hexdigest()
         dados = Buscas()
         dados.Autenticacao(login, hashSenha)        
        
        
    
   
       
    
    
        
    
        
        
    
      