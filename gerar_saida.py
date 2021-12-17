from matrizAdjacencia import Grafo


def gerar_saida(file, g: Grafo):
    with open(file, "r") as f:
        linha = "Número de vértices = " + str(g.vertices) + "\n"
        f.write(linha)
        linha = "Número de arestas = " # implementar contador de arestas na classe do Grafo
        f.write(linha)
        # adicionar grau mínimo, máximo, médio e mediana de grau
        # adicionar informações sore componentes conexas
    f.close()
