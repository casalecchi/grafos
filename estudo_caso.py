from leituraGrafo import ler_grafo
import time


grafo = ler_grafo("grafo_2.txt", "matriz")
start_time = time.time()
print(grafo)
print("--- %s seconds ---" % (time.time() - start_time))