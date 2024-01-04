import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

graph = {}
cities = set()
for line in L:
    names, cost = line.split(' = ')
    cost = int(cost)
    name1, name2 = names.split(' to ')
    cities.add(name1)
    cities.add(name2)
    if name1 not in graph:
        graph[name1] = [(name2, cost)]
    elif name1 in graph:
        graph[name1].append((name2, cost))

    if name2 not in graph:
        graph[name2] = [(name1, cost)]
    elif name2 in graph:
        graph[name2].append((name1, cost))

p1 = float('inf')
p2 = float('-inf')
for name in graph:
    stack = [(name, 0, set())]
    while stack:
        name, cost, seen = stack.pop(0)
        seen.add(name)
        for neigh, neigh_cost in graph[name]:
            if neigh not in seen:
                stack.append((neigh, cost + neigh_cost, seen.copy()))

        if cost < p1 and len(seen) == len(cities):
            p1 = cost
        if cost > p2 and len(seen) == len(cities):
            p2 = cost

print(p1)
print(p2)
