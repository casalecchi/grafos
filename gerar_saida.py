def gerar_saida(file, g):
    """Função para escrever em um arquivo de texto o número de vértices, o número de arestas, o grau mínimo, o grau máximo, o grau médio, a mediana de grau
    e os detalhes das componentes conexas"""
    with open(file, "w+") as f:
        linha = f"Número de vértices = {str(g.vertices)} \n" \
                f"Número de arestas = {str(g.arestas)} \n" \
                f"Grau mínimo = {str(g.grau_minimo())} \n" \
                f"Grau máximo = {str(g.grau_maximo())} \n" \
                f"Grau médio = {str(g.grau_medio())} \n" \
                f"Mediana de grau = {str(g.mediana_de_grau())} \n"
        f.write(linha)
        numcompconex = f"Número de Componentes Conexas = {str(g.info_cc()[0])} \n"
        f.write(numcompconex)
        for i in range(len(g.info_cc()[1])):
            componentes = f"Componente {i + 1} = {str(g.info_cc()[2][i])} \n" \
                  f"Tamanho da componente {i + 1} = {str(g.info_cc()[1][i])} \n"
            f.write(componentes)
    f.close()
    print("Arquivo com informações do grafo gerado.")