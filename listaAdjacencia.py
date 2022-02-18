from grafo import Grafo


class Lista(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação de lista de adjacência"""

    def __init__(self, vertices, arestas, peso_negativo=False):
        super().__init__(vertices)
        self.vertices = vertices
        self.arestas = arestas
        self.peso_negativo = peso_negativo
        self.grafo = [[] for _ in range(self.vertices)]
        self.num_arestas = len(arestas)
        self.lista_graus = []
        self.tem_peso_negativo = self.peso_negativo
        self.adiciona_arestas()

    def imprime_lista(self):
        """Função que imprime a matriz de adjacência"""
        for i in range(self.vertices):
            print(str(i+1) + " -> ", end="")
            for v in self.grafo[i]:
                print(str(v[0]+1) + " peso: " + str(v[1]) + ", ", end="")
            print()

    def adiciona_arestas(self):
        """Função que adiciona a aresta no grafo"""
        if self.tem_peso_negativo:
            self.tem_peso = True
            for aresta in self.arestas:
                self.grafo[aresta[0] - 1].append([aresta[1] - 1, aresta[2]])

        else:
            for aresta in self.arestas:
                self.grafo[aresta[0] - 1].append([aresta[1] - 1, aresta[2]])
                self.grafo[aresta[1] - 1].append([aresta[0] - 1, aresta[2]])

                if (not self.tem_peso) and (aresta[2] != 1):
                    self.tem_peso = True

        # Lista dos vizinhos de cada vértice é ordenada para funcionamento da BFS e DFS
        for lista_vertice in self.grafo:
            lista_vertice.sort()

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        if self.tem_peso_negativo:
            self.grafo[u-1].remove(v-1)
            self.num_arestas -= 1
        else:
            self.grafo[u - 1].remove(v - 1)
            self.grafo[v-1].remove(u-1)
            self.num_arestas -= 1

    def vizinhos_bfs(self, s):
        """Função auxiliar a BFS, que retorna uma lista com os vizinhos a serem percorridos de um vértice s.
        Verifica qual é a implementação para poder criar essa lista."""
        vizinhos = []
        for vizinho in self.grafo[s]:
            vizinhos.append(vizinho[0])
        return vizinhos

    def vizinhos_dfs(self, s):
        """Função auxiliar a DFS, que retorna uma lista com os vizinhos de um determinado vértice s
        em ordem decrescente. Verifica qual é a implementação para poder criar essa lista."""
        vizinhos = []
        for vizinho in self.grafo[s]:
            vizinhos.append(vizinho[0])
        return vizinhos[::-1]

    def peso_aresta(self, u, v):
        """Função que retorna o peso de uma aresta entre dois vértices passados"""
        infinito = float("inf")

        for aresta in self.grafo[u]:
            if aresta[0] == v:
                return aresta[1]
        return infinito

    def arestas_grafo(self):
        """Função que retorna uma lista contendo todas as arestas do grafo."""
        arestas = []
        if self.tem_peso_negativo:
            for aresta in self.arestas:
                arestas.append([aresta[0] - 1, aresta[1] - 1])
        else:
            for aresta in self.arestas:
                arestas.append([aresta[0] - 1, aresta[1] - 1])
                arestas.append([aresta[1] - 1, aresta[0] - 1])
        return arestas
