from matrizAdjacencia import grafo
from listaAdjacencia import grafo


def gerar_saida(file, g):
    with open(file, "w+") as f:
        linha = f"Número de vértices = {str(g.vertices)} \n" \
                f"Número de arestas = {str(g.arestas)} \n" \
                f"Grau mínimo = {str(g.grau_minimo())} \n" \
                f"Grau máximo = {str(g.grau_maximo())} \n" \
                f"Grau médio = {str(g.grau_medio())} \n" \
                f"Mediana de grau = {str(g.mediana_de_grau())} \n"
        f.write(linha)
    f.close()
gerar_saida("saida.txt", grafo)
