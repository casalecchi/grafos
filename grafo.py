from math import log2
from random import sample


class Grafo:

    # Atributos que serão utilizados na bfs e na dfs para poder funcionar para ambas as implementações
    matriz = False
    lista = False

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []
        self.lista_graus = []

    def adiciona_aresta(self, u, v):
        """Função que adiciona a aresta no grafo"""
        pass

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        pass

    def grau_vertice(self, u):
        """Função que retorna o grau do vértice passado como argumento."""
        return len(self.grafo[u-1])

    def grau_minimo(self):
        """Função que retorna o grau mínimo do grafo, ele determina o grau
        de todos os vértices e pega o menor valor dessa lista"""
        for i in range(self.vertices):
            self.lista_graus.append(self.grau_vertice(i))
        return min(self.lista_graus)

    def grau_maximo(self):
        """Função que retorna o grau máximo do grafo, ele determina o grau
        de todos os vértices e pega o maior valor dessa lista"""
        for i in range(self.vertices):
            self.lista_graus.append(self.grau_vertice(i))
        return max(self.lista_graus)

    def grau_medio(self):
        """Função que retorna o grau médio do grafo, ele determina o grau
        de todos os vértices, realiza a soma deles e divide pelo número de vértices"""
        for i in range(self.vertices):
            self.lista_graus.append(self.grau_vertice(i))
        return sum(self.lista_graus) / len(self.lista_graus)

    def mediana_de_grau(self):
        """Função que retorna a mediana de grau, ou seja, o grau do vértice
        no meio da ordenação de vértices. Primeiro ela pega os graus dos vértices, ordena
        eles e, sem seguida, caso o número de vértices seja par, pega-se os dois valores
        centrais e tira a média e, caso seja ímpar, pega o valor central da lista"""
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
        """Executa a BFS do vértice passado como o vértice raiz e retorna uma tupla com 3 listas -> A ordem dos vértices
        da BFS, uma lista com os níveis de cada vértice na árvore induzida e uma lista com os pais de cada vértice
        nesse árvore."""
        vetor_marcacao = [0 for _ in range(self.vertices)]
        descobertos = []
        ordem = []

        # Criação das listas que indicarão o nível de cada vértice e o seu respectivo pai
        nivel = [0 for _ in range(self.vertices)]
        pai = [-1 for _ in range(self.vertices)]

        # Marca-se o vértice passado e ele é adicionado na fila de descobertos
        vetor_marcacao[s - 1] = 1
        descobertos.append(s - 1)

        while descobertos:
            vertice = descobertos.pop(0)

            # O nível dos vizinhos que serão analizados vai ser o nível do vértice pai + 1
            nivel_atual = nivel[vertice] + 1

            # Como em cada implementação temos que percorrer por iteráveis diferentes
            # foi usado uma variável booleana para identificar qual implementação está
            # sendo usada
            if self.matriz:
                # Percorre os vizinhos pela matriz esparsa -> retorna um dict_keys com os vizinhos do vértices
                for vizinho in self.grafo[vertice].keys():
                    if vetor_marcacao[vizinho[1]] == 0:
                        vetor_marcacao[vizinho[1]] = 1
                        descobertos.append(vizinho[1])
                        nivel[vizinho[1]] = nivel_atual
                        pai[vizinho[1]] = vertice + 1

            if self.lista:
                for vizinho in self.grafo[vertice]:
                    if vetor_marcacao[vizinho] == 0:
                        vetor_marcacao[vizinho] = 1
                        descobertos.append(vizinho)
                        nivel[vizinho] = nivel_atual
                        pai[vizinho] = vertice + 1

            ordem.append(vertice + 1)

        return ordem, nivel, pai

    def arvore_bfs(self, s, file):
        bfs, nivel, pai = self.bfs(s)
        with open(file, 'w') as f:
            for vertice in range(1, self.vertices + 1):
                linha = f"Vértice {vertice}; Nível = {nivel[vertice - 1]}; Pai = {pai[vertice - 1]} \n"
                f.write(linha)
        f.close()
        print("Arquivo com árvore de busca criado.")

    def dfs(self, s):
        """Executa a DFS do vértice passado como o vértice raiz e
        retorna uma lista com a ordem da DFS."""
        vetor_marcacao = [0 for _ in range(self.vertices)]
        # Cria-se a pilha e o vértice raiz é adicionado.
        pilha = [s - 1]
        ordem = []
        pai = [-1 for _ in range(self.vertices)]
        while len(pilha) != 0:
            vertice = pilha.pop()
            if vetor_marcacao[vertice] == 0:
                # Vértice é marcado e adicionado a ordem que será retornada
                vetor_marcacao[vertice] = 1
                ordem.append(vertice + 1)

                # Assim como no algoritmo da BFS, é utilizado uma verificação para saber qual
                # implementacão está sendo usada.
                if self.matriz:
                    for vizinho in list(self.grafo[vertice].keys())[::-1]:
                        if vetor_marcacao[vizinho[1]] == 0:
                            pai[vizinho[1]] = vertice + 1
                            pilha.append(vizinho[1])

                if self.lista:
                    for vizinho in self.grafo[vertice][::-1]:
                        if vetor_marcacao[vizinho] == 0:
                            pai[vizinho] = vertice + 1
                            pilha.append(vizinho)
        return ordem, pai

    def distancia(self, u, v):
        """"Função retorna distância entre dois vértices"""
        nivel = self.bfs(u)[1]
        dist = nivel[v - 1]
        return dist

    def diametro(self):
        """Função retorna o diâmetro do grafo"""
        diametro = 0

        # Implementação para grafos muito grandes com algoritmo aproximativo
        if self.vertices > 1000000:
            num_vertices = log2(self.vertices)
            vertices_bfs = sample(range(1, self.vertices + 1), num_vertices)
            for v in vertices_bfs:
                niveis = self.bfs(v)[1]
                maior_nivel = max(niveis)
                if maior_nivel > diametro:
                    diametro = maior_nivel
        else:
            for i in range(1, self.vertices + 1):
                niveis = self.bfs(i)[1]
                maior_nivel = max(niveis)
                if maior_nivel > diametro:
                    diametro = maior_nivel
        return diametro

    def pai_bfs(self, raiz, v):
        pai = self.bfs(raiz)[2]
        return pai[v - 1]

    def pai_dfs(self, raiz, v):
        pai = self.dfs(raiz)[1]
        return pai[v - 1]

    def componentes_conexas(self):
        """Função utilizada para achar as componentes conexas do grafo"""
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
        """Função retorna informações sobre as componentes conexas do grafo"""
        cc = self.componentes_conexas()
        num_cc = len(cc)
        # Colocar as componentes em ordem decrescente
        cc.sort(key=len, reverse=True)
        tam_cc = [len(componente) for componente in cc]
        return num_cc, tam_cc, cc
