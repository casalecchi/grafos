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
        if (not self.tem_peso) and (peso != 1):
            self.tem_peso = True
        if self.tem_peso and (peso < 0):
            self.tem_peso_negativo = True

        self.grafo[u - 1, v - 1] = peso
        self.grafo[v - 1, u - 1] = peso
        self.num_arestas += 1

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        self.grafo[u - 1, v - 1] = 0
        self.grafo[v - 1, u - 1] = 0
        self.num_arestas -= 1


# g = Matriz(7)
# g.adiciona_aresta(1, 2, 1)
# g.adiciona_aresta(1, 5, 2)
# g.adiciona_aresta(1, 4, 4)
# g.adiciona_aresta(2, 4, 2)
# g.adiciona_aresta(2, 3, 4)
# g.adiciona_aresta(5, 4, 2)
# g.adiciona_aresta(5, 6, 3)
# g.adiciona_aresta(4, 6, 2)
# g.adiciona_aresta(3, 7, 2)
# g.adiciona_aresta(6, 7, 3)
# g.adiciona_aresta(4, 3, 1)
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

g = Matriz(4)
g.adiciona_aresta(1, 2, 3)
g.adiciona_aresta(1, 3, 4)
g.adiciona_aresta(2, 3, -2)
g.adiciona_aresta(2, 4, 5)
g.adiciona_aresta(3, 4, -1)

print(g.bellman_ford(1))
