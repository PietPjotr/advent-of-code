import sys
sys.path.append('..')
import my_parser as p


L = p.input_as_lines('inputs/inp.txt')


def solve(regs):
    i = 0
    while 0 <= i < len(L):
        ins = L[i]
        ins = ins.split()
        if ins[0] == 'cpy':
            reg = ins[-1]
            if ins[1].isdigit():
                regs[reg] = int(ins[1])
            else:
                regs[reg] = regs[ins[1]]
        elif ins[0] == 'inc':
            regs[ins[-1]] += 1
        elif ins[0] == 'dec':
            regs[ins[-1]] -= 1
        elif ins[0] == 'jnz':
            offset = int(ins[-1])
            if ins[1].isdigit():
                if int(ins[1]) != 0:
                    i += offset - 1
            elif regs[ins[1]] != 0:
                i += offset - 1
        else:
            print('something is wrong')
        i += 1

    print(regs['a'])

regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
solve(regs)
regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
solve(regs)
