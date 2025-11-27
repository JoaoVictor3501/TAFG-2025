from elo import Elo
import unicodedata
#Limpa o nome do usuário
class Elo_03(Elo):
    def __init__(self, nome='Elo_03', model=None):
        super().__init__(nome, model=model)
        
    def solicitacao_processo(self, dados):
        if isinstance(dados, dict) and "dados" in dados:
            dados = dados["dados"] 
        
        if "nome" not in dados:
            return {
                "status": "Error",
                "mensagem": "Campo 'nome' não encontrado nos dados."
            }

        nome = str(dados["nome"]).strip()
        nome = " ".join(nome.split()) 

        nome = nome.strip()

        nome = " ".join(nome.split())

        nome = nome.lower()

        nome = ''.join(
            c for c in unicodedata.normalize('NFD', nome)
            if unicodedata.category(c) != 'Mn'
        )
        dados["nome"] = nome

        return {"status": "Ok", "dados": dados}