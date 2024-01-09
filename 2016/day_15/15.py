import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

discs = []
for line in L:
    line = line.replace('.', '')
    line = line.split()
    m = line[3]
    pos = line[-1]
    discs.append([int(pos), int(m)])


def update_discs(discs, i):
    new = []
    for disc in discs:
        pos, m = disc
        new.append([(pos + i) % m, m])
    return new


def solve(discs):
    i = 0
    while True:
        cur = update_discs(discs, i)
        test = []
        for j, disc in enumerate(cur):
            pos, m = disc
            test.append((pos + j) % m == 0)

        if all(test):
            print(i - 1)
            return

        i += 1


solve(discs)
solve(discs + [[0, 11]])
