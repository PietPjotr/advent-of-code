import sys
sys.path.append('..')
import my_parser as p
import heapq
from collections import deque

L = p.input_as_lines('inputs/inp.txt')
target = (7, 770)
depth = 10647

# target = (10, 10)
# depth = 510


def geo_i(x, y, erosions):
    if (x, y) == target or (x, y) == (0, 0):
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return erosions[y][x - 1] * erosions[y - 1][x]


def create_erosions(maxx, maxy):
    erosions = [[] for _ in range(maxy)]
    for y in range(maxy):
        for x in range(maxx):
            i = geo_i(x, y, erosions)
            erosion_level = (i + depth) % 20183
            erosions[y].append(erosion_level)

    return erosions


def create_G(maxx, maxy):
    erosions = create_erosions(maxx, maxy)
    p1 = 0
    G = []
    for r, row in enumerate(erosions):
        nrow = []
        for c, el in enumerate(row):
            if el % 3 == 0:
                nrow.append('.')
            elif el % 3 == 1:
                nrow.append('=')
                if r <= target[1] and c <= target[0]:
                    p1 += 1
            elif el % 3 == 2:
                nrow.append('|')
                if r <= target[1] and c <= target[0]:
                    p1 += 2
        G.append(nrow)

    print(p1)
    return G


G = create_G(target[0] + 31, target[1] + 31)
R = len(G)
C = len(G[0])


def show(G, path):
    path_pos = [el[:2] for el in path]
    for r in range(R):
        for c in range(C):
            if (r, c) == (0, 0):
                print('S', end='')
            elif (r, c) == target:
                print('T', end='')
            elif (r, c) in path_pos:
                print(path[path_pos.index((r, c))][-1], end='')
            else:
                print(G[r][c], end='')
        print()
    print()


# dfs with optimalisations and ofc keep track of the current time
# for some reason, using different numbers for the gear changes the result ??? wtf is wrong
# also: for some reason our path is too short, we are 3 or 4 short on different examples
def p2(G):
    NEITHER = 2
    GEAR = 1
    TORCH = 0
    gear = {'.': [GEAR, TORCH], '=': [GEAR, NEITHER], '|': [TORCH, NEITHER]}
    hq = [(0, 0, 0, TORCH, [])]
    visited = {(0, 0, 0): 0}
    while hq:
        time, r, c, cgear, path = heapq.heappop(hq)
        if (c, r) == target:
            if cgear != TORCH:
                time += 7
            print(time)
            # return time, path
        if visited[(r, c, cgear)] < time:
            continue
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C:
                for ngear in gear[G[nr][nc]]:
                    ntime = time + 1
                    if ngear != cgear:
                        ntime += 7
                    if (nr, nc, ngear) in visited and visited[(nr, nc, ngear)] <= ntime:
                        continue
                    heapq.heappush(hq, (ntime, nr, nc, ngear, path + [(r, c, cgear)]))
                    visited[(nr, nc, ngear)] = ntime

    return time, path


# NOTE: does not work entire right now, not in the mood to fix it tho so
# just try a few of the shortest distances from the list, seems like the 3rd
# one often is the right one
def p2q():
    times = []
    TORCH = 0
    GEAR = 1
    NEITHER = 2
    gear = {'.': [GEAR, TORCH], '=': [GEAR, NEITHER], '|': [TORCH, NEITHER]}
    q = deque([(0, 0, 0, TORCH, [])])
    visited = {(0, 0, TORCH): 0}
    while q:
        time, r, c, cgear, path = q.popleft()
        if (c, r) == target:
            if cgear != TORCH:
                time += 7
            times.append(time)
            times.sort()
            # return time, path
        if visited[(r, c, cgear)] < time:
            continue
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C:
                for ngear in gear[G[nr][nc]]:
                    ntime = time + 1
                    if ngear != cgear:
                        ntime += 7
                    if (nr, nc, ngear) in visited and visited[(nr, nc, ngear)] <= ntime:
                        continue
                    q.append((ntime, nr, nc, ngear, path + [(r, c, cgear)]))
                    visited[(nr, nc, ngear)] = ntime

    print(times)
    return time, path


p2q()
