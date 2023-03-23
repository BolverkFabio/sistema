from pctBancoDados.Inserts import InserirDados


class FuncaoUsuario:
    
    def criarUsuario(self, nome):
        dados = InserirDados()
        dados.inserirNovoUsuario(nome)