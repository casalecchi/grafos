from grafo import Grafo


class Matriz(Grafo):

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

    def remover_aresta(self, u, v):
        self.grafo[u-1][v-1] = 0
        self.grafo[v-1][u-1] = 0

    def grau_vertice(self, u):
        grau = 0
        for i in self.grafo[u-1]:
            grau += i
        return grau

    def dfs(self, s):
        vetor_marcacao = [0 for _ in range(self.vertices)]
        pilha = [s - 1]
        ordem = []
        while len(pilha) != 0:
            vertice = pilha.pop()
            if vetor_marcacao[vertice] == 0:
                vetor_marcacao[vertice] = 1
                ordem.append(vertice + 1)
                for i, vizinho in enumerate(self.matriz[vertice][::-1]):  # vértices descobertos em ordem decrescentes
                    if vizinho == 0:
                        continue
                    pilha.append(len(self.matriz[vertice]) - i - 1)
        return ordem


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
print(grafo.bfs(1))
# print(grafo.grau_vertice(3))
