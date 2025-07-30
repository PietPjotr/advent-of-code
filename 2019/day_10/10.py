import sys
sys.path.append('..')
import my_parser as p
from utils import *
from math import gcd
from math import atan2

G = p.input_as_grid('inputs/inp.txt')
G = Grid(G)
spos = Pos(G.Rmin, G.Cmin)
epos = Pos(G.Rmax, G.Cmax)

ds = G.findall('#')

# for every rock check if there's any in between the current and the p2 rock
visible = dict()
for p1 in ds[:]:
    rocks = []
    for p2 in ds:
        if p1 == p2:
            continue

        d = p2 - p1
        gcdv = gcd(*d)
        d //= gcdv
        np = p1
        ok = True
        for j in range(1, gcdv):
            np += d
            if np in ds:
                ok = False
                break

        if ok:
            rocks.append(p2)

    visible[p1] = rocks

# sort the rocks based on wich one can detect the most
pos, rocks = sorted(visible.items(), key=lambda x: (len(x[1]), x[0]), reverse=True)[0]

print(len(rocks))

# sort on angle for some reason this sorts it as we want it
rocks.sort(key=lambda x: atan2((x - pos).c, ((x - pos).r)), reverse=True)

# no need to actually redetect etc since we can already see geq 200 rocks
assert len(rocks) >= 200
tr, tc = rocks[200 - 1]
print(tc * 100 + tr)
