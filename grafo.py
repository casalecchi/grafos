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
        if self.lista:
            return len(self.grafo[u-1])
        if self.matriz:
            grau = 0
            for i in self.grafo[u - 1]:
                grau += i
            return grau

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

            # Iteração usando tanto os index como os valores dos vizinhos
            # O index será útil para descobrir que é o vizinho que possui valor 1 na matriz de adjacência.
            # O valor do vizinho será útil para adicioná-lo na fila na lista de adjacência.
            for index, vizinho in enumerate(self.grafo[vertice]):
                if self.matriz:
                    # Caso o valor do vizinho seja 0 -> o vértice não é vizinho do vértice analisado.
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
        # pai = [-1 for _ in range(self.vertices)]
        while len(pilha) != 0:
            vertice = pilha.pop()
            if vetor_marcacao[vertice] == 0:
                # Vértice é marcado e adicionado a ordem que será retornada
                vetor_marcacao[vertice] = 1
                ordem.append(vertice + 1)
                # Assim como no algoritmo da BFS, é utilizado o index como os valores dos vizinhos
                # Percorre os vizinhos em ordem decrescente
                for index, vizinho in enumerate(self.grafo[vertice][::-1]):
                    if self.matriz:
                        if vizinho == 0:
                            continue
                        if vetor_marcacao[len(self.grafo[vertice]) - index - 1] == 0:
                            # pai[len(self.grafo[vertice]) - index - 1] = vertice + 1
                            pilha.append(len(self.grafo[vertice]) - index - 1)
                    if self.lista:
                        if vetor_marcacao[vizinho] == 0:
                            # pai[vizinho] = vertice + 1
                            pilha.append(vizinho)
        return ordem

    def distancia(self, u, v):
        """"Função retorna distância entre dois vértices"""
        nivel = self.bfs(u)[1]
        dist = nivel[v - 1]
        return dist

    def diametro(self):
        """Função retorna o diâmetro do grafo"""
        diametro = 0
        for i in range(1, self.vertices + 1):
            niveis = self.bfs(i)[1]
            maior_nivel = max(niveis)
            if maior_nivel > diametro:
                diametro = maior_nivel
        return diametro

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
