from grafo import Grafo
from scipy.sparse import dok_matrix


class Matriz(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação com matriz de adjacência"""

    def __init__(self, vertices, peso_negativo):
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


g = Matriz(8, peso_negativo=True)
g.adiciona_aresta(1, 2, 3)
g.adiciona_aresta(1, 6, -1)
g.adiciona_aresta(6, 2, 1)
g.adiciona_aresta(2, 3, 1)
g.adiciona_aresta(6, 3, 4)
g.adiciona_aresta(6, 5, 2)
g.adiciona_aresta(5, 8, 3)
g.adiciona_aresta(8, 7, 1)
g.adiciona_aresta(7, 2, -2)
g.adiciona_aresta(4, 3, -1)
# g.imprime_matriz()

# g = Matriz(8)
# g.adiciona_aresta(1, 2, 1)
# g.adiciona_aresta(2, 3, 1)
# g.adiciona_aresta(3, 5, 1)
# g.adiciona_aresta(5, 6, 1)
# g.adiciona_aresta(5, 7, 1)
# g.adiciona_aresta(1, 4, 1)
# g.adiciona_aresta(2, 4, 1)
# g.adiciona_aresta(4, 8, 1)

# g = Matriz(6)
# g.adiciona_aresta(1, 2, 4)
# g.adiciona_aresta(1, 5, 5)
# g.adiciona_aresta(2, 4, 3)
# g.adiciona_aresta(2, 3, 1)
# g.adiciona_aresta(2, 5, 2)
# g.adiciona_aresta(3, 4, 5)
# g.adiciona_aresta(3, 6, 2)
# g.adiciona_aresta(5, 6, 1)

# g = Matriz(5, peso_negativo=True)
# g.adiciona_aresta(1, 2, 4)
# g.adiciona_aresta(1, 3, 2)
# g.adiciona_aresta(2, 3, 3)
# g.adiciona_aresta(3, 2, 1)
# g.adiciona_aresta(2, 4, 2)
# g.adiciona_aresta(2, 5, 3)
# g.adiciona_aresta(3, 4, 4)
# g.adiciona_aresta(3, 5, 5)
# g.adiciona_aresta(5, 4, -5)
#
print(g.bellman_ford(1))
