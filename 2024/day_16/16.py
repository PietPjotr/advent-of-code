import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict
from heapq import heappush, heappop
from collections import Counter


G = p.input_as_grid('inputs/inp.txt')
R = len(G)
C = len(G[0])

# Find the start and end points
start = (0, 0)
end = (0, 0)
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            start = (r, c)
        if G[r][c] == 'E':
            end = (r, c)


def bfs(G):
    # right, down, left, up
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    heap = []
    heappush(heap, (0, *start, 0, [start]))
    visited = defaultdict(lambda: float('inf'))
    visited[(*start, 0)] = 0

    min_cost = float('inf')
    best_paths = []

    while heap:
        cost, r, c, d, path = heappop(heap)

        if (r, c) == end:
            if cost < min_cost:
                min_cost = cost
                best_paths = [path]
            elif cost == min_cost:
                best_paths.append(path)
            continue

        # Rotate left or right
        for nd in [d - 1, d + 1]:
            nd = nd % 4
            if cost + 1000 <= visited[(r, c, nd)]:
                visited[(r, c, nd)] = cost + 1000
                heappush(heap, (cost + 1000, r, c, nd, path))

        # OR Step forward in the current direction
        dr, dc = deltas[d]
        nr, nc = r + dr, c + dc
        if G[nr][nc] != '#':
            if cost + 1 <= visited[(nr, nc, d)]:
                visited[(nr, nc, d)] = cost + 1
                heappush(heap, (cost + 1, nr, nc, d, path + [(nr, nc)]))

    return min_cost, best_paths


min_cost, best_paths = bfs(G)
print(min_cost)

# Count the number of unique positions visited in all best paths
all_positions = set()
for path in best_paths:
    all_positions |= set(path)

print(len(all_positions))
