import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')

i = 0
lines = []
section = []
for line in L:
    if line:
        section.append(line)
    else:
        lines.append(section)
        section = []
lines.append(section)

start_state = lines[0][0][-2]
steps = int(lines[0][1].split()[-2])
lines = lines[1:]
transform = {}
for section in lines:
    inner = {}
    state = section[0][-2]
    val1, val2 = section[1][-2], section[5][-2]
    w1, m1, c1 = section[2][-2], section[3][-3], section[4][-2]
    w2, m2, c2 = section[6][-2], section[7][-3], section[8][-2]

    m1 = {'h': 1, 'f':-1}[m1]
    m2 = {'h': 1, 'f':-1}[m2]
    w1 = int(w1)
    w2 = int(w2)
    val1 = int(val1)
    val2 = int(val2)

    inner[val1] = (w1, m1, c1)
    inner[val2] = (w2, m2, c2)
    transform[state] = inner

tape = [0 for i in range(2 * steps)]
index = len(tape) // 2
state = start_state
for _ in range(steps):
    # print(tape, index, state)
    cur_value = tape[index]
    write, move, new_state = transform[state][cur_value]
    tape[index] = write
    index -= move
    state = new_state

print(tape.count(1))
