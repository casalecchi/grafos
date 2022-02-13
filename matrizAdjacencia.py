from grafo import Grafo
from scipy.sparse import dok_matrix


class Matriz(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação com matriz de adjacência"""

    def __init__(self, vertices):
        super().__init__(vertices)
        self.matriz = True
        self.vertices = vertices
        # Foi utilizado a matriz esparsa "dok_matrix" implementada na biblioteca scipy
        self.grafo = dok_matrix((self.vertices, self.vertices))
        self.num_arestas = 0
        self.lista_graus = []

    def imprime_matriz(self):
        """Função que imprime a matriz de adjacência"""
        print(self.grafo)

    def adiciona_aresta(self, u, v, peso):
        """Função que adiciona a aresta no grafo"""
        self.grafo[u - 1, v - 1] = peso
        self.grafo[v - 1, u - 1] = peso
        self.num_arestas += 1

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        self.grafo[u - 1, v - 1] = 0
        self.grafo[v - 1, u - 1] = 0
        self.num_arestas -= 1


g = Matriz(5)
g.adiciona_aresta(1, 2, 0.1)
g.adiciona_aresta(1, 5, 1)
g.adiciona_aresta(2, 5, 0.2)
g.adiciona_aresta(3, 5, 5)
g.adiciona_aresta(3, 4, -9.5)
g.adiciona_aresta(4, 5, 2.3)
g.imprime_matriz()
