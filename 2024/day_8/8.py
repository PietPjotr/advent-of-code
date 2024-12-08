import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict


G = p.input_as_grid('inputs/inp.txt')
R = len(G)
C = len(G[0])

els = defaultdict(set)

for r in range(R):
    for c in range(C):
        el = G[r][c]
        if el != '.':
            els[el].add((r, c))

poss1, poss2 = set(), set()
for k, v in els.items():
    for r1, c1 in v:
        for r2, c2 in v:
            if (r1, c1) != (r2, c2):
                dr = r2 - r1
                dc = c2 - c1

                nr1, nc1 = r1, c1
                nr2, nc2 = r2, c2

                # mirroring in point 1
                i = 0
                while 0 <= nr1 < R and 0 <= nc1 < C:
                    poss2.add((nr1, nc1))
                    # p1
                    if i == 1:
                        poss1.add((nr1, nc1))

                    nr1 -= dr
                    nc1 -= dc
                    i += 1

                # mirroring in point 2
                i = 0
                while 0 <= nr2 < R and 0 <= nc2 < C:
                    poss2.add((nr2, nc2))
                    # p1
                    if i == 1:
                        poss1.add((nr2, nc2))

                    nr2 += dr
                    nc2 += dc
                    i += 1

print(len(poss1))
print(len(poss2))
