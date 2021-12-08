class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.lista = [[] for _ in range(self.vertices)]

    def imprime_lista(self):
        for i in range(self.vertices):
            print(str(i+1) + " -> ", end="")
            for v in self.lista[i]:
                print(str(v+1) + ", ", end="")
            print()

    def adiciona_aresta(self, u, v):
        self.lista[u-1].append(v-1)
        self.lista[v-1].append(u-1)

    def remover_aresta(self, u, v):
        self.lista[u-1].remove(v-1)
        self.lista[v-1].remove(u-1)

    def grau_vertice(self, u):
        return len(self.lista[u-1])




g = Grafo(5)
g.adiciona_aresta(1,2)
g.adiciona_aresta(2,4)
g.adiciona_aresta(3,1)
g.adiciona_aresta(5,2)
g.imprime_lista()
print(g.grau_vertice(2))