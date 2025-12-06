import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

G = p.input_as_grid('inputs/inp.txt')
G = u.Grid(G)
G = G.remove('.')

s = set()

res = sum([1 for key in G.keys() if len(G.get_neigh(key)) <= 3])
print(res)

to_remove = set()
removed = 0
i = 0
while to_remove or i == 0:
    to_remove = set()
    for key in G.keys():
        ns = G.get_neigh(key)
        if len(ns) <= 3:
            to_remove.add(key)

    for el in to_remove:
        del G[el]
        removed += 1
    i += 1

print(removed)
