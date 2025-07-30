import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict
from math import lcm

L = p.input_as_lines('inputs/inp.txt')
ps = [get_all_numbers(x) for x in L]
vs = [[0 for _ in range(len(ps[0]))] for _ in range(len(ps))]


def step(ps, vs):
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            p1, p2 = ps[i], ps[j]

            # apply gravity
            for d, (d1, d2) in enumerate(zip(p1, p2)):
                if d1 > d2:
                    vs[i][d] -= 1
                    vs[j][d] += 1
                elif d2 > d1:
                    vs[i][d] += 1
                    vs[j][d] -= 1

    # apply velocity
    for i in range(len(ps)):
        for d in range(len(ps[0])):
            ps[i][d] += vs[i][d]
    return ps, vs


def score(ps, vs):
    p1 = 0
    for p, v in zip(ps, vs):
        sp = sum([el if el > 0 else -el for el in p])
        sv = sum([el if el > 0 else -el for el in v])
        p1 += sp * sv

    return p1


def part1(ps, vs):
    for i in range(1000):
        ps, vs = step(ps, vs)
    print(score(ps, vs))


# split up per dimension and check whenever all the states align:
def step_single(ps, vs, d):
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            p1, p2 = ps[i], ps[j]

            # apply gravity
            d1, d2 = p1[d], p2[d]
            if d1 > d2:
                vs[i][d] -= 1
                vs[j][d] += 1
            elif d2 > d1:
                vs[i][d] += 1
                vs[j][d] -= 1

    # apply velocity
    for i in range(len(ps)):
        ps[i][d] += vs[i][d]
    return ps, vs


part1(ps, vs)


repeats = []
for d in range(3):
    states = set()

    i = 0
    while True:
        psd = [p[d] for p in ps]
        vsd = [v[d] for v in vs]

        s = tuple(psd + vsd)

        if s in states:
            repeats.append(i)
            break

        states.add(s)
        i += 1
        ps, vs = step_single(ps, vs, d)

p2 = 1
for el in repeats:
    p2 *= el
print(lcm(*repeats))