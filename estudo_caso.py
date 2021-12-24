from leituraGrafo import ler_grafo
import random
import time


# Questão 1 vai printar pelo memory profiler
grafo = ler_grafo("grafo_5.txt", "matriz")

# Na questão 2 e 3 precisamos usar os mesmos 1000 vértices aleatórios
vertices_bfs_dfs = []
for _ in range(1, 1001):
    n = random.randint(1, grafo.vertices)
    vertices_bfs_dfs.append(n)

start_time = time.time()
grafo.bfs(1)
print("--- %s seconds --- 1 BFS" % (time.time() - start_time))

start_time = time.time()
grafo.dfs(1)
print("--- %s seconds --- 1 DFS" % (time.time() - start_time))


# Questão 2 - 1000 BFS's
start_time = time.time()
for v in vertices_bfs_dfs:
    grafo.bfs(v)
print("--- %s seconds --- Questão 2" % (time.time() - start_time))

# Questão 3 - 1000 DFS's
start_time = time.time()
for v in vertices_bfs_dfs:
    grafo.dfs(v)
print("--- %s seconds --- Questão 3" % (time.time() - start_time))

# Questão 4 - Pai dos vértices
start_time = time.time()
print("--------- BFS ---------")
print("-- Árvore com raiz 1 --")
print(grafo.pai_bfs(1, 10))
print(grafo.pai_bfs(1, 20))
print(grafo.pai_bfs(1, 30))
print("-- Árvore com raiz 2 --")
print(grafo.pai_bfs(2, 10))
print(grafo.pai_bfs(2, 20))
print(grafo.pai_bfs(2, 30))
print("-- Árvore com raiz 3 --")
print(grafo.pai_bfs(3, 10))
print(grafo.pai_bfs(3, 20))
print(grafo.pai_bfs(3, 30))
print("--------- DFS ---------")
print("-- Árvore com raiz 1 --")
print(grafo.pai_dfs(1, 10))
print(grafo.pai_dfs(1, 20))
print(grafo.pai_dfs(1, 30))
print("-- Árvore com raiz 2 --")
print(grafo.pai_dfs(2, 10))
print(grafo.pai_dfs(2, 20))
print(grafo.pai_dfs(2, 30))
print("-- Árvore com raiz 3 --")
print(grafo.pai_dfs(3, 10))
print(grafo.pai_dfs(3, 20))
print(grafo.pai_dfs(3, 30))
print("--- %s seconds --- Questão 4" % (time.time() - start_time))

# Questão 5 - Distância entre vértices
start_time = time.time()
print(grafo.distancia(10, 20))
print(grafo.distancia(10, 30))
print(grafo.distancia(20, 30))
print("--- %s seconds --- Questão 5" % (time.time() - start_time))

# Questão 6 - Componentes conexas
start_time = time.time()
print(grafo.info_cc())
print("--- %s seconds --- Questão 6" % (time.time() - start_time))

# Questão 7 - Diâmetro
start_time = time.time()
print(grafo.diametro())
print("--- %s seconds --- Questão 7" % (time.time() - start_time))
