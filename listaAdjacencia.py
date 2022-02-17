from grafo import Grafo


class Lista(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação de lista de adjacência"""

    def __init__(self, vertices, arestas, peso_negativo=False):
        super().__init__(vertices)
        self.lista = True
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


# a = [[1, 2, 4], [1, 3, 2], [2, 3, -5], [3, 2, 1], [2, 4, 2], [2, 5, 3], [3, 4, 4], [3, 5, 5], [5, 4, -5]]
# g = Lista(5, a, peso_negativo=True)
#
# print(g.bellman_ford(1))
