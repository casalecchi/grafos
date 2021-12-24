# Biblioteca de Grafos
Biblioteca criada para o trabalho prático 1 da disciplina COS242 - Teoria dos Grafos, no período 21.2. Foi escrita na linguagem [Python3]((https://www.python.org/)).

## Implementações

* Utilizando Matriz de Adjacência
* Utilizando Lista de Adjacência

## Funcionalidades

* Busca em largura e profundidade
* Diâmetro de um grafo
* Distância entre dois vértices
* Grau mínimo, máximo e médio de um grafo
* Mediana de graus de um grafo
* Árvore induzida pela busca em largura e também pela em profundidade
* Componentes conexas e suas informações

## Pré-requisitos

* [Python 3](https://www.python.org/) (com pip)

### Instalando dependências

Para instalar todas as dependências com uma venv:

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
## Usando a biblioteca

É usada a função ler_grafo(arquivo, implementação) passando um arquivo txt como primeiro parâmetro e passando uma string escolhendo a forma de implementação. Essa string pode ser "matriz" ou "lista".
Um exemplo de utilização é mostrado:

```python3
from grafos.leitura_grafo import ler_grafo
ler_grafo("grafo_teste.txt", "matriz")
```

Dentro da biblioteca é possível achar o arquivo "estudo_caso.py" que foi utilizado para fazer os estudos de caso que é pedido pelo trabalho prático. Nele temos alguns exemplos de utilização das funcionalidades citadas acima.

