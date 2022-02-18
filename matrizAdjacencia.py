from grafo import Grafo
from scipy.sparse import dok_matrix


class Matriz(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação com matriz de adjacência"""

    def __init__(self, vertices, peso_negativo=False):
        super().__init__(vertices)
        self.vertices = vertices
        self.peso_negativo = peso_negativo
        # Foi utilizado a matriz esparsa "dok_matrix" implementada na biblioteca scipy
        self.grafo = dok_matrix((self.vertices, self.vertices))
        self.num_arestas = 0
        self.lista_graus = []
        self.tem_peso_negativo = self.peso_negativo

    def imprime_matriz(self):
        """Função que imprime a matriz de adjacência"""
        print(self.grafo)

    def adiciona_aresta(self, u, v, peso):
        """Função que adiciona a aresta no grafo"""
        if (not self.tem_peso) and (peso != 1):
            self.tem_peso = True

        if self.tem_peso_negativo:
            self.grafo[u - 1, v - 1] = peso
            self.num_arestas += 1
        else:
            self.grafo[u - 1, v - 1] = peso
            self.grafo[v - 1, u - 1] = peso
            self.num_arestas += 1

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        if self.tem_peso_negativo:
            self.grafo[u - 1, v - 1] = 0
            self.num_arestas -= 1
        else:
            self.grafo[u - 1, v - 1] = 0
            self.grafo[v - 1, u - 1] = 0
            self.num_arestas -= 1

    def vizinhos_bfs(self, s):
        """Função auxiliar a BFS, que retorna uma lista com os vizinhos a serem percorridos de um vértice s.
        Verifica qual é a implementação para poder criar essa lista."""
        pares_vertices = self.grafo[s].keys()
        return list(map(lambda x: x[1], pares_vertices))

    def vizinhos_dfs(self, s):
        """Função auxiliar a DFS, que retorna uma lista com os vizinhos de um determinado vértice s
        em ordem decrescente. Verifica qual é a implementação para poder criar essa lista."""
        pares_vertices = self.grafo[s].keys()
        return list(map(lambda x: x[1], pares_vertices))[::-1]

    def peso_aresta(self, u, v):
        """Função que retorna o peso de uma aresta entre dois vértices passados"""
        infinito = float("inf")

        if self.grafo[(u, v)] == 0:
            return infinito
        return self.grafo[(u, v)]

    def arestas_grafo(self):
        """Função que retorna uma lista contendo todas as arestas do grafo."""
        return list(self.grafo.keys())
