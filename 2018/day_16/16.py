import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')

names = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
         "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]


def apply(ins_name, ins, regs):
    opcode, a, b, c = [int(el) for el in ins]

    if ins_name == "addr":
        regs[c] = regs[a] + regs[b]
    elif ins_name == "addi":
        regs[c] = regs[a] + b
    elif ins_name == "mulr":
        regs[c] = regs[a] * regs[b]
    elif ins_name == "muli":
        regs[c] = regs[a] * b
    elif ins_name == "banr":
        regs[c] = regs[a] & regs[b]
    elif ins_name == "bani":
        regs[c] = regs[a] & b
    elif ins_name == "borr":
        regs[c] = regs[a] | regs[b]
    elif ins_name == "bori":
        regs[c] = regs[a] | b
    elif ins_name == "setr":
        regs[c] = regs[a]
    elif ins_name == "seti":
        regs[c] = a
    elif ins_name == "gtir":
        if a > regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    elif ins_name == "gtri":
        if regs[a] > b:
            regs[c] = 1
        else:
            regs[c] = 0
    elif ins_name == "gtrr":
        if regs[a] > regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    elif ins_name == "eqir":
        if a == regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    elif ins_name == "eqri":
        if regs[a] == b:
            regs[c] = 1
        else:
            regs[c] = 0
    elif ins_name == "eqrr":
        if regs[a] == regs[b]:
            regs[c] = 1
        else:
            regs[c] = 0
    else:
        print('not valid instruction')

    return regs


def p1():
    ps = {}
    i = 0
    p1 = 0
    while i < 3340:
        regs_in = eval(L[i].split(': ')[1])
        ins = L[i + 1].split()
        opcode = ins[0]
        regs_out = eval(L[i + 2].split('  ')[1])
        possible_names = []
        for name in names:
            res = apply(name, ins, deepcopy(regs_in))
            if res == regs_out:
                possible_names.append(name)
        if len(possible_names) >= 3:
            p1 += 1
        if ins[0] in ps:
            for p in possible_names:
                ps[opcode].add(name)
        else:
            ps[opcode] = set(possible_names)

        i += 4
    print(p1)
    return ps


def reduce(ps):
    mapping = {}
    while len(mapping) < 16:
        for opn in set(names) - set(mapping.values()):
            for opcode, operations in ps.items():
                if opn in operations and len(operations) == 1:
                    mapping[opcode] = opn
                    ps.pop(opcode)
                    for k, v in ps.items():
                        if opn in v:
                            v.remove(opn)
                    break

    return mapping


def p2(mapping):
    i = 3342
    regs = [0, 0, 0, 0]
    for ins in L[i:]:
        ins = ins.split()
        regs = apply(mapping[ins[0]], ins, regs)

    print(regs, regs[0])


ps = p1()
mapping = reduce(ps)
p2(mapping)
