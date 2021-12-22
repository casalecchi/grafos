from grafo import Grafo


class Lista(Grafo):
    """Classe com herança da classe Grafo, que usa a implementação de lista de adjacência"""

    def __init__(self, vertices):
        super().__init__(vertices)
        self.lista = True
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)]
        self.arestas = 0
        self.lista_graus = []

    def imprime_lista(self):
        """Função que imprime a matriz de adjacência"""
        for i in range(self.vertices):
            print(str(i+1) + " -> ", end="")
            for v in self.grafo[i]:
                print(str(v+1) + ", ", end="")
            print()

    def adiciona_aresta(self, u, v):
        """Função que adiciona a aresta no grafo"""
        self.grafo[u-1].append(v-1)
        self.grafo[v-1].append(u-1)
        for l in self.grafo:
            l.sort()
        self.arestas += 1

    def remover_aresta(self, u, v):
        """Função que remove a aresta do grafo"""
        self.grafo[u-1].remove(v-1)
        self.grafo[v-1].remove(u-1)
        self.arestas -= 1
