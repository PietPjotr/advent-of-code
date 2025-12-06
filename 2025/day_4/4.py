import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

G = p.input_as_grid('inputs/inp.txt')
R = len(G[0])
C = len(G)

res = 0
removed = 0
to_remove = set()
iterations = 0
while to_remove or iterations == 0:
    to_remove = set()
    for r in range(R):
        for c in range(C):
            if G[r][c] != '@':
                continue

            neighs = []
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    nr = r + i
                    nc = c + j
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or (nr == r and nc == c):
                        continue
                    neighs.append(G[nr][nc])

            if neighs.count('@') <= 3:
                to_remove.add((r, c))
                if iterations == 0:
                    res = len(to_remove)

    iterations += 1
    for (r, c) in to_remove:
        G[r][c] = '.'
        removed += 1

    print(iterations)

print(res)
print(removed)
