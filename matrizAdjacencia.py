from grafo import Grafo


class Matriz(Grafo):

    arestas = 0
    l = []

    def __init__(self, vertices):
        self.matriz = True
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

    def imprime_matriz(self):
        for i in self.grafo:
            print(i)

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1
        self.grafo[v-1][u-1] = 1
        self.arestas += 1

    def remover_aresta(self, u, v):
        self.grafo[u-1][v-1] = 0
        self.grafo[v-1][u-1] = 0
        self.arestas -= 1


# Grafo slide aula dfs
grafo = Matriz(8)
grafo.adiciona_aresta(1,3)
grafo.adiciona_aresta(1,4)
grafo.adiciona_aresta(2,4)
grafo.adiciona_aresta(3,8)
grafo.adiciona_aresta(2,3)
grafo.adiciona_aresta(3,4)
grafo.adiciona_aresta(4,7)
grafo.adiciona_aresta(4,6)
grafo.adiciona_aresta(5,7)
grafo.adiciona_aresta(6,5)
grafo.adiciona_aresta(6,7)
# grafo.imprime_matriz()
# print(grafo.grau_vertice(3))
print("A DFS do grafo começando no vértice 1 é ", grafo.dfs(1))
print("O grau do vértice 3 é", grafo.grau_vertice(3))
print("O grafo possui", grafo.arestas, "arestas.")
print("O grafo possui", grafo.vertices, "vertices.")
print("O grau mínimo do grafo é", grafo.grau_minimo())
print("O grau máximo do grafo é", grafo.grau_maximo())
print("O grau médio do grafo é", grafo.grau_medio())
print("A mediana de grau do grafo é", grafo.mediana_de_grau())
