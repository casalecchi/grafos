from grafo import Grafo


class Lista(Grafo):
    arestas = 0
    l = []
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
        Grafo.arestas += 1

    def remover_aresta(self, u, v):
        self.grafo[u-1].remove(v-1)
        self.grafo[v-1].remove(u-1)
        Grafo.arestas -= 1

    def grau_vertice(self, u):
        return len(self.grafo[u-1])
    
    def grau_minimo(self):
        for i in range(self.vertices):
            Grafo.l.append(Grafo.grau_vertice(self, i))
        return min(Grafo.l)    

    def grau_maximo(self):
        for i in range(self.vertices):
            Grafo.l.append(Grafo.grau_vertice(self, i))
        return max(Grafo.l)
    
    def grau_medio(self):
        for i in range(self.vertices):
            Grafo.l.append(Grafo.grau_vertice(self, i))
        return sum(Grafo.l)/len(Grafo.l)
    
    def mediana_de_grau(self):
        mediana = []
        for i in range(self.vertices):
            mediana.append(Grafo.grau_vertice(self, i))
        mediana = sorted(mediana)
        if len(mediana) % 2 == 0:
            media = (mediana[len(mediana) // 2 - 1] + mediana[(len(mediana) // 2)]) / 2
            return media
        else:
            return mediana[len(mediana) // 2]
        
        
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
print("A DFS do grafo começando no vértice 1 é ", grafo.dfs(1))
print("O grau do vértice 3 é", grafo.grau_vertice(3))
print("O grafo possui", grafo.arestas, "arestas.")
print("O grafo possui", grafo.vertices, "vertices.")
print("O grau mínimo do grafo é", grafo.grau_minimo())
print("O grau máximo do grafo é", grafo.grau_maximo())
print("O grau médio do grafo é", grafo.grau_medio())
print("A mediana de grau do grafo é", grafo.mediana_de_grau())

