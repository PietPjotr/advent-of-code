import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict

dirs = [(-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),]

L = p.input_as_lines('inputs/inp.txt')
# G = p.input_as_grid('inputs/inp.txt')
# R = len(G)
# C = len(G[0])

s = 1176
# s = 21

orders = L[:s]
orders = [[int(el) for el in order.split('|')] for order in orders]

inss = L[s + 1:]
inss = [[int(el) for el in l.split(',')] for l in inss]


def part1():
    res = 0
    for ins in inss:
        for a, b in list(zip(ins[:-1], ins[1:])):
            correct = True

            if [a, b] in orders:
                continue
            else:
                correct = False
                break

        if correct:
            i = (len(ins) //2)
            res += ins[i]


def check_correct(ins):
    for a, b in list(zip(ins[:-1], ins[1:])):
        if [a, b] in orders:
            continue
        else:
            return False
    return True


res = 0
for ins in inss:
    og_ins = ins.copy()
    not_correct = False
    while not (check_correct(ins)):
        not_correct = True
        for a, b in zip(ins[:-1], ins[1:]):
            if [a, b] not in orders:
                ia = ins.index(a)
                ib = ins.index(b)

                temp = ins[ia]
                ins[ia] = ins[ib]
                ins[ib] = temp

    if not_correct:
        i = len(ins) // 2
        res += ins[i]

print(res)
