import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

inp = p.input_as_lines('inputs/inp.txt')[0]


def create(a):
    b = deepcopy(a)
    b = b[::-1]
    b = ['10'[int(el)] for el in b]
    b = ''.join(b)
    return a + '0' + b


def checksum(a):
    res = ''
    for i in range(len(a) // 2):
        window = a[2*i:2*i+2]
        if window[0] == window[1]:
            res += '1'
        else:
            res += '0'
    return res


def solve(inp, length):
    while len(inp) < length:
        inp = create(inp)
    check = checksum(inp[:length])
    while len(check) % 2 == 0:
        check = checksum(check)
    print(check)


solve(inp, 272)
solve(inp, 35651584)