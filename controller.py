class Controller:
    def __init__(self):
        self.view = None
        self.model = None

    def definir_tela(self,view):
        self.view = view

    def definir_model(self,model):
        self.model = model    

    def processar_teste(self, dados):
        resultado = self.model.start(dados)

        if resultado["status"] == "Error":
            self.view.mostrar_erro(resultado["mensagem"])
            return

        dados_final = resultado["dados"]

        sucesso, msg, dados_salvos = self.model.salvar_teste(dados_final)

        if not sucesso:
            self.view.mostrar_erro(msg)
            return

        self.view.mostrar_resultado(dados_salvos)

    def exibir_resultado(self,dados_final):
        self.view.mostrar_resultado(dados_final)

    def listar_resultado(self):
        listar_testes = self.model.lista_testes()
        self.view.mostrar_lista(listar_testes)

    def excluir_resultado(self, id):
        self.model.excluir_teste(id)
        self.listar_resultado()
    
    def comecar_busca(self,termo):
        resultado = self.model.buscar_testes(termo)
        self.view.mostrar_lista(resultado)
        
