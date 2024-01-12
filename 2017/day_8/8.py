import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

p2 = 0
regs = {line.split()[0]: 0 for line in L}
for line in L:
    reg, ins, val, _, cond_reg, op, cond_val = line.split()
    if eval(str(regs[cond_reg]) + op + cond_val):
        if ins == 'dec':
            regs[reg] -= int(val)
        elif ins == 'inc':
            regs[reg] += int(val)
        p2 = max(p2, regs[reg])

print(max(list(regs.values())))
print(p2)
