import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')


def show(grid):
    for row in grid:
        for el in row:
            print(el, end='')
        print()
    print()


C = 50
R = 6
grid = [['.' for c in range(C)] for r in range(R)]

for line in L:
    next_grid = deepcopy(grid)
    args = line.split()
    if args[0] == 'rect':
        width, height = args[1].split('x')
        width, height = int(width), int(height)
        for c in range(width):
            for r in range(height):
                next_grid[r][c] = '#'
    elif args[1] == 'row':
        r = int(args[2].split('=')[1])
        shift = int(args[-1])
        for c in range(C):
            next_grid[r][(c + shift) % C] = grid[r][c]
    elif args[1] == 'column':
        c = int(args[2].split('=')[1])
        shift = int(args[-1])
        for r in range(R):
            next_grid[(r + shift) % R][c] = grid[r][c]

    grid = next_grid

p1 = 0
for row in grid:
    for el in row:
        if el == '#':
            p1 += 1

print(p1)
show(grid)
