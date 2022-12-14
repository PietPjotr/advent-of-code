import parser

# Decides the character used to represent the air in the cave.
air = '.'

def print_grid(grid):
    for row in grid:
        for el in row[400:570]:
            print(el, end='')
        print()

def store_grid(grid):
    with open('grid.txt', 'w') as f:
        for row in grid:

            f.write(''.join(row))
        # f.write('\n')

"""
Drops sand in the grid from starting positiion (sx, sy) and returns True if sand dropped and False if sand did not 
drop.
"""
def dropsand(sx, sy, grid):
    i = sy
    j = sx
    while True:
        if grid[i + 1][j] == air:
            i += 1
        elif j - 1 > 0 and grid[i + 1][j - 1] == air:
            i += 1
            j -= 1
        elif j + 1 < len(grid[0]) and grid[i + 1][j + 1] == air:
            i += 1
            j += 1
        else:
            grid[i][j] = 'o'
            if i == sy and j == sx:
                return False
            return True
        if 0 < i < len(grid) - 1:
            continue
        # sand falling infinitely returning false since sand did not drop.
        else:
            return False

def part(part):
    lines = parser.input_as_lines('inputs/dag14.txt')
    # lines = parser.input_as_lines('inputs/dag14_test.txt')

    instructions = []
    for line in lines:
        line = line.strip().split(' -> ')
        ins = []
        for coord in line:
            x, y = coord.split(',')
            ins.append([int(x), int(y)])
        instructions.append(ins)

    xs = []
    ys = []
    for ins in instructions:
        for el in ins:
            xs.append(el[0])
            ys.append(el[1])

    max_x = max(xs)
    max_y = max(ys)

    if part == 2:
        extension_right = 500
        instructions.append([[0, max_y + 2], [max_x + extension_right, max_y + 2]])
        max_y += 2
        max_x += extension_right

    grid = [[air for x in range(max_x + 1)] for y in range(max_y + 1)]

    for ins in instructions:
        for i in range(len(ins) - 1):

            fro = ins[i]
            to = ins[i + 1]
            if fro[0] == to[0]:
                for dy in range(0, abs(to[1] - fro[1]) + 1):
                    start_y = min(fro[1], to[1])
                    grid[start_y + dy][fro[0]] = '#'
            elif fro[1] == to[1]:
                for dx in range(0, abs(to[0] - fro[0]) + 1):
                    start_x = min(fro[0], to[0])
                    grid[fro[1]][start_x + dx] = '#'

    sx = 500
    sy = 0
    grid[sy][sx] = '+'
    sand = 0

    while dropsand(sx, sy, grid):
        # print_grid(grid)
        sand += 1

    # turn on to show the sand in the grid.
    # print_grid(grid)
    if part == 1:
        print(sand)
    elif part == 2:
        print(sand + 1)

def main():
    part(1)
    part(2)


if __name__ == "__main__":
    main()