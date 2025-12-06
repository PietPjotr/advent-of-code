import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

S = p.input_as_string('inputs/inp.txt')

S = S.split(',')

def p1():
    res = 0
    for l in S:
        s, e = [int(el) for el in l.split('-')]
        for i in range(s, e + 1):
            i = str(i)
            if len(i) % 2 == 0:
                if i[0: len(i) // 2] == i[len(i) // 2:]:
                    res += int(i)

    print(res)


def p2():
    res = 0
    for l in S:
        s, e = [int(el) for el in l.split('-')]
        for i in range(s, e + 1):
            i = str(i)
            for idx in range(1, len(i) // 2 + 1):
                if len(i) % idx == 0:
                    if i == len(i) // idx * i[0:idx]:
                        res += int(i)
                        break

    print(res)

p2()