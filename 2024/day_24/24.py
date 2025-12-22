import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from itertools import permutations
import random

S = p.input_as_string('inputs/inp.txt')
vals, connections = S.split('\n\n')

wires = dict()

for l in vals.split('\n'):
    name, value = l.split(': ')
    value = int(value)
    wires[name] = value

og_wires = wires.copy()
xwires = {'x' + (2 - len(str(i))) * '0' + str(i) for i in range(45)}
ywires = {'y' + (2 - len(str(i))) * '0' + str(i) for i in range(45)}
zwires = {'z' + (2 - len(str(i))) * '0' + str(i) for i in range(46)}


def get_data(connections):
    instructions = []
    for w1, op, w2, _, w3 in [el.split() for el in connections.split('\n')]:
        instructions.append([w1, op, w2, w3])

    return instructions, xwires, ywires, zwires


def wires_to_num(wires, wire_names):
    bits = ''
    for w in sorted(wire_names):
        bits = str(wires[w]) + bits
    return int(bits, 2)


def run(instructions, wires, xwires, ywires, zwires):
    i = 0
    changed = 0
    x = wires_to_num(wires, xwires)
    y = wires_to_num(wires, ywires)
    z = x + y
    z = '0' * (45 - len(bin(z)[2:])) + bin(z)[2:]

    while not all([w in wires for w in zwires]):
        w1, op, w2, w3 = instructions[i % len(instructions)]
        added = False
        if w1 in wires and w2 in wires and w3 not in wires:
            added = True
            changed = i
            if op == 'XOR':
                wires[w3] = wires[w1] ^ wires[w2]
            elif op == 'OR':
                wires[w3] = wires[w1] | wires[w2]
            elif op == 'AND':
                wires[w3] = wires[w1] & wires[w2]

        # check if new z bit is correct based off addition of x and y
        if added and w3 in zwires and 'z45' not in wires:
            if int(z[-(int(w3[1:]) + 1)]) == wires[w3]:
                continue
            else:
                return [w1, op, w2, w3]

        # the connections graph is no longer 'fully connected'
        if i - changed > len(instructions):
            return [w1, op, w2, w3]

        i += 1

    return [w1, op, w2, w3]


# sort the instructions by first finding all the instructions based on 0, then
# all on 1, then all on 2 etc etc:
def sort_instructions(instructions, base_wires):
    base  = 0
    wires = {wire: base_wires[wire] for wire in base_wires if get_all_numbers(wire) == base}
    ins_sorted = []
    while 'z45' not in wires:
        i = 0
        changed = 0
        while changed >= i - len(instructions):
            w1, op, w2, w3 = instructions[i % len(instructions)]
            if w1 in wires and w2 in wires and w3 not in wires:
                changed = i
                if op == 'XOR':
                    wires[w3] = wires[w1] ^ wires[w2]
                elif op == 'OR':
                    wires[w3] = wires[w1] | wires[w2]
                elif op == 'AND':
                    wires[w3] = wires[w1] & wires[w2]
                ins_sorted.append([w1, op, w2, w3])
            i += 1

        # add the new base wires
        base += 1
        for wire in base_wires:
            if get_all_numbers(wire) == base:
                wires[wire] = base_wires[wire]

    return ins_sorted


def find_instruction(instructions, w3):
    for i, ins in enumerate(instructions):
        if ins[-1] == w3:
            return i
    return


def init_wires(binx, biny):
    wires = {}
    for i, (xi, yi) in enumerate(zip(binx[::-1], biny[::-1])):
        i = str(i)
        if len(i) == 1:
            i = '0' + i
        wires['x' + i] = int(xi)
        wires['y' + i] = int(yi)
    return wires


def swap(instructions, a, b):
    instructions[a][-1], instructions[b][-1] = instructions[b][-1], instructions[a][-1]
    return instructions


instructions, _, _, _ = get_data(connections)
instructions_sorted = sort_instructions(instructions, wires)
instructions = instructions_sorted

# testing the 'passing on' functionality of the addition
binx = 44 * '0' + '1'
biny = 45 * '1'
wires = init_wires(binx, biny)


def find_lowest_in(instructions):
    wrong_iis = set()
    for i in range(200):
        binx = ''.join([str(random.randint(0, 1)) for _ in range(45)])
        biny = ''.join([str(random.randint(0, 1)) for _ in range(45)])
        wires = init_wires(binx, biny)
        wrong_ins = run(instructions, wires.copy(), xwires, ywires, zwires)
        wrong_iis.add(wrong_ins[-1])

    return sorted(wrong_iis)[0]

# first swap seems to be 59, 60!
instructions = swap(instructions, 59, 60)
# second swap pseems to be 92, 95!
instructions = swap(instructions, 92, 95)
# third swap seems to be 117, 118
instructions = swap(instructions, 117, 118)
# last swap seems to be 184, 186
instructions = swap(instructions, 184, 186)

wrong_ins = run(instructions, wires.copy(), xwires, ywires, zwires)

worst_in = find_lowest_in(instructions)
# print(worst_in)

# try swapping all the instructions between the worst one and the one before it
aa = find_instruction(instructions, 'z' + str(get_all_numbers(worst_in) - 1))
ab = find_instruction(instructions, worst_in)

# try swapping all instructions between aa and ab and find the value for a and
# b that gives the 'biggest' wrong instruction
# wrong_inss = {}
# for a in range(aa, ab + 1):
#     print(aa, ab, a)
#     for b in range(a + 1, len(instructions)):
#         instructions = swap(instructions, a, b)
#         wrong_ins = find_lowest_in(instructions)
#         wrong_inss[(a, b)] = wrong_ins
#         instructions = swap(instructions, a, b)

# print(sorted(wrong_inss.items(), key=lambda x: x[1], reverse=True)[0])
# print(sorted(wrong_inss.items(), key=lambda x: x[1], reverse=True)[:20])

indices = [59, 60, 92, 95, 117, 118, 184, 186]

names = []
for i, (w1, _, w2, w3) in enumerate(instructions):
    if i in indices:
        names.append(w3)


print(','.join(sorted(names)))


