import sys
sys.path.append('..')
import my_parser as p
from collections import deque
from collections import Counter
from collections import defaultdict


G = p.input_as_grid('inputs/inp.txt')
R = len(G)
C = len(G[0])

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

start = (0, 0)
end = (0, 0)
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            start = (r, c)
        if G[r][c] == 'E':
            end = (r, c)


def get_distances_from(G, pos):
    distances = {}

    q = deque([(*pos, 0)])
    distances[pos] = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        r, c, dist = q.popleft()

        # Explore all 4 possible directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if G[nr][nc] != '#' and (nr, nc) not in distances:
                distances[(nr, nc)] = dist + 1
                q.append((nr, nc, dist + 1))

    return distances


def all_cheat_distances(G, start, end, max_cheats=2):
    distances_from_end = get_distances_from(G, end)
    distances_from_start = get_distances_from(G, start)
    normal_dist = distances_from_start[end]
    results = [normal_dist]  # so we can easily extract the normal_distance
    for (r, c) in distances_from_start:
        sd = distances_from_start[(r, c)]

        visited = defaultdict(int)
        q = deque([(r, c, 0)])

        while q:
            r, c, dist = q.popleft()
            if dist >= max_cheats:
                continue

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= c < C and (nr, nc) not in visited:
                    q.append((nr, nc, dist + 1))
                    visited[(nr, nc)] = dist + 1

        for (r, c), dist in visited.items():
            if (r, c) in distances_from_end:
                ed = distances_from_end[(r, c)]
                if sd + ed + dist < normal_dist:
                    results.append(sd + ed + dist)

    return results


def get_score(costs):
    normal_dist = costs[0]
    C = Counter(costs)

    score = 0
    for k, v in C.items():
        if k <= normal_dist - 100:
            score += v
    return score


print(get_score(all_cheat_distances(G, start, end, 2)))
print(get_score(all_cheat_distances(G, start, end, 20)))
