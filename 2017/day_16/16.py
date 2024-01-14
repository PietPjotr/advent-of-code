import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')[0]
inss = L.split(',')
l = list('abcdefghijklmnop')

loop = ['0']
i = 0
while i < 100:
    for ins in inss:
        c = ins[0]
        if c == 's':
            n = int(ins[1:])
            l = l[-n:] + l[:-n]
        elif c == 'x':
            a, b = [int(el) for el in re.findall(r'\d+', ins)]
            temp = l[a]
            l[a] = l[b]
            l[b] = temp
        elif c == 'p':
            na, nb = re.findall(r'[a-z]+', ins[1:])
            a = l.index(na)
            b = l.index(nb)
            temp = l[a]
            l[a] = l[b]
            l[b] = temp

    state = ''.join(l)
    if state in loop:
        repeat = i
        break
    else:
        loop.append(state)
    i += 1


print(loop[1])
loop_index = 1000000000 % repeat
print(loop[loop_index])
