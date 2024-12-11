import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


S = p.input_as_string('inputs/inp.txt')
R = 6
C = 25

Gs = []
start_grid = 0
while start_grid < len(S):
    G = []
    for r in range(R):
        start = start_grid + r * C
        end = start_grid + (r + 1) * C
        G.append(S[start:end])

    Gs.append(G)
    start_grid += R * C


def score(Gs):
    m = float('inf')
    lm = 0
    for i, G in enumerate(Gs):
        if ''.join(G).count('0') < m:
            lm = i
            m = ''.join(G).count('0')
    ones = ''.join(Gs[lm]).count('1')
    twos = ''.join(Gs[lm]).count('2')

    return ones * twos


print(score(Gs))

finalG = [['' for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        layer = 0
        p = Gs[layer][r][c]
        while p == '2':
            layer += 1
            p = Gs[layer][r][c]
        finalG[r][c] = p

finalG = [[int(el) for el in r] for r in finalG]


def show(G):
    for r in G:
        print()
        for c in r:
            if c == 1:
                print('#', end='')
            else:
                print(' ', end='')
    print()


show(finalG)