from functools import partial
from aocd.models import Puzzle
import re

inp = open('inputs/inp.txt').read()
nums = [int(el) for el in re.findall(r'\d+', inp)]

registers = nums[:3]
program = nums[3:]


def combo_operand(o):
    return registers[o - 4] if o >= 4 else o

def adv(o, rp):
    registers[rp] = registers[0] >> combo_operand(o)

def bxl(o):
    registers[1] = registers[1] ^ o

def bst(o):
    registers[1] = combo_operand(o) % 8

def jnz(o):
    if registers[0]:
        return o
    return None

def bxc(o):
    registers[1] = registers[1] ^ registers[2]


instructions = {
    0: partial(adv, rp=0),
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: lambda o: combo_operand(o) % 8,
    6: partial(adv, rp=1),
    7: partial(adv, rp=2),
}


def run(register_a=registers[0]):
    out = []
    pointer = 0

    if register_a:
        registers[0] = register_a

    while pointer < len(program):
        inst, arg = program[pointer : pointer + 2]
        r = instructions[inst](arg)

        if inst == 3 and r is not None:
            pointer = r
        else:
            pointer += 2

        if inst == 5:
            out.append(r)

    return out

a = ','.join(str(o) for o in run())
print(a)

# all the programs do the following:

# B becomes A % 8, which is the same as last three bits of A, and B/C follow from there
# A becomes A // (2 ** 3), which is A >> 3 - up to three bits of A are flushed
# output B % 8, which is the last three bits of B
# jump to the beginning, until A = 0

# so every three bits of A maps to a three-bit output, one three-bit chunk at a time
# this narrows the output space enough to brute-force.

ra_possibilities = set(range(8))  # just for the start, can be 1 or 2 bits

for p in range(2, len(program) + 1):
    goal = program[-p:]

    next_possibilities = set()

    for ra_base in ra_possibilities:
        for block in range(8):
            if run(ra := (ra_base << 3) + block) == goal:
                next_possibilities.add(ra)

    ra_possibilities = next_possibilities

b = min(ra_possibilities)
print(b)
