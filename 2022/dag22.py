import parser
import re

def deel1(lines):
    pass

def deel2(lines):
    pass

def get_col(pos, grid):
    x, y = pos
    col = ''
    for line in grid:
        if len(line) > x:
            col += line[x]
    return col


def get_row(pos, grid):
    x, y = pos
    row = grid[y]
    return row


def change_dir(dir, turn):
    dirs = ['N', 'E', 'S', 'W']
    if turn == 'R':
        return dirs[(dirs.index(dir) + 1) % 4]
    else:
        return dirs[(dirs.index(dir) - 1) % 4]


def move(grid, pos, dir, steps, path=[]):
    x, y = pos
    row = get_row(pos, grid)
    col = get_col(pos, grid)

    offset_x = row.index('.') if '#' not in row else min(row.index('.'), row.index('#'))
    offset_y = col.index('.') if '#' not in col else min(col.index('.'), col.index('#'))
    row = row.strip()
    col = col.strip()

    # walking in the x direction
    if dir == 'W':
        for step in range(steps):
            x, y = pos
            next_i = (x - offset_x - 1) % len(row)
            if row[next_i] != '#':
                pos[0] = (x - offset_x - 1) % len(row) + offset_x
                path.append(pos.copy())
            else:
                break

    elif dir == 'E':
        for step in range(steps):
            x, y = pos
            next_i = (x - offset_x + 1) % len(row)
            if row[next_i] != '#':
                pos[0] = (x - offset_x + 1) % len(row) + offset_x
                path.append(pos.copy())
            else:
                break


    # walking in the y direction
    elif dir == 'N':
        for step in range(steps):
            x, y = pos
            next_i = (y - offset_y - 1) % len(col)
            if col[next_i] != '#':
                pos[1] = (y - offset_y - 1) % len(col) + offset_y
                path.append(pos.copy())
            else:
                break

    elif dir == 'S':
        for step in range(steps):
            x, y = pos
            next_i = (y - offset_y + 1) % len(col)
            if col[next_i] != '#':
                pos[1] = (y - offset_y + 1) % len(col) + offset_y
                path.append(pos.copy())
            else:
                break
    else:
        print("wrong direction detected:", dir)
        return

    return pos, path


def main():
    lines = parser.input_as_lines('inputs/dag22.txt')
    # lines = parser.input_as_lines('inputs/dag22_test.txt')
    ins = lines[-1]
    grid = []
    for line in lines[:-2]:
        grid.append(line)

    ins = list(ins)
    instructions = []
    instruction = ''
    for el in ins:
        if el == 'R' or el == 'L':
            instructions.append(instruction)
            instructions.append(el)
            instruction = ''
        else:
            instruction += el

    instructions.append(instruction)

    row = grid[0]
    offset = row.index('.') if '#' not in row else min(row.index('.'), row.index('#'))

    pos = [offset, 0]
    dir = 'E'
    path = []

    for i, ins in enumerate(instructions):
        if ins.isnumeric():
            pos, path = move(grid, pos, dir, int(ins), path)
        else:
            dir = change_dir(dir, ins)

    dirs = ['E', 'S', 'W', 'N']
    col = pos[0] + 1
    row = pos[1] + 1

    print(1000 * row + 4 * col + dirs.index(dir))


if __name__ == "__main__":
    main()