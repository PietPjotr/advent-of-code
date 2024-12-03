import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = p.input_as_grid('inputs/inp.txt')
R = len(G)
C = len(G[0])


def check(n):
    n = str(n)
    n = [int(el) for el in n]
    diffs = [b - a for a, b in zip(n[:-1], n[1:])]
    incr = all([0 <= d for d in diffs])
    same = any([0 == d for d in diffs])

    return incr and same


def check_b(n):
    n = str(n)
    n = [int(el) for el in n]
    diffs = [b - a for a, b in zip(n[:-1], n[1:])]

    b = False
    # lone 0 in diffs
    for i in range(len(diffs) - 2):
        l = diffs[i]
        m = diffs[i + 1]
        r = diffs[i + 2]

        # begin lone 0
        if i == 0 and l == 0 and m != 0:
            b = True
        # end lone 0
        elif i + 2 == len(diffs) - 1 and r == 0 and m != 0:
            b = True
        # middle lone 0
        elif m == 0 and l != 0 and r != 0:
            b = True

    return b


inp = '248345-746315'
a, b = [int(el) for el in inp.split('-')]

p1 = 0
p2 = 0
for i in range(a, b + 1):
    if check(i):
        p1 += 1
        if check_b(i):
            p2 += 1

print(p1)
print(p2)


