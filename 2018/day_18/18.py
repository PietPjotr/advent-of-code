import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])


def get_neighbours(r, c):
    neighs = []
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dc == dr == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C:
                neighs.append((nr, nc))
    return neighs


def show(G):
    for row in G:
        print(''.join(row))
    print()


def solve(G):
    states = {}
    i = 0
    for i in range(600):  # note maybe change to higher for p2

        s = score(G)
        if s in states:
            states[s].append(i)
        else:
            states[s] = [i]

        nG = deepcopy(G)
        for r in range(R):
            for c in range(C):
                el = G[r][c]
                neighs = get_neighbours(r, c)
                if el == '.':
                    if len([n for n in neighs if G[n[0]][n[1]] == '|']) >= 3:
                        nG[r][c] = '|'
                elif el == '|':
                    if len([n for n in neighs if G[n[0]][n[1]] == '#']) >= 3:
                        nG[r][c] = '#'
                elif el == '#':
                    if len([n for n in neighs if G[n[0]][n[1]] == '#']) >= 1 and \
                    len([n for n in neighs if G[n[0]][n[1]] == '|']) >= 1:
                        nG[r][c] = '#'
                    else:
                        nG[r][c] = '.'

        G = nG
        i += 1

    its = 1000000000
    delta = 0
    for k, v in states.items():
        if len(v) > 1:
            delta = v[1] - v[0]

    idx = 500 + (its - 500) % delta

    for k, v in states.items():
        if 10 in v:
            print(k)  # print part1
        elif idx in v:
            print(k)  # print part2


def score(G):
    l = 0
    t = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == '|':
                t += 1
            elif G[r][c] == '#':
                l += 1

    return l * t


solve(G)
