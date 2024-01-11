import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

# find the positions of all the digits and also of the start digit
nums = []
start = (-1, -1)
for r in range(R):
    for c in range(C):
        el = G[r][c]
        if el == '0':
            start = (r, c)
        if el.isdigit():
            nums.append((r, c))

graph = {num: {} for num in nums}

# find all the neighbours and their distances:
for num in nums:
    visited = set()
    stack = [[0, num]]
    while stack:
        steps, pos = stack.pop(0)
        r, c = pos
        if G[r][c].isdigit() and (r, c) != num and (r, c) not in graph[num]:
            graph[num][(r, c)] = steps
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and G[nr][nc] != '#':
                stack.append((steps + 1, (nr, nc)))
                visited.add((nr, nc))


# perform the tsp on the graph created above
def tsp():
    p1 = float('inf')
    p2 = float('inf')
    stack = [[0, deepcopy(start), []]]
    endpoints = []
    while stack:
        dist, pos, visited = stack.pop(0)
        new_visited = deepcopy(visited)
        new_visited.append(pos)
        if len(new_visited) == len(nums):
            if dist < p1:
                p1 = dist
            if dist + graph[start][pos] < p2:
                p2 = dist + graph[start][pos]
            continue

        for neigh, delta_dist in graph[pos].items():
            if neigh not in visited:
                stack.append((dist + delta_dist, neigh, new_visited))

    print(p1)
    print(p2)


tsp()
