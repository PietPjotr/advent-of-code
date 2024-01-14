import sys
sys.path.append('..')
import my_parser as p
from collections import deque

L = p.input_as_lines('inputs/inp.txt')
a, b = [int(x.split()[-1]) for x in L]


def nex(val, fact):
    return (val * fact) % 2147483647 if val * fact > 2147483647 else val * fact


def solve(a, b):
    facta = 16807
    factb = 48271
    a = 883
    b = 879

    p1 = 0
    pairs1 = 0
    p2 = 0
    pairs2 = 0
    stacka, stackb = deque(), deque()

    while pairs2 < 5 * 10 ** 6:
        a = nex(a, facta)
        b = nex(b, factb)

        if a % 4 == 0:
            stacka.append(a)
        if b % 8 == 0:
            stackb.append(b)

        if pairs1 < 40 * 10 ** 6:
            pairs1 += 1
            # Check the last 16 bits directly using bitwise operations
            if (a & 0xFFFF) == (b & 0xFFFF):
                p1 += 1

        if stacka and stackb:
            pairs2 += 1
            sa = stacka.popleft()
            sb = stackb.popleft()
            # Check the last 16 bits directly using bitwise operations
            if (sa & 0xFFFF) == (sb & 0xFFFF):
                p2 += 1
                print(str(pairs2 / (5 * 10 ** 6) * 100) + '%')
    print(p1)
    print(p2)


solve(a, b)
