from matrizAdjacencia import Matriz
from listaAdjacencia import Lista
from memory_profiler import profile


@profile
def ler_grafo(file, classe):
    """Função que lê o grafo a partir de um arquivo e usa a implementação escolhida"""

    arestas = []

    # Abre o arquivo e lê as linhas
    with open(file) as f:
        vertices = int(f.readline())
        for line in f.readlines():
            data = line.split()

            for i in range(len(data)):
                # Converte os números
                data[i] = int(data[i])

            arestas.append(data)

    f.close()

    if classe == "matriz":
        grafo = Matriz(vertices)
        for aresta in arestas:
            grafo.adiciona_aresta(aresta[0], aresta[1])
    elif classe == "lista":
        grafo = Lista(vertices, arestas)
    else:
        return "Implementação inválida."

    return grafo
