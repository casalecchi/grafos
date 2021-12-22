from grafo import Grafo


class Matriz(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação com matriz de adjacência"""

    def __init__(self, vertices):
        super().__init__(vertices)
        self.matriz = True
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]
        self.arestas = 0
        self.lista_graus = []

    def imprime_matriz(self):
        """Função que imprime a matriz de adjacência"""
        for i in self.grafo:
            print(i)

    def adiciona_aresta(self, u, v):
        """Função que adiciona a aresta no grafo"""
        self.grafo[u-1][v-1] = 1
        self.grafo[v-1][u-1] = 1
        self.arestas += 1

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        self.grafo[u-1][v-1] = 0
        self.grafo[v-1][u-1] = 0
        self.arestas -= 1
