from leituraGrafo import ler_grafo
import random
import time


grafo = ler_grafo("grafo_W_4_1.txt", "lista")

# Questão 1
# start_time = time.time()
# dist_cam = grafo.dist_caminho_min(1)
# print(f"Distância e caminho entre 1 e 10 -> {dist_cam[9]}")
# print(f"Distância e caminho entre 1 e 20 -> {dist_cam[19]}")
# print(f"Distância e caminho entre 1 e 30 -> {dist_cam[29]}")
# print(f"Distância e caminho entre 1 e 40 -> {dist_cam[39]}")
# print(f"Distância e caminho entre 1 e 50 -> {dist_cam[49]}")
# print("--- %s seconds --- 1 Dijkstra" % (time.time() - start_time))
#
# # Questão 2
# vertices = []
# for _ in range(100):
#     n = random.randint(1, grafo.vertices)
#     vertices.append(n)
# print(f"Vértices escolhidos: {vertices}, total = {len(vertices)}")
#
# tempos = []
# i = 0
# for v in vertices:
#     start_time = time.time()
#     grafo.dijkstra(v)
#     final_time = time.time() - start_time
#     print(f"Iteração {i} levou {final_time} segundos")
#     i += 1
#     tempos.append(float(final_time))
#
# print(f"A média é = {sum(tempos) / 100}")

# Questão 3
start_time = time.time()
print(f"Começou = {start_time}")
arvore = grafo.gerar_mst(1)[0]
print("--- %s seconds --- Gerar MST" % (time.time() - start_time))

print(f"O peso total da MST é = {sum(arvore)}")
