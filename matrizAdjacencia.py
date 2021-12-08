class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[0] * self.vertices for _ in range(self.vertices)]

    def imprime_matriz(self):
        for i in self.matriz:
            print(i)

    def adiciona_aresta(self, u, v):
        self.matriz[u-1][v-1] = 1
        self.matriz[v-1][u-1] = 1

    def remover_aresta(self, u, v):
        self.matriz[u-1][v-1] = 0
        self.matriz[v-1][u-1] = 0

    def grau_vertice(self, u):
        grau = 0
        for i in self.matriz[u-1]:
            grau += i
        return grau

    def bfs(self, s):
        vetor_marcacao = [0 for _ in range(self.vertices)]
        descobertos = []
        ordem = []
        nivel = [0 for _ in range(self.vertices)]
        pai = [-1 for _ in range(self.vertices)]
        vetor_marcacao[s-1] = 1
        descobertos.append(s-1)
        nivel_atual = 1
        while descobertos:
            vertice = descobertos.pop(0)
            nivel_atual = nivel[vertice] + 1
            for w, vizinho in enumerate(self.matriz[vertice]):
                if vizinho == 0:
                    continue
                if vetor_marcacao[w] == 0:
                    vetor_marcacao[w] = 1
                    descobertos.append(w)
                    nivel[w] = nivel_atual
                    pai[w] = vertice + 1
            ordem.append(vertice + 1)

        return ordem, nivel, pai


# Grafo exercício 5 -> lista 2
grafo = Grafo(9)
grafo.adiciona_aresta(1,2)
grafo.adiciona_aresta(1,6)
grafo.adiciona_aresta(1,4)
grafo.adiciona_aresta(2,3)
grafo.adiciona_aresta(2,3)
grafo.adiciona_aresta(3,4)
grafo.adiciona_aresta(3,8)
grafo.adiciona_aresta(3,5)
grafo.adiciona_aresta(4,5)
grafo.adiciona_aresta(4,6)
grafo.adiciona_aresta(5,6)
grafo.adiciona_aresta(5,8)
grafo.adiciona_aresta(5,7)
grafo.adiciona_aresta(7,9)
grafo.adiciona_aresta(8,9)

grafo.imprime_matriz()
print(grafo.bfs(1))
print(grafo.grau_vertice(3))