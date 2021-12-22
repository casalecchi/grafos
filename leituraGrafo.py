from matrizAdjacencia import Matriz
from listaAdjacencia import Lista
import sys


def ler_grafo(file, classe):
    """Função que lê o grafo a partir de um arquivo e usa a implementação escolhida"""

    vertices = 0
    arestas = []

    # Abre o arquivo e lê as linhas
    with open(file) as f:
        for line in f.readlines():
            data = line.split()

            for i in range(len(data)):
                # Converte os números
                data[i] = int(data[i])

            if len(data) == 2:
                arestas.append(data)
            elif len(data) == 1:
                vertices = data[0]

    f.close()

    if classe == "matriz":
        grafo = Matriz(vertices)
    elif classe == "lista":
        grafo = Lista(vertices)
    else:
        return "Implementação inválida."

    for aresta in arestas:
        grafo.adiciona_aresta(aresta[0], aresta[1])
    return grafo
