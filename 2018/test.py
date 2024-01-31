from functools import lru_cache
from heapq import heappush, heappop

MOD = 20183

tx, ty  = (7, 770)
depth = 10647

@lru_cache(None)
def gindex(x, y):
    if x == y == 0: return 0
    if x == tx and y == ty: return 0
    if y == 0: return x * 16807 % MOD
    if x == 0: return y * 48271 % MOD
    return ((gindex(x-1, y) + depth) *
            (gindex(x, y-1) + depth) % MOD)

def region(x, y):
    return (gindex(x, y) + depth) % MOD % 3

ans1 = sum(region(x, y)
           for x in range(tx+1)
           for y in range(ty+1))


def neighbors(x, y, e):
    for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 0 <= nx and 0 <= ny:
            r = region(nx, ny)
            for ne in range(3):
                if r != ne:
                    yield nx, ny, ne, 8 if e != ne else 1

# rocky - neither [0]
# wet - torch [1]
# narrow - climb [2]

pq = [(0, 0, 0, 1)]
dist = {(0, 0, 1): 0}
while pq:
    d, x, y, e = heappop(pq)
    if (x, y, e) == (tx, ty, 1):
        print(f'Answer: {d}')

    if x > 5 * tx or y > 2 * ty: continue
    if dist.get((x, y, e)) < d: continue
    for nx, ny, ne, nw in neighbors(x, y, e):
        if d + nw < dist.get((nx, ny, ne), float('inf')):
            dist[nx, ny, ne] = d + nw
            heappush(pq, (d + nw, nx, ny, ne))