import sys
sys.path.append('..')
import my_parser as p
import re
import numpy as np

L = p.input_as_lines('inputs/inp.txt')

og = []
for line in L:
    nums = [int(el) for el in re.findall(r'-?\d+', line)]
    og.append(nums)


def simulate(particles, time):
    ret = []
    for p in particles:
        pos = p[0:3]
        v = p[3:6]
        a = p[6:9]
        np = []
        nv = []
        for d in range(3):
            nv.append(v[d] + a[d] * time)
            np.append(pos[d] + nv[d] * time)

        ret.append(np + nv + a)
    return ret


particles = simulate(og, 1000000)
mpos = float('inf')
particle = -1
for i, p in enumerate(particles):
    if abs(p[0]) + abs(p[1]) + abs(p[2]) < mpos:
        mpos = abs(p[0]) + abs(p[1]) + abs(p[2])
        particle = i

print(particle)


def collide_all(particles):
    ret = []
    for i, p1 in enumerate(particles):
        add = True
        for j, p2 in enumerate(particles):
            if i == j:
                continue
            if tuple(p1[0:3]) == tuple(p2[0:3]):
                add = False
                break
        if add:
            ret.append(p1)
    return ret


ps = og
for time in range(100):
    ps = simulate(ps, 1)
    ps = collide_all(ps)
    print(len(ps))
