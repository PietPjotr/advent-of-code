import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

# up right down left
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def p1():
    p = 0
    pos = (*start, 0)
    for i in range(10000):
        r, c, d = pos
        if (r, c) in infected:
            infected.remove((r, c))
            nd = (d + 1) % 4
        else:
            infected.add((r, c))
            nd = (d - 1) % 4
            p += 1

        nr = r + DR[nd]
        nc = c + DC[nd]
        pos = (nr, nc, nd)

    print(p)


def p2():
    p = 0
    pos = (*start, 0)
    for i in range(10000000):
        r, c, d = pos
        if (r, c) in weakened:
            weakened.remove((r, c))
            infected.add((r, c))
            nd = d
            p += 1
        elif (r, c) in infected:
            infected.remove((r, c))
            flagged.add((r, c))
            nd = (d + 1) % 4
        elif (r, c) in flagged:
            flagged.remove((r, c))
            nd = (d + 2) % 4
        else:
            weakened.add((r, c))
            nd = (d - 1) % 4

        nr = r + DR[nd]
        nc = c + DC[nd]
        pos = (nr, nc, nd)

    print(p)


infected_og = set()
weakened = set()
flagged = set()
start = (R // 2, C // 2)
for r in range(R):
    for c in range(C):
        el = G[r][c]
        if el == '#':
            infected_og.add((r, c))

infected = deepcopy(infected_og)
p1()
infected = deepcopy(infected_og)
p2()