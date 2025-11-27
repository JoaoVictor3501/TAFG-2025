from abc import ABC, abstractmethod

class Elo(ABC):
    def __init__(self, nome='Elo', model=None):
        self.proximo = None
        self.nome = nome
        self.model = model
                
    def def_proximo(self, proximo):
        self.proximo = proximo
        return proximo
        
    def comecar(self, dados):
        resultado = self.solicitacao_processo(dados)
        
        if not isinstance(resultado, dict) == resultado.get("status") == "Error":
            return resultado
        
        if self.proximo is not None:
            return self.proximo.comecar(dados)
        else:
            return {"Status": "Ok",
                    "dados": dados}
        
    @abstractmethod
    def solicitacao_processo(self,dados):
        pass                