from matrizAdjacencia import Grafo
import sys

def ler_grafo(file):
    vertices = 0
    arestas = []
    with open(file) as f:
        for line in f.readlines():
            data = line.split()
            for i in range(len(data)):
                data[i] = int(data[i])
            if len(data) == 2:
                arestas.append(data)
            elif len(data) == 1:
                vertices = data[0]
    f.close()
    g = Grafo(vertices)
    for aresta in arestas:
        g.adiciona_aresta(aresta[0], aresta[1])
    return g


arquivo = sys.argv[1]
grafo = ler_grafo(arquivo)
grafo.imprime_matriz()
