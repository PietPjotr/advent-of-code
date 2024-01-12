import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

lines1 = [int(el) for el in L]
lines2 = [int(el) for el in L]

i = 0
steps = 0
while 0 <= i < len(lines1):
    jump = lines1[i]
    lines1[i] += 1
    i += jump
    steps += 1

print(steps)

i = 0
steps = 0
while 0 <= i < len(lines2):
    jump = lines2[i]
    if jump >= 3:
        lines2[i] -= 1
    else:
        lines2[i] += 1
    i += jump
    steps += 1

print(steps)
