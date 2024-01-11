import sys
sys.path.append('..')
import my_parser as p
import math

L = p.input_as_lines('inputs/inp.txt')


inss = [ins.split() for ins in L]
for ins in inss:
    for i in range(len(ins)):
        try:
            ins[i] = int(ins[i])
        except:
            continue


regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}


def solve():
    i = 0
    while 0 <= i < len(L):
        ins = inss[i]
        if ins[0] == 'cpy':
            regs[ins[2]] = ins[1] if isinstance(ins[1], int) else regs[ins[1]]
        elif ins[0] == 'inc':
            regs[ins[-1]] += 1
        elif ins[0] == 'dec':
            regs[ins[-1]] -= 1
        elif ins[0] == 'jnz':
            val = ins[1] if isinstance(ins[1], int) else regs[ins[1]]
            skip = ins[2] if isinstance(ins[2], int) else regs[ins[2]]
            if val != 0:
                i += skip - 1
        elif ins[0] == 'tgl':
            to_change = i + regs[ins[1]]
            if to_change < len(inss):
                l = inss[to_change]
                if len(l) == 2:
                    if l[0] == 'inc':
                        l[0] = 'dec'
                    else:
                        l[0] = 'inc'
                if len(l) == 3:
                    if l[0] == 'jnz':
                        if not isinstance(l[2], int):
                            l[0] = 'cpy'
                    else:
                        l[0] = 'jnz'
        else:
            print('something is wrong')
        i += 1

    print(regs['a'])


# solve()

print(math.factorial(7) + 6384)
print(math.factorial(12) + 6384)
