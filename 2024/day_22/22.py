import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict
from itertools import product

L = p.input_as_lines('inputs/inp.txt')
L = [int(el) for el in L]


def update(num):
    m = num * 64
    num ^= m
    num %= 16777216

    d = num // 32
    num ^= d
    num %= 16777216

    m2 = num * 2048
    num ^= m2
    num %= 16777216

    return num


def update_all(nums):
    return [update(num) for num in nums]


all_tens = [[int(str(n)[-1]) for n in L]]
dss = [[0 for _ in range(len(L))]]

for it in range(2000):
    L = update_all(L)
    tens_old = all_tens[it]
    tens_new = [int(str(n)[-1]) for n in L]
    all_tens.append(tens_new)

    ds = [b - a for a, b in zip(tens_old, tens_new)]
    dss.append(ds)

print(sum(L))

scores = defaultdict(int)
for num in range(len(L)):
    temp_scores = {}
    for it in range(4, len(dss)):
        a, b, c, d = dss[it-3][num], dss[it-2][num], dss[it-1][num], dss[it][num]

        if (a, b, c, d) not in temp_scores:
            temp_scores[(a, b, c, d)] = all_tens[it][num]
    for k, v in temp_scores.items():
        scores[k] += v

s = sorted(scores.items(), key=lambda x: x[1], reverse=True)
best = s[0]
print(best[1])
