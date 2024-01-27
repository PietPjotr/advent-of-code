import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

bound, L = L[0], L[1:]
bound = int(bound[-1])

inss = []
for ins in L:
    ins_name, *rest = ins.split()
    a, b, c = [int(el) for el in rest]
    inss.append((ins_name, a, b, c))


def apply(ins_name, a, b, c, regs):
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


def solve(inss):
    regs = [0, 0, 0, 0, 0, 0]
    i = 0
    seen = set()
    prev = -1
    while 0 <= i < len(L):
        if i == 28:
            if regs[5] in seen:
                print(prev)
                break
            else:
                seen.add(regs[5])
                prev = regs[5]
                if len(seen) == 1:
                    print(prev)
            print(len(seen))

        ins_name, a, b, c = inss[i]

        regs[bound] = i

        regs = apply(ins_name, a, b, c, regs)

        i = regs[bound]
        i += 1


solve(inss)
