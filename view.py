import tkinter as tk
from tkinter import ttk
import sys
from tkinter import messagebox

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x400")

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.menu_frame = tk.Frame(self.container)
        self.insercao_frame = tk.Frame(self.container)
        self.resultado_frame = tk.Frame(self.container)
        self.lista_frame = tk.Frame(self.container)
        
        self.menu_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.insercao_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.resultado_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.lista_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.tela_1_inicio()
        self.tela_2_teste()
        self.tela_3_lista_testes()
        self.tela_menu()

    def tela_1_inicio(self):
        titulo = tk.Label(self.menu_frame, text="MENU", font=("Arial", 14, "bold"))
        titulo.pack(pady=10)

        self.novo_teste = tk.Button(self.menu_frame, text='Novo Teste', command=self.tela_inserir_dados)
        self.novo_teste.pack(pady=10)

        self.listar_testes = tk.Button(self.menu_frame, text='Listar Atletas', command=lambda: self.controller.listar_resultado())
        self.listar_testes.pack(pady=10)

        self.sair = tk.Button(self.menu_frame, text="Sair", command=sys.exit)
        self.sair.pack(pady=10)

    def tela_2_teste(self):
        titulo_pag_2 = tk.Label(self.insercao_frame, text="Tela de Novo Teste", font=("Arial", 14, "bold"))
        titulo_pag_2.grid(row=0, column=0,columnspan=2,pady=5,padx=10)
        
        nome_atleta = tk.Label(self.insercao_frame, text="Nome")
        nome_atleta.grid(row=1, column=0, padx=10, pady=5)
        
        self.nome_entrada = tk.Entry(self.insercao_frame, width=30)
        self.nome_entrada.grid(row=1, column=1, padx=10, pady=5)
        
        idade_atleta = tk.Label(self.insercao_frame, text="Idade")
        idade_atleta.grid(row=2, column=0, padx=10, pady=5)
        
        self.idade_entrada = tk.Entry(self.insercao_frame, width=12)
        self.idade_entrada.grid(row=2, column=1, padx=10, pady=5)
        
        altura_atleta = tk.Label(self.insercao_frame, text="Altura")
        altura_atleta.grid(row=3, column=0, padx=10, pady=5)
        
        self.altura_entrada = tk.Entry(self.insercao_frame, width=30)
        self.altura_entrada.grid(row=3, column=1, padx=10, pady=5)
                
        salto_horizontal = tk.Label(self.insercao_frame, text="Salto Horizontal")
        salto_horizontal.grid(row=4, column=0, padx=10, pady=5)
        
        self.salto_h_entrada = tk.Entry(self.insercao_frame, width=25)
        self.salto_h_entrada.grid(row=4, column=1, padx=10, pady=5)
        
        salto_vertical = tk.Label(self.insercao_frame, text="Salto Vertical")
        salto_vertical.grid(row=5, column=0, padx=10, pady=5)
        
        self.salto_v_entrada = tk.Entry(self.insercao_frame, width=25)
        self.salto_v_entrada.grid(row=5, column=1, padx=10, pady=5)
        
        flexibilidade = tk.Label(self.insercao_frame, text="Flexibilidade")
        flexibilidade.grid(row=6, column=0, padx=10, pady=5)
        
        self.flexibilidade_entrada = tk.Entry(self.insercao_frame, width=25)
        self.flexibilidade_entrada.grid(row=6, column=1, padx=10, pady=5)
        
        forca = tk.Label(self.insercao_frame, text="Força")
        forca.grid(row=7, column=0, padx=10, pady=5)
        
        self.forca_entrada = tk.Entry(self.insercao_frame, width=25)
        self.forca_entrada.grid(row=7, column=1, padx=10, pady=5)
        self.forca_entrada.insert(0, "Digite a Força")
        
        velocidade = tk.Label(self.insercao_frame, text="Velocidade")
        velocidade.grid(row=8, column=0, padx=10, pady=5)
        
        self.velocidade_entrada = tk.Entry(self.insercao_frame, width=25)
        self.velocidade_entrada.grid(row=8, column=1, padx=10, pady=5)
        
        peso = tk.Label(self.insercao_frame, text="Digite o Peso")
        peso.grid(row=9, column=0, padx=10, pady=5)
        
        self.peso_entrada = tk.Entry(self.insercao_frame, width=25)
        self.peso_entrada.grid(row=9, column=1, padx=10, pady=5)
        
        voltar = tk.Button(self.insercao_frame, text="Voltar para Tela Inicial", command=self.tela_menu)
        voltar.grid(row=10, column=0,pady=10,padx=10)

        processar = tk.Button(self.insercao_frame, text="Processar",command=self.processo)
        processar.grid(row=10, column=1,pady=10,padx=10)

    def tela_resultado(self):
        for widget in self.resultado_frame.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.resultado_frame, text="Resultado do Processamento", font=("Arial", 14, "bold")
        )
        titulo.pack(pady=10)

        self.resultado_label = tk.Label(self.resultado_frame, text="", font=("Arial", 12))
        self.resultado_label.pack(pady=10)

        voltar_btn = tk.Button(
            self.resultado_frame, text="Voltar ao Menu", command=self.tela_menu
        )
        voltar_btn.pack(pady=10)
        
    def mostrar_resultado(self,dados):
        self.tela_resultado()
        texto = "DADOS PROCESSADOS:\n\n"
        for chave, valor in dados.items():
            texto += f"{chave.capitalize()}: {valor}\n"

        if hasattr(self, "resultado_label"):
            self.resultado_label.config(text=texto)

        self.resultado_frame.tkraise()

    def tela_3_lista_testes(self):
        frame_controles = tk.Frame(self.lista_frame)
        frame_controles.pack(pady=10, padx=10, fill='x')

        titulo = tk.Label(frame_controles, text="Lista de Testes Realizados", font=("Arial", 14, "bold"))
        titulo.pack(pady=(0, 10))
        
        frame_busca = tk.Frame(frame_controles)
        frame_busca.pack(fill='x', pady=5)
        
        buscar = tk.Label(frame_busca, text="Buscar Atleta:")
        buscar.pack(side=tk.LEFT, padx=(0, 5))
        
        self.entrada_busca = tk.Entry(frame_busca)
        self.entrada_busca.pack(side=tk.LEFT, fill='x', expand=True, padx=5)
        
        btn_buscar = tk.Button(frame_busca, text="Buscar", command=self.buscar)
        btn_buscar.pack(side=tk.LEFT)
        
        treeview_container = tk.Frame(self.lista_frame)
        treeview_container.pack(pady=5, padx=10, fill="both", expand=True)

        scroll = tk.Scrollbar(treeview_container)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        colunas = ('nome', 'idade', 'modalidade')
        
        self.tree_lista = ttk.Treeview(treeview_container, columns=colunas, show='headings', yscrollcommand=scroll.set)
        
        self.tree_lista.heading('nome', text='Nome')
        self.tree_lista.heading('idade', text='Idade')
        self.tree_lista.heading('modalidade', text='Modalidade') 

        self.tree_lista.column('nome', width=150)
        self.tree_lista.column('idade', width=40)
        self.tree_lista.column('modalidade', width=100)

        self.tree_lista.pack(side=tk.LEFT, fill="both", expand=True)
        scroll.config(command=self.tree_lista.yview)
        
        frame_botoes_acao = tk.Frame(self.lista_frame)
        frame_botoes_acao.pack(pady=10)

        btn_excluir = tk.Button(frame_botoes_acao, text="Excluir Selecionado", command=self.excluir_atleta)
        btn_excluir.pack(side=tk.LEFT, padx=5)

        btn_voltar = tk.Button(frame_botoes_acao, text="Voltar ao Menu", command=self.tela_menu)
        btn_voltar.pack(side=tk.LEFT, pady=5)
        
    def tela_menu(self):
        self.menu_frame.tkraise()       

    def tela_inserir_dados(self):
        self.nome_entrada.delete(0, tk.END)
        self.idade_entrada.delete(0, tk.END)
        self.altura_entrada.delete(0, tk.END)
        self.salto_h_entrada.delete(0, tk.END)
        self.salto_v_entrada.delete(0, tk.END)
        self.flexibilidade_entrada.delete(0, tk.END)
        self.forca_entrada.delete(0, tk.END)
        self.velocidade_entrada.delete(0, tk.END)
        self.peso_entrada.delete(0, tk.END)
        self.insercao_frame.tkraise()

    def mostrar_lista(self, lista_de_testes):
        for i in self.tree_lista.get_children():
            self.tree_lista.delete(i)
        
        if lista_de_testes:
            for teste in lista_de_testes:
                self.tree_lista.insert('', 'end',iid=str(teste['_id']), values=(
                    teste.get('nome', 'N/A'), 
                    teste.get('idade', 'N/A'),
                    teste.get('modalidade', 'N/A') 
                )) 
        
        self.lista_frame.tkraise()

    def excluir_atleta(self):
        selecionado = self.tree_lista.focus()
        if not selecionado:
            messagebox.showerror("Erro", "Nenhum atléta foi selecionado para excluir!")   
            return 
                 
        _id = selecionado  
        self.controller.excluir_resultado(_id)

    def buscar(self):
        termo = self.entrada_busca.get()
        self.controller.comecar_busca(termo)

    def iniciar(self):
        self.root.mainloop()
    
    def definir_controller(self,controller):
        self.controller = controller
        
    def processo(self):
        nome = self.nome_entrada.get()
        idade = self.idade_entrada.get()
        salto_horizontal = self.salto_h_entrada.get()
        salto_vertical = self.salto_v_entrada.get()
        flexibilidade = self.flexibilidade_entrada.get()
        forca = self.forca_entrada.get()
        velocidade = self.velocidade_entrada.get()
        peso = self.peso_entrada.get()
        altura = self.altura_entrada.get()
        
        dados = {'nome': nome,
                 'idade':idade,
                 'altura': altura,
                 'salto_horizontal': salto_horizontal,
                 'salto_vertical': salto_vertical, 
                 'flexibilidade': flexibilidade,
                 'força': forca,
                 'velocidade': velocidade,
                 'peso': peso}
        
        self.controller.processar_teste(dados)                
        
    def mostrar_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)

    def mostrar_sucesso(self, mensagem):
        messagebox.showinfo("Sucesso", mensagem)

