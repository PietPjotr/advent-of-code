import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict

S = p.input_as_string('inputs/inp.txt')

parts = S.split('\n\n')

locks = []
keys = []
for p in parts:
    p = [[el for el in l] for l in p.split('\n')]

    if all([el == '#' for el in p[0]]):
        heights = []
        for c in range(len(p[0])):
            r = 0
            while p[r][c] == '#':
                r += 1

            heights.append(r - 1)
        locks.append(heights)
    else:
        show(p)
        heights = []
        for c in range(len(p[0])):
            r = len(p) - 1
            while p[r][c] == '#':
                r -= 1

            heights.append(len(p) - 1 - (r + 1))
        keys.append(heights)

p1 = 0
for key in keys:
    for lock in locks:
        if all([a + b <= 5 for a, b in zip(key, lock)]):
            p1 += 1

print(p1)
