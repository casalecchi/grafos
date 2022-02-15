from math import log10
from random import sample
from heapq import heappop, heappush


class Grafo:

    # Atributos que serão utilizados na bfs e na dfs para poder funcionar para ambas as implementações
    matriz = False
    lista = False

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []
        self.lista_graus = []
        self.tem_peso = False
        self.tem_peso_negativo = False

    def adiciona_aresta(self, u, v):
        """Função que adiciona a aresta no grafo"""
        pass

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        pass

    def grau_vertice(self, u):
        """Função que retorna o grau do vértice passado como argumento."""
        return len(self.grafo[u-1])

    def calcula_lista_graus(self):
        """Função que calcula a lista com os graus de cada vértice"""
        for vertice in range(self.vertices):
            self.lista_graus.append(self.grau_vertice(vertice))

    def grau_minimo(self):
        """Função que retorna o grau mínimo do grafo, ele determina o grau
        de todos os vértices e pega o menor valor dessa lista"""
        if not self.lista_graus:
            self.calcula_lista_graus()
        return min(self.lista_graus)

    def grau_maximo(self):
        """Função que retorna o grau máximo do grafo, ele determina o grau
        de todos os vértices e pega o maior valor dessa lista"""
        if not self.lista_graus:
            self.calcula_lista_graus()
        return max(self.lista_graus)

    def grau_medio(self):
        """Função que retorna o grau médio do grafo, ele determina o grau
        de todos os vértices, realiza a soma deles e divide pelo número de vértices"""
        if not self.lista_graus:
            self.calcula_lista_graus()
        return sum(self.lista_graus) / len(self.lista_graus)

    def mediana_de_grau(self):
        """Função que retorna a mediana de grau, ou seja, o grau do vértice
        no meio da ordenação de vértices. Primeiro ela pega os graus dos vértices, ordena
        eles e, sem seguida, caso o número de vértices seja par, pega-se os dois valores
        centrais e tira a média e, caso seja ímpar, pega o valor central da lista"""
        if not self.lista_graus:
            self.calcula_lista_graus()
        mediana = sorted(self.lista_graus)
        if len(mediana) % 2 == 0:
            media = (mediana[len(mediana) // 2 - 1] + mediana[(len(mediana) // 2)]) / 2
            return media
        else:
            return mediana[len(mediana) // 2]

    def vizinhos_bfs(self, s):
        """Função auxiliar a BFS, que retorna uma lista com os vizinhos a serem percorridos de um vértice s.
        Verifica qual é a implementação para poder criar essa lista."""
        if self.lista:
            vizinhos = []
            for vizinho in self.grafo[s]:
                vizinhos.append(vizinho[0])
            return vizinhos
        elif self.matriz:
            pares_vertices = self.grafo[s].keys()
            return list(map(lambda x: x[1], pares_vertices))

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
            # foi usado uma função auxiliar "vizinhos_bfs" em que retorna uma lista com os
            # vizinhos do vértice passado
            for vizinho in self.vizinhos_bfs(vertice):
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

    def vizinhos_dfs(self, s):
        """Função auxiliar a DFS, que retorna uma lista com os vizinhos de um determinado vértice s
        em ordem decrescente. Verifica qual é a implementação para poder criar essa lista."""
        if self.lista:
            vizinhos = []
            for vizinho in self.grafo[s]:
                vizinhos.append(vizinho[0])
            return vizinhos[::-1]
        elif self.matriz:
            pares_vertices = self.grafo[s].keys()
            return list(map(lambda x: x[1], pares_vertices))[::-1]

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

                # Assim como no algoritmo da BFS, é utilizado uma função auxiliar para obter uma lista
                # dos vizinhos.
                for vizinho in self.vizinhos_dfs(vertice):
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
            num_vertices = log10(2) * self.vertices
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
        """Função utilizada para retornar o pai de um vértice v, dado que a BFS foi realizada
        em um vértice raiz."""
        pai = self.bfs(raiz)[2]
        return pai[v - 1]

    def pai_dfs(self, raiz, v):
        """Função utilizada para retornar o pai de um vértice v, dado que a DFS foi realizada
        em um vértice raiz."""
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

    # Implementação da Parte 2 do Trabalho - GRAFOS COM PESOS

    '''
    1) Implementar a distância entre dois vértices, assim como indicar o caminho.
    2) Se o grafo não possuir peso, usar a buca em largura.
    3) Se possuir pesos não negativos -> usar Dijkstra.
    4) Se possuir pesos negativos -> usar Floyd-Warshall ou Bellman-Ford.
    5) Se possuir pesos negativos -> detectar ciclos negativos (casos em que a distância não está definida).
    6) Além de calcular a distância e caminho mínimo entre um par de vértices, fazer isso com um vértice para
    todos os outros. 
    7) Encontrar uma árvore geradora mínima do grafo. 
    8) MST deve ser escrita em um arquivo.    
    '''

    def peso_aresta(self, u, v):
        infinito = float("inf")
        if self.lista:
            for aresta in self.grafo[u]:
                if aresta[0] == v:
                    return aresta[1]
            return infinito
        if self.matriz:
            if self.grafo[(u, v)] == 0:
                return infinito
            return self.grafo[(u, v)]

    def dijkstra(self, s):
        infinito = float('inf')
        distancia = [infinito for _ in range(self.vertices)]
        descobertos = [False for _ in range(self.vertices)]
        pai = [-1 for _ in range(self.vertices)]
        distancia[s - 1] = 0
        fila = [(0, s - 1)]

        while len(fila) > 0:
            peso, u = heappop(fila)

            if descobertos[u]:
                continue

            descobertos[u] = True

            for vizinho in self.vizinhos_bfs(u):
                peso_uv = self.peso_aresta(u, vizinho)
                if distancia[vizinho] > distancia[u] + peso_uv:
                    distancia[vizinho] = distancia[u] + peso_uv
                    pai[vizinho] = u + 1
                    heappush(fila, (distancia[vizinho], vizinho))

        return distancia, pai

    def arestas_grafo(self):
        if self.lista:
            arestas = []
            for aresta in self.arestas:
                arestas.append([aresta[0] - 1, aresta[1] - 1])
                arestas.append([aresta[1] - 1, aresta[0] - 1])
            return arestas
        if self.matriz:
            return list(self.grafo.keys())

    def bellman_ford(self, s):
        infinito = float('inf')
        distancias = [infinito for _ in range(self.vertices)]
        distancias[s - 1] = 0
        pai = [-1 for _ in range(self.vertices)]

        for _ in range(self.vertices - 1):
            modificou = False
            for v, w in self.arestas_grafo():
                peso = self.peso_aresta(v, w)
                if distancias[v] != infinito and distancias[v] + peso < distancias[w]:
                    distancias[w] = distancias[v] + peso
                    modificou = True
                    pai[w] = v + 1
            if not modificou:
                break

        # Detecção de ciclos negativos
        # for a, b in self.arestas_grafo():
        #     peso = self.peso_aresta(a, b)
        #     if distancias[a] != infinito and distancias[a] + peso < distancias[b]:
        #         print("Grafo contém um ciclo negativo, distâncias não estão definidas.")
        #         return 0, 0

        return distancias, pai

    def buscar(self, s):
        """Função que faz uma buscar a partir do vértice passado. Retorna os vetores de distância e pai."""
        if self.tem_peso_negativo:
            return self.bellman_ford(s)
        if self.tem_peso:
            return self.dijkstra(s)
        else:
            return self.bfs(s)[1:]

    def dist_caminho_min(self, u):
        distancias, pai = self.buscar(u)

        # Caso onde o grafo possui um ciclo negativo e não terá informações
        if distancias == 0 and pai == 0:
            return

        dist_cam = []

        for i in range(1, self.vertices + 1):
            caminho = [i]
            vertice = i

            while vertice != -1:
                vertice = pai[vertice - 1]
                caminho.append(vertice)

            dist_cam.append((distancias[i - 1], caminho[::-1][1:]))
        return dist_cam

    def dist_caminho_par(self, u, v):
        return self.dist_caminho_min(u)[v - 1]

    def gerar_mst(self, s):

        # Implementação do Algoritmo Prim
        infinito = float('inf')
        custo = [infinito for _ in range(self.vertices)]
        custo[s - 1] = 0
        fila = [(0, s - 1)]
        descobertos = [False for _ in range(self.vertices)]
        pai = [-1 for _ in range(self.vertices)]

        while len(fila) > 0:
            peso, v = heappop(fila)

            if descobertos[v]:
                continue

            descobertos[v] = True

            for w in self.vizinhos_bfs(v):
                peso = self.peso_aresta(v, w)
                if not descobertos[w] and custo[w] > peso:
                    custo[w] = peso
                    pai[w] = v + 1
                    heappush(fila, (peso, w))

        # Preparar para formatação do arquivo .txt com a árvore

        print(f"O custo total da MST é = {sum(custo)}")

        n_vertice = self.vertices
        arestas = []
        vertices = [i for i in range(self.vertices)]

        while len(vertices) != 0:
            vertice = vertices.pop()
            if pai[vertice] != -1:
                arestas.append([vertice + 1, pai[vertice], self.peso_aresta(vertice, pai[vertice] - 1)])

        with open("mst.txt", "w") as f:
            f.write(str(n_vertice) + "\n")
            for aresta in arestas:
                f.write(f"{aresta[0]} {aresta[1]} {aresta[2]}\n")

        f.close()

        return custo, pai, [n_vertice, arestas]
