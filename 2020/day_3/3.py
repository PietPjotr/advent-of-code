import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

G = p.input_as_grid('inputs/inp.txt')
G = u.Grid(G)

R = G.Rmax
C = G.Cmax

dc = 3
dr = 1

def trees(dr, dc):
    t = 0
    r = dr
    c = dc
    while r < R:
        if G[u.Pos(r, c % C)] == '#':
            t += 1
        r += dr
        c = (c + dc) % (C)
    return t

p2 = 1
p1 = 0
for i, (dc, dr) in enumerate([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]):
    d = trees(dr, dc)
    if i == 1:
        p1 = d
    p2 *= d

print(p1)
print(p2)
