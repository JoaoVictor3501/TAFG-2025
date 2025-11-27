from elo import Elo
#Verifica se todos os campos foram preenchidos
class Elo_01(Elo):
    def solicitacao_processo(self, dados):
        for c, v in dados.items():
            if v is None or str(v).strip() == "":
                return {
                    "status": "Error",
                    "mensagem": f"O campo {c} está vazio"
                }

        return {
            "status": "Ok",
            "dados": dados
        }
        