import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')

def p1():
    res = 0
    for l in L:
        i1 = l.index(max(l[:-1]))
        i2 = l.index(max(l[i1 + 1:]))

        lres = l[i1] + l[i2]
        res += int(lres)

    print(res)


def p2():
    res = 0
    for l in L[:]:
        to_add = 11
        Is = []
        i_prev = -1
        while to_add >= 0:
            slice = l[i_prev + 1:len(l) - to_add]
            i = slice.index(max(slice)) + i_prev + 1
            Is.append(i)
            i_prev = i
            to_add -= 1

        lres = ''
        for i in Is:
            lres += l[i]
        assert len(lres) == 12

        res += int(lres)

    print(res)


p1()
p2()
