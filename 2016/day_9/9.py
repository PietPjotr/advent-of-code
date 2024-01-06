import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')

line = L[0]
line = line.strip()


def p1():
    res = ''
    i = 0
    while i < len(line):
        el = line[i]
        if el != '(':
            res += el
        if line[i:].startswith('('):
            marker = line[i+1:].split(')')[0]
            size, repeats = [int(el) for el in marker.split('x')]
            marked = line[i + len(marker) + 2:i + len(marker) + 2 + size]
            res += marked * repeats
            i = i + len(marker) + 2 + size - 1
        i += 1

    return len(res)


def p2(line):
    i = 0
    res2 = 0
    while i < len(line):
        el = line[i]
        if el != '(':
            res2 += 1
        if line[i:].startswith('('):
            marker = line[i+1:].split(')')[0]
            size, repeats = [int(el) for el in marker.split('x')]
            marked = line[i + len(marker) + 2:i + len(marker) + 2 + size]

            res2 += repeats * p2(marked)

            i = i + len(marker) + 2 + size - 1
        i += 1
    return res2


print(p1())
print(p2(line))
