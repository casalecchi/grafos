class Grafo:

    matriz = False
    lista = False

    def __init__(self, vertices):
        self.vertices =vertices
        self.grafo = []

    def grau_vertice(self, u):
        if self.lista:
            return len(self.grafo[u-1])
        if self.matriz:
            grau = 0
            for i in self.grafo[u - 1]:
                grau += i
            return grau

    def grau_minimo(self):
        for i in range(self.vertices):
            self.l.append(self.grau_vertice(i))
        return min(self.l)

    def grau_maximo(self):
        for i in range(self.vertices):
            self.l.append(self.grau_vertice(i))
        return max(self.l)

    def grau_medio(self):
        for i in range(self.vertices):
            self.l.append(self.grau_vertice(i))
        return sum(self.l) / len(self.l)

    def mediana_de_grau(self):
        mediana = []
        for i in range(self.vertices):
            mediana.append(self.grau_vertice(i))
        mediana = sorted(mediana)
        if len(mediana) % 2 == 0:
            media = (mediana[len(mediana) // 2 - 1] + mediana[(len(mediana) // 2)]) / 2
            return media
        else:
            return mediana[len(mediana) // 2]

    def bfs(self, s):
        """Executa a BFS do vértice passado como argumento e retorna uma tupla com 3 listas -> A ordem dos vértices da BFS,
        uma lista com os níveis de cada vértice na árvore induzida e uma lista com os pais de cada vértice nesse árvore."""
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
        return ordem

    def distancia(self, u, v):
        bfs = self.bfs(u)[0]
        dist = 0
        for elem in bfs[1:]:
            dist += 1
            if elem == v:
                break
        return dist

    def diametro(self):
        diametro = 0
        for i in range(1, self.vertices + 1):
            niveis = self.bfs(i)[1]
            maior_nivel = max(niveis)
            if maior_nivel > diametro:
                diametro = maior_nivel
        return diametro

    def componentes_conexas(self):
        componentes = []
        vertices_adicionados = 0
        vetor_marcacao = [0 for _ in range(self.vertices)]
        while vertices_adicionados != self.vertices:
            for vertice in range(1, self.vertices + 1):
                if vetor_marcacao[vertice - 1] == 0:
                    descobertos = self.bfs(vertice)[0]
                    componentes.append(descobertos)
                    for elem in descobertos:
                        vetor_marcacao[elem - 1] = 1
                        vertices_adicionados += 1

        return componentes

    def info_cc(self):
        cc = self.componentes_conexas()
        num_cc = len(cc)
        # Colocar as componentes em ordem decrescente
        cc.sort(key=len, reverse=True)
        tam_cc = [len(componente) for componente in cc]
        return num_cc, tam_cc, cc