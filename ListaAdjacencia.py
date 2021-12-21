from grafo import Grafo


class Lista(Grafo):

    def __init__(self, vertices):
        self.lista = True
        self.vertices = vertices
        self.grafo = [[] for _ in range(self.vertices)]

    def imprime_lista(self):
        for i in range(self.vertices):
            print(str(i+1) + " -> ", end="")
            for v in self.grafo[i]:
                print(str(v+1) + ", ", end="")
            print()

    def adiciona_aresta(self, u, v):
        self.grafo[u-1].append(v-1)
        self.grafo[v-1].append(u-1)
        for l in self.grafo:
            l.sort()

    def remover_aresta(self, u, v):
        self.grafo[u-1].remove(v-1)
        self.grafo[v-1].remove(u-1)

    def grau_vertice(self, u):
        return len(self.grafo[u-1])


grafo = Lista(8)
grafo.adiciona_aresta(1,3)
grafo.adiciona_aresta(1,4)
grafo.adiciona_aresta(2,4)
grafo.adiciona_aresta(3,8)
grafo.adiciona_aresta(2,3)
grafo.adiciona_aresta(3,4)
grafo.adiciona_aresta(4,7)
grafo.adiciona_aresta(4,6)
grafo.adiciona_aresta(5,7)
grafo.adiciona_aresta(6,5)
grafo.adiciona_aresta(6,7)
print(grafo.lista)
print(grafo.dfs(1))