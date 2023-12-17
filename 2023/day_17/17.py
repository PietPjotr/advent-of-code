import sys
sys.path.append('..')
import my_parser as p
import heapq

lines = p.input_as_lines('inputs/inp.txt')

G = [[int(el) for el in line] for line in lines]
R = len(G)
C = len(G[0])

# north, east, south, west
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def get_score(distances):
    """Note Got lucky with the end point being further than 4 points from a
    turn otherwise would have had to change the score calculation."""
    min_dist = float('inf')
    for k, v in distances.items():
        if k[0] == R - 1 and k[1] == C - 1:
            if v < min_dist:
                min_dist = v
    return min_dist


def get_dirs(part, d, con):
    dirs = [0, 1, 2, 3]
    dirs.remove((d + 2) % 4)
    if part == 1:

        if con == 3:
            dirs.remove(d)
    else:
        if con == 10:
            dirs.remove(d)
        elif con < 4:
            dirs = [d]

    return dirs


for part in [1, 2]:
    distances = {}
    visited = set()
    pq = [(0, 0, 0, 1, 0), (0, 0, 0, 2, 0)]  # (row, col, dir, consecutive, distance)
    while pq:
        l, r, c, d, con = heapq.heappop(pq)

        if (r, c, d, con) in distances:
            if l < distances[(r, c, d, con)]:
                distances[(r, c, d, con)] = l
            else:
                continue
        else:
            distances[(r, c, d, con)] = l

        dirs = get_dirs(part, d, con)

        for nd in dirs:
            nr = r + DR[nd]
            nc = c + DC[nd]

            if nr < 0 or nc < 0 or nr >= R or nc >= C:
                continue

            nl = l + G[nr][nc]
            if nd == d:
                heapq.heappush(pq, (nl, nr, nc, nd, con + 1))
            else:
                heapq.heappush(pq, (nl, nr, nc, nd, 1))


    print(get_score(distances))

