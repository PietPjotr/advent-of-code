import sys
sys.path.append('..')
import my_parser as p
from itertools import combinations

L = p.input_as_lines('inputs/inp.txt')

liters = 150

lines = [int(el) for el in L]

iis = list(range(len(lines)))
combs = set()
for i in range(4, 19):
    cs = set([comb for comb in combinations(iis, i) if sum([lines[i] for i in comb]) == 150])
    combs = combs.union(cs)

print(len(combs))


def solve2(combs):
    p2 = 0
    m = min([len(el) for el in combs])
    for el in combs:
        if len(el) == m:
            p2 += 1
    print(p2)


solve2(combs)