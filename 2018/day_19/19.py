import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

bound, L = L[0], L[1:]
bound = int(bound[-1])


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


def get_num(regs):
    i = 0
    for j in range(50):
        ins = L[i]
        ins_name, *rest = ins.split()
        a, b, c = [int(el) for el in rest]

        regs[bound] = i

        regs = apply(ins_name, a, b, c, regs)

        i = regs[bound]
        i += 1

    return regs[4]


# found out that the program just finds the sum of all the divisors
# of the number in register 4
def find_divisors(s):
    divs = set([1, s])
    for i in range(1, int(s **.5) + 1):
        if s % i == 0:
            divs.add(i)
            divs.add(s // i)

    return sum(list(divs))


regs1 = [0, 0, 0, 0, 0, 0]
print(find_divisors(get_num(regs1)))

regs2 = [1, 0, 0, 0, 0, 0]
print(find_divisors(get_num(regs2)))
