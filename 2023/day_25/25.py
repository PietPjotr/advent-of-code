import sys
sys.path.append('..')
import my_parser as p
import networkx as nx
import matplotlib.pyplot as plt

L = p.input_as_lines('inputs/inp.txt')
# G = [[el for el in line] for lin in L]
# R = len(G)
# C = len(G[0])

wires = {}

for line in L:
    s, e = line.split(': ')
    e = e.split(' ')
    wires[s] = e


def dict_to_graph(graph_dict):
    G = nx.Graph()
    for node, neighbors in graph_dict.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G


def graph_to_dict(graph):
    graph_dict = {}
    for node in graph.nodes():
        graph_dict[node] = list(graph.neighbors(node))
    return graph_dict


def split_graph(graph_dict):
    # Convert the dictionary representation to a NetworkX graph
    G = dict_to_graph(graph_dict)

    # Calculate betweenness centrality for each edge
    edge_centrality = nx.edge_betweenness_centrality(G)

    # Sort edges by centrality and choose the top 3
    edges_to_remove = sorted(edge_centrality, key=edge_centrality.get, reverse=True)[:3]

    # Remove the chosen edges
    for edge in edges_to_remove:
        G.remove_edge(*edge)

    # Convert the modified graph back to a dictionary
    modified_graph_dict = graph_to_dict(G)

    # Verify connectivity
    components = list(nx.connected_components(G))

    print(len(components[0]) * len(components[1]))

split_graph(wires)
