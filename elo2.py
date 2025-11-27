from elo import Elo
#Verifica se o usuário prencheu os dados corretamente
class Elo_02(Elo):
    def solicitacao_processo(self, dados):
        
        if isinstance(dados, dict) and "dados" in dados:
            dados = dados["dados"]
        
        campos_numericos = [
            "idade",
            "altura",
            "salto_horizontal",
            "salto_vertical",
            "flexibilidade",
            "força",
            "velocidade",
            "peso"
        ]

        for campo in campos_numericos:
            try:
                dados[campo] = float(dados[campo])
            except:
                return {
                    "status": "Error",
                    "mensagem": f"O campo '{campo}' deve conter apenas números."
                }
                
        return {"status": "Ok",
                "dados": dados}