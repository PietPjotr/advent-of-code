import sys
sys.path.append('..')
import my_parser as p
from collections import deque


L = p.input_as_lines('inputs/inp.txt')
R, C = 71, 71
G = [['.' for _ in range(C)] for _ in range(R)]

split = 1024

bytess = [[int(el) for el in line.split(',')] for line in L]
for x, y in bytess[:split]:
    G[y][x] = '#'


def bfs(G):
    start = (0, 0)
    end = (R - 1, C - 1)
    q = deque([(*start, 0)])
    visited = set([start])
    while q:
        r, c, dist = q.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != '#' and (nr, nc) not in visited:
                q.append((nr, nc, dist + 1))
                visited.add((nr, nc))

    return -1


print(bfs(G))

for x, y in bytess[split:]:
    G[y][x] = '#'
    if bfs(G) == -1:
        print(f'{x},{y}')
        break
