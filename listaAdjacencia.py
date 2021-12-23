from grafo import Grafo


class Lista(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação de lista de adjacência"""

    def __init__(self, vertices, arestas):
        super().__init__(vertices)
        self.lista = True
        self.vertices = vertices
        self.arestas = arestas
        self.grafo = [[] for _ in range(self.vertices)]
        self.num_arestas = len(arestas)
        self.lista_graus = []
        self.adiciona_arestas()

    def imprime_lista(self):
        """Função que imprime a matriz de adjacência"""
        for i in range(self.vertices):
            print(str(i+1) + " -> ", end="")
            for v in self.grafo[i]:
                print(str(v+1) + ", ", end="")
            print()

    def adiciona_arestas(self):
        """Função que adiciona a aresta no grafo"""
        for aresta in self.arestas:
            self.grafo[aresta[0] - 1].append(aresta[1] - 1)
            self.grafo[aresta[1] - 1].append(aresta[0] - 1)

        for lista_vertice in self.grafo:
            lista_vertice.sort()

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        self.grafo[u-1].remove(v-1)
        self.grafo[v-1].remove(u-1)
        self.num_arestas -= 1
