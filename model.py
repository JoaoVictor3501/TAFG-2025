from pymongo import MongoClient
from bson.objectid import ObjectId
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


from elo1 import Elo_01
from elo2 import Elo_02
from elo3 import Elo_03

class Model:
    def __init__(self):
        self.controller = None
        self.old_data = None  # opcional: armazenar histórico

        # conectar ao mongo
        self.client = None
        self.db = None
        self.banco_atleta = None
        
        #Kmeans
        self.scaler = None
        self.kmeans = None
        
        self.conectar_banco()
        self.treinar_kmeans()

        # instanciar elos (passa self ao elo final que precisa salvar)
        self.e0 = Elo_01()
        self.e1 = Elo_02()
        self.e2 = Elo_03()

        # montar a corrente: e0 -> e1 -> e2 -> e3
        self.e0.def_proximo(self.e1).def_proximo(self.e2)

    def conectar_banco(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["Banco_Atleta"]
        self.banco_atleta = self.db["Banco_db"]

    def buscar_testes(self,termo):
        try:
            if not termo:
                return self.lista_testes()
            filtro = {"nome":{"$regex": termo, "$options": "i"}}
            return list(self.banco_atleta.find(filtro))
        except Exception as e:
                print(f"[Model] erro ao realizar a buscar{e}")
                return []
            
    def lista_testes(self):
        return list(self.banco_atleta.find({}))

    def salvar_teste(self, dados_avaliacao):
        try:
            self.banco_atleta.insert_one(dados_avaliacao)
            return True, 'Sucesso ao salvar os dados', dados_avaliacao
        except Exception as e:
            return False, str(e), None
    
    def excluir_teste(self, id_unico):
        self.banco_atleta.delete_one({"_id": ObjectId(id_unico)})    

    def set_controller(self, controller):
        self.controller = controller

    def start(self, dados):
        resultado = self.e0.comecar(dados)
        if resultado["status"] == "Error":
            return resultado

        dados_limpos = resultado["dados"]
        dados_processados = self.aplicar_kmeans(dados_limpos)

        return {
            "status": "OK",
            "dados": dados_processados
        }

    def treinar_kmeans(self):
        dataset = [
            # FUTEBOL (cluster 0)
            [195,245,65,15,95,22,92],
            [188,230,60,17,88,24,85],
            [192,255,72,14,100,20,96],
            [185,220,58,18,90,25,84],
            [198,260,70,12,110,19,93],
            [190,240,63,16,92,23,89],
            [187,225,59,19,85,26,82],
            [196,248,68,13,105,21,97],
            [186,218,57,20,87,24,83],
            [193,238,66,15,98,22,91],

            # FUTSAL (cluster 1)
            [172,185,42,32,60,26,68],
            [168,175,38,35,55,28,64],
            [175,200,46,30,65,27,72],
            [170,178,40,36,57,29,66],
            [166,170,37,38,53,30,62],
            [178,190,45,29,68,26,74],
            [171,180,39,33,59,28,67],
            [174,188,43,31,63,25,70],
            [165,168,35,37,54,29,60],
            [176,192,48,28,70,26,75],]
        
        X = np.array(dataset)

        # normalização
        self.scaler = StandardScaler()
        X_norm = self.scaler.fit_transform(X)
        self.kmeans = KMeans(n_clusters=2, n_init=10)
        self.kmeans.fit(X_norm)
        
        print("\nTREINAMENTO DO KMEANS REALIZADO!")
        print("---------------------------------")

        print("\nLABELS DOS CLUSTERS (0=futebol, 1=futsal):")
        print(self.kmeans.labels_)

        print("\nCENTRÓIDES NORMALIZADOS:")
        print(self.kmeans.cluster_centers_)

        centroids_original = self.scaler.inverse_transform(self.kmeans.cluster_centers_)
        print("\nCENTRÓIDES (NO ESPAÇO ORIGINAL):")
        print(centroids_original)

        print("\nAGRUPAMENTO DAS AMOSTRAS:")
        for i, amostra in enumerate(dataset):
            print(f"Amostra {i}: {amostra}  ->  Cluster {self.kmeans.labels_[i]}")
        
    def aplicar_kmeans(self, dados):       
        
        vetor = [
            dados["altura"],
            dados["salto_horizontal"],
            dados["salto_vertical"],
            dados["flexibilidade"],
            dados["força"],
            dados["velocidade"],
            dados["peso"]
        ]

        X = self.scaler.transform([vetor])
        cluster = int(self.kmeans.predict(X)[0])

        dados["cluster"] = cluster
        dados["modalidade"] = "Futebol" if cluster == 0 else "Futsal"

        return dados    
    


