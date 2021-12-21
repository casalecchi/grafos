class Grafo:

    matriz = False
    lista = False

    def __init__(self, vertices):
        self.vertices =vertices
        self.grafo = []

    def bfs(self, s):
        vetor_marcacao = [0 for _ in range(self.vertices)]
        descobertos = []
        ordem = []
        nivel = [0 for _ in range(self.vertices)]
        pai = [-1 for _ in range(self.vertices)]
        vetor_marcacao[s - 1] = 1
        descobertos.append(s - 1)
        while descobertos:
            vertice = descobertos.pop(0)
            nivel_atual = nivel[vertice] + 1
            for index, vizinho in enumerate(self.grafo[vertice]):
                if self.matriz:
                    if vizinho == 0:
                        continue
                    if vetor_marcacao[index] == 0:
                        vetor_marcacao[index] = 1
                        descobertos.append(index)
                        nivel[index] = nivel_atual
                        pai[index] = vertice + 1
                if self.lista:
                    if vetor_marcacao[vizinho] == 0:
                        vetor_marcacao[vizinho] = 1
                        descobertos.append(vizinho)
                        nivel[vizinho] = nivel_atual
                        pai[vizinho] = vertice + 1
            ordem.append(vertice + 1)

        return ordem, nivel, pai

    def dfs(self, s):
        vetor_marcacao = [0 for _ in range(self.vertices)]
        pilha = [s - 1]
        ordem = []
        pai = [-1 for _ in range(self.vertices)]
        while len(pilha) != 0:
            vertice = pilha.pop()
            if vetor_marcacao[vertice] == 0:
                vetor_marcacao[vertice] = 1
                ordem.append(vertice + 1)
                for index, vizinho in enumerate(self.grafo[vertice][::-1]):  # vértices descobertos em ordem decrescentes
                    if self.matriz:
                        if vizinho == 0:
                            continue
                        if len(self.grafo[vertice]) - index not in ordem:
                            pai[len(self.grafo[vertice]) - index - 1] = vertice + 1
                        pilha.append(len(self.grafo[vertice]) - index - 1)
                    if self.lista:
                        if vizinho + 1 not in ordem:
                            pai[vizinho] = vertice + 1
                        pilha.append(vizinho)
        return ordem, pai
