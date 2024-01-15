import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')


def p1(regs):
    i = 0
    p = 0
    while 0 <= i < len(L):
        ins = L[i].split()
        cmd = ins[0]
        reg = ins[1]
        if cmd == 'set':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] = val
        elif cmd == 'sub':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] -= val
        elif cmd == 'mul':
            p += 1
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] *= val
        elif cmd == 'jnz':
            offset = regs[ins[2]] if ins[2] in regs else int(ins[2])
            val = regs[ins[1]] if ins[1] in regs else int(ins[1])
            if val != 0:
                i += offset
                continue
        i += 1
    print(p)


def initialize_registers():
    regs = {}
    for ins in L:
        ins = ins.split()
        reg = ins[1]
        try:
            reg = int(ins[1])
        except ValueError:
            if reg not in regs:
                regs[reg] = 0
    return regs


def solve1():
    regs1 = initialize_registers()
    p1(regs1)


solve1()


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def count_non_prime_numbers(b, c):
    h = 0
    for num in range(b, c + 1, 17):
        if not is_prime(num):
            h += 1
    return h


def solve2():
    # Given b = 105700 and c = 122700, taken from the input
    b = 105700
    c = 122700

    result = count_non_prime_numbers(b, c)
    print(result)


solve2()
