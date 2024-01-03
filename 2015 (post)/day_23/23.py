import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

registers = {}
inss = []
for line in L:
    line = line.replace(',', '')
    line = line.split(' ')

    if len(line) == 3 or line[0] == 'jmp':
        offset = line[-1]
        if offset[0] == '+':
            offset = int(offset[1:])
        elif offset[0] == '-':
            offset = -int(offset[1:])
        line[-1] = offset
    else:
        if line[1] not in registers:
            registers[line[1]] = 0

    inss.append(line)

registers['a'] = 1
i = 0
while 0 <= i < len(inss):
    ins = inss[i]
    if ins[0] == 'hlf':
        registers[ins[1]] //= 2
        i += 1
    elif ins[0] == 'tpl':
        registers[ins[1]] *= 3
        i += 1
    elif ins[0] == 'inc':
        registers[ins[1]] += 1
        i += 1
    elif ins[0] == 'jmp':
        i += ins[1]
    elif ins[0] == 'jie':
        if registers[ins[1]] % 2 == 0:
            i += ins[2]
        else:
            i += 1
    elif ins[0] == 'jio':
        if registers[ins[1]] == 1:
            i += ins[2]
        else:
            i += 1

print(registers)