import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

L = p.input_as_lines('inputs/inp.txt')


# Build the graph as an adjacency list
graph = defaultdict(set)
for c in L:
    a, b = c.split('-')
    graph[a].add(b)
    graph[b].add(a)


def find_all_fully_connected(graph):
    visited = set()
    groups = []

    for node in graph:
        group = set()
        if node in visited:
            continue
        stack = [node]


def find_triplets(graph):
    triplets = set()
    for node, neighbors in graph.items():
        neighbors = sorted(neighbors)
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                a, b = neighbors[i], neighbors[j]
                if b in graph[a] or a in graph[b]:
                    triplets.add(tuple(sorted([node, a, b])))
    return triplets

groups = find_triplets(graph)

p1 = 0
for g in groups:
    if any(el.startswith('t') for el in g):
        p1 += 1
print(p1)

G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

cliques = list(nx.find_cliques(G))
best = sorted(cliques, key=len, reverse=True)[0]

print(','.join(sorted(best)))


def plot(G):
    pos = nx.spring_layout(G, k=0.15, iterations=20)
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, node_size=30, node_color='blue', with_labels=False, alpha=0.7, edge_color='gray')
    plt.title('Graph Visualization')
    plt.show()


plot(G)
