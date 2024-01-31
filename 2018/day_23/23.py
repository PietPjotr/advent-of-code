import sys
sys.path.append('..')
import my_parser as p
import re
import matplotlib.pyplot as plt
import numpy as np

L = p.input_as_lines('inputs/inp.txt')
bots = []
for l in L:
    nums = [int(el) for el in re.findall(r'-?\d+', l)]
    bots.append(nums)


def distance(b1, b2):
    return sum([abs(b1[i] - b2[i]) for i in range(3)])


def p1():
    ranges = [bot[-1] for bot in bots]
    maxr = max(ranges)
    maxb = bots[ranges.index(maxr)]

    print(sum([1 if distance(maxb, b) <= maxr else 0 for b in bots]))


p1()

# ds = []
# for i, b1 in enumerate(bots):
#     for b2 in bots[i + 1:]:
#         d = distance(b1, b2)
#         ds.append(d)

# mind = min(ds)

def p2():
    xs, ys, zs, rs = [], [], [], []
    for b in bots:
        xs.append(b[0])
        ys.append(b[1])
        zs.append(b[2])
        rs.append(b[3])

    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    minz, maxz = min(zs), max(zs)
    minr, maxr = min(rs), max(rs)


    def show_dimension(mind, maxd, d):
        insides = []
        for val in np.linspace(mind, maxd + 1, 100):
            inside = 0
            for bot in bots:
                if abs(bot[d] - val) <= bot[-1]:
                    inside += 1
            insides.append(inside)

        plt.plot(insides)
        plt.show()

    show_dimension(minx, maxx, 0)
    show_dimension(miny, maxy, 1)
    show_dimension(minz, maxz, 2)

p2()
# def hope():
