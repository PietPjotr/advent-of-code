import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict


G = p.input_as_grid('inputs/inp.txt')
R = len(G)
C = len(G[0])

G = [[int(el) for el in r] for r in G]

start_positions = []

for r in range(R):
    for c in range(C):
        if G[r][c] == 0:
            start_positions.append((r, c))

# p1
dirs = [(-1, 0),(0, -1), (0, 1), (1, 0)]
p1 = 0
for start_pos in start_positions:
    stack = [start_pos]
    visited = set()
    while stack:
        (r, c) = stack.pop()
        visited.add((r, c))

        if G[r][c] == 9:
            p1 += 1
            continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and G[nr][nc] == G[r][c] + 1:
                stack.append((nr, nc))

print(p1)


# p2
dirs = [(-1, 0),(0, -1), (0, 1), (1, 0)]
p2 = 0
for start_pos in start_positions:
    stack = [start_pos]
    while stack:
        r, c = stack.pop()

        if G[r][c] == 9:
            p2 += 1
            continue

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == G[r][c] + 1:
                stack.append((nr, nc))

print(p2)
