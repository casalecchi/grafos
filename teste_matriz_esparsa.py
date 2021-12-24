from matrizAdjacencia import Matriz
from listaAdjacencia import Lista





# Grafo slide aula dfs
grafo = Lista(8, [[1, 3], [1, 4], [2, 4], [3, 8], [2, 3], [3, 4], [4, 7], [4, 6], [5, 7], [6, 5], [6, 7]])
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
print(grafo.bfs(2))
#print(grafo.bfs(1))


#for i in a.toarray():
 #   print(i)
