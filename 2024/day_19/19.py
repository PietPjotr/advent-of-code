import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict
from functools import cache


S = p.input_as_string('inputs/inp.txt')

patterns, towels = S.split('\n\n')

towels = towels.split('\n')
patterns = patterns.split(', ')


@cache
def find(patterns, towel):
    if not towel:
        return 1

    test = []
    for p in patterns:
        if towel.startswith(p):
            test.append(find(patterns, towel[len(p):]))
    return sum(test)


p1 = 0
p2 = 0
for towel in towels:
    if ways := find(tuple(patterns), towel):
        p1 += 1
        p2 += ways

print(p1)
print(p2)
