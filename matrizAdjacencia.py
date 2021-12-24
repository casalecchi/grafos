from grafo import Grafo
from scipy.sparse import dok_matrix


class Matriz(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação com matriz de adjacência"""

    def __init__(self, vertices):
        super().__init__(vertices)
        self.matriz = True
        self.vertices = vertices
        self.grafo = dok_matrix((self.vertices, self.vertices))
        self.num_arestas = 0
        self.lista_graus = []

    def imprime_matriz(self):
        """Função que imprime a matriz de adjacência"""
        print(self.grafo.toarray())

    def adiciona_aresta(self, u, v):
        """Função que adiciona a aresta no grafo"""
        self.grafo[u - 1, v - 1] = 1
        self.grafo[v - 1, u - 1] = 1
        self.num_arestas += 1

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        self.grafo[u - 1, v - 1] = 0
        self.grafo[v - 1, u - 1] = 0
        self.num_arestas -= 1
