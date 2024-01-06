import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
# G = G = [[el for el in line] for line in L]
# R = len(G)
# C = len(G[0])

inss = L[0]
dirs = ['north', 'east', 'south', 'west']

inss = inss.split(', ')
direction = 'north'
x = 0
y = 0
visited = [(0,0)]
p2 = -1
for ins in inss:
    turn, steps = ins[0], int(ins[1:])
    if turn == 'R':
        direction = dirs[(dirs.index(direction) + 1) % 4]
    elif turn == 'L':
        direction = dirs[(dirs.index(direction) - 1) % 4]

    for step in range(steps):
        if direction == 'north':
            y += 1
        elif direction == 'south':
            y -= 1
        elif direction == 'east':
            x += 1
        elif direction == 'west':
            x -= 1

        if (x, y) in visited and p2 < 0:
            p2 = abs(x) + abs(y)

        visited.append((x, y))


print(abs(x) + abs(y))
print(p2)
