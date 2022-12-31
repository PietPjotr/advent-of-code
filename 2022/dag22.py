import parser

# foldage into the cube
#   BBRR
#   BBRR
#   TT
#   TT
# LLFF
# LLFF
# DD
# DD

# T: 50, 100, 50, 100
# F: 50, 100, 100, 150
# L: 0, 50, 100, 150
# D: 0, 50, 150, 200
# B: 50, 100, 0, 50
# R: 100, 150, 0, 50
# maps the the face to its x and y ranges. To check if a position is on a certain face check for x1 < x <= x2 and y1 < y <= y2
faces = {'T': (50, 100, 50, 100), 'F': (50, 100, 100, 150), 'L': (0, 50, 100, 150), 'D': (0, 50, 150, 200),
         'B': (50, 100, 0, 50), 'R': (100, 150, 0, 50)}


# foldage into the cube
#     BB
#     BB
# DDLLTT
# DDLLTT
#     FFRR
#     FFRR

# B: 8, 12, 0, 4
# T: 8, 12, 4, 8
# F: 8, 12, 8, 12
# D: 0, 4, 4, 8
# L: 4, 8, 4, 8
# R: 12, 16, 8, 12
# used for the test input
# faces = {'T': (8, 12, 4, 8), 'F': (8, 12, 8, 12), 'L': (4, 8, 4, 8), 'D': (0, 4, 4, 8), 'B': (8, 12, 0, 4), 'R': (12, 16, 8, 12)}


def get_col(pos, grid):
    x, y = pos
    col = ''
    for line in grid:
        if len(line) > x:
            col += line[x]
    return col


def get_row(pos, grid):
    x, y = pos
    return grid[y]


# finds the face that the position is on and returns the face and the ranges of the face
def get_face(pos):
    x, y = pos
    for face, (x1, x2, y1, y2) in faces.items():
        if x1 <= x < x2 and y1 <= y < y2:
            return face, (x1, x2, y1, y2)


# This function is used for the move function for par`
def get_row2(pos, grid, ranges):
    x, y = pos
    row = ''
    for i in range(ranges[0], ranges[1]):
        row += grid[y][i]

    return row


# this function is used for the move function for part 2
def get_col2(pos, grid, ranges):
    x, y = pos
    col = ''
    for j in range(ranges[2], ranges[3]):
        col += grid[j][x]

    return col


def change_dir(dir, turn):
    dirs = ['N', 'E', 'S', 'W']
    if turn == 'R':
        return dirs[(dirs.index(dir) + 1) % 4]
    else:
        return dirs[(dirs.index(dir) - 1) % 4]


def move(grid, pos, dir, steps, path=[]):
    row = get_row(pos, grid)
    col = get_col(pos, grid)
    offset_x = row.index('.') if '#' not in row else min(row.index('.'), row.index('#'))
    offset_y = col.index('.') if '#' not in col else min(col.index('.'), col.index('#'))
    row = row.strip()
    col = col.strip()

    translate = {'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'N': (0, -1)}

    # walking in the x direction
    if dir == 'W' or dir == 'E':
        delta = translate[dir][0]

        for step in range(steps):
            x, y = pos
            next_i = (x - offset_x + delta) % len(row)
            if row[next_i] != '#':
                pos[0] = (x - offset_x + delta) % len(row) + offset_x
                path.append(pos.copy())
            else:
                break

    # walking in the y direction
    elif dir == 'N' or dir == 'S':
        delta = translate[dir][1]
        for step in range(steps):
            x, y = pos
            next_i = (y - offset_y + delta) % len(col)
            if col[next_i] != '#':
                pos[1] = (y - offset_y + delta) % len(col) + offset_y
                path.append(pos.copy())
            else:
                break
    else:
        print("wrong direction detected:", dir)
        return

    return pos, path


# this function is used to determine the new face we have just moved to and returns the name of the new face
def get_new_face(face, pos):
    x, y = pos
    if face == 'F':
        if x < 50:
            return 'L'
        elif x >= 100:
            return 'R'
        elif y >= 150:
            return 'D'
        elif y < 100:
            return 'T'
        else:
            print("no new face found for F")
            return 'F'
    elif face == 'B':
        if x < 50:
            return 'L'
        elif x >= 100:
            return 'R'
        elif y < 0:
            return 'D'
        elif y >= 50:
            return 'T'
        else:
            print("no new face found for D")
            return 'B'
    elif face == 'T':
        if x < 50:
            return 'L'
        elif x >= 100:
            return 'R'
        elif y < 50:
            return 'B'
        elif y >= 100:
            return 'F'
        else:
            print("no new face found for T")
            return 'T'
    elif face == 'D':
        if x < 0:
            return 'B'
        elif x >= 50:
            return 'F'
        elif y < 150:
            return 'L'
        elif y >= 200:
            return 'R'
        else:
            print("no new face found for D")
            return 'D'
    elif face == 'L':
        if x < 0:
            return 'B'
        elif x >= 50:
            return 'F'
        elif y < 100:
            return 'T'
        elif y >= 150:
            return 'D'
        else:
            print("no new face found for L")
            return 'L'
    elif face == 'R':
        if x < 100:
            return 'B'
        elif x >= 150:
            return 'F'
        elif y < 0:
            return 'D'
        elif y >= 50:
            return 'T'
        else:
            print("no new face found for R")
            return 'R'
    else:
        print("error")
        return None

# foldage into the cube
#   BBRR
#   BBRR
#   TT
#   TT
# LLFF
# LLFF
# DD
# DD


transform = {('T', 'R'): ('L', lambda x, y: (100 + (y - 50), 49)), ('T', 'L'): ('L', lambda x, y: (0 + (y - 50), 100)),
             ('T', 'B'): ('', lambda x, y: (x, y)), ('T', 'F'): ('', lambda x, y: (x, y)),
             ('F', 'R'): ('RR', lambda x, y: (149, 49 - (y - 100))), ('F', 'L'): ('', lambda x, y: (x, y)),
             ('F', 'T'): ('', lambda x, y: (x, y)), ('F', 'D'): ('R', lambda x, y: (49, 150 + (x - 50))),
             ('L', 'T'): ('R', lambda x, y: (50, 50 + x)), ('L', 'F'): ('', lambda x, y: (x, y)),
             ('L', 'B'): ('RR', lambda x, y: (50, 49 - (y - 100))), ('L', 'D'): ('', lambda x, y: (x, y)),
             ('D', 'R'): ('', lambda x, y: (100 + x, 0)), ('D', 'L'): ('', lambda x, y: (x, y)),
             ('D', 'B'): ('L', lambda x, y: (50 + (y - 150), 0)), ('D', 'F'): ('L', lambda x, y: (50 + (y - 150), 149)),
             ('B', 'R'): ('', lambda x, y: (x, y)), ('B', 'T'): ('', lambda x, y: (x, y)),
             ('B', 'L'): ('RR', lambda x, y: (0, 100 + 49 - y)), ('B', 'D'): ('R', lambda x, y: (0, 150 + (x - 50))),
             ('R', 'B'): ('', lambda x, y: (x, y)), ('R', 'T'): ('R', lambda x, y: (99, 50 + (x - 100))),
             ('R', 'F'): ('RR', lambda x, y: (99, 100 + (49 - y))), ('R', 'D'): ('', lambda x, y: (0 + (x - 100), 199))
             }


# foldage into the cube
#     BB
#     BB
# DDLLTT
# DDLLTT
#     FFRR
#     FFRR


# used to test the the main function using the test input on the website
# transform = {('T', 'R'): ('R', lambda x, y: (15 - (y - 4), 8)), ('T', 'L'): ('', lambda x, y: (x, y)),
#              ('T', 'B'): ('', lambda x, y: (x, y)), ('T', 'F'): ('', lambda x, y: (x, y)),
#              ('F', 'R'): ('', lambda x, y: (x, y)), ('F', 'L'): ('R', lambda x, y: (7 - (y - 8), 7)),
#              ('F', 'T'): ('', lambda x, y: (x, y)), ('F', 'D'): ('RR', lambda x, y: (3 - (x - 8), 7)),
#              ('L', 'T'): ('', lambda x, y: (x, y)), ('L', 'F'): ('L', lambda x, y: (8, 8 + (x - 4))),
#              ('L', 'B'): ('R', lambda x, y: (8, (x - 4))), ('L', 'D'): ('', lambda x, y: (x, y)),
#              ('D', 'R'): ('R', lambda x, y: (8 + (y - 4))), ('D', 'L'): ('', lambda x, y: (x, y)),
#              ('D', 'B'): ('RR', lambda x, y: (11 - (y - 4), 0)), ('D', 'F'): ('LL', lambda x, y: (11 - x, 11)),
#              ('B', 'R'): ('RR', lambda x, y: (15, 11 - y)), ('B', 'T'): ('', lambda x, y: (x, y)),
#              ('B', 'L'): ('L', lambda x, y: (4 + y, 4)), ('B', 'D'): ('RR', lambda x, y: (3 - (x - 8), 4)),
#              ('R', 'B'): ('RR', lambda x, y: (11, 3 - (y - 8))), ('R', 'T'): ('L', lambda x, y: (11, 7 - (x - 12))),
#              ('R', 'F'): ('', lambda x, y: (x, y)), ('R', 'D'): ('R', lambda x, y: (0, 7 - (x - 12)))
#              }

# same here, function implemented to test the test input on the website
def get_new_face2(face, pos):
    x, y = pos
    if face == 'F':
        if x < 8:
            return 'L'
        elif x >= 12:
            return 'R'
        elif y >= 12:
            return 'D'
        elif y < 8:
            return 'T'
        else:
            print("no new face found for F", pos)
            return 'F'
    elif face == 'B':
        if x < 8:
            return 'L'
        elif x >= 12:
            return 'R'
        elif y < 0:
            return 'D'
        elif y >= 4:
            return 'T'
        else:
            print("no new face found for D", pos)
            return 'B'
    elif face == 'T':
        if x < 8:
            return 'L'
        elif x >= 12:
            return 'R'
        elif y < 4:
            return 'B'
        elif y >= 8:
            return 'F'
        else:
            print("no new face found for T", pos)
            return 'T'
    elif face == 'D':
        if x < 0:
            return 'R'
        elif x >= 4:
            return 'L'
        elif y < 4:
            return 'B'
        elif y >= 8:
            return 'F'
        else:
            print("no new face found for D", pos)
            return 'D'
    elif face == 'L':
        if x < 4:
            return 'D'
        elif x >= 8:
            return 'T'
        elif y < 4:
            return 'B'
        elif y >= 8:
            return 'F'
        else:
            print("no new face found for L", pos)
            return 'L'
    elif face == 'R':
        if x < 12:
            return 'F'
        elif x >= 16:
            return 'B'
        elif y < 8:
            return 'T'
        elif y >= 12:
            return 'D'
        else:
            print("no new face found for R", pos)
            return 'R'
    else:
        print("error")
        return None

def move2(grid, pos, dir, steps, path=[], i=0):
    translate = {'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'N': (0, -1)}

    # walking in the x direction
    if dir == 'W' or dir == 'E':
        sign = translate[dir][0]
        face, ranges = get_face(pos)
        row = get_row2(pos, grid, ranges)
        start_i = pos[0] % 50
        start_x = pos[0]

        for step in range(0, steps + 1):
            next_i = + start_i + sign * step
            if 0 <= next_i < len(row):
                if row[next_i] != '#':
                    pos[0] = start_x + sign * step
                    path.append(pos.copy())
                else:
                    break
            # we step onto a new face (since we can never change faces more than once per step instruction this
            # recursive call is safe)
            else:
                x = start_x + sign * step
                y = pos[1]
                new_face = get_new_face(face, [x, y])
                if new_face != face:
                    rotate, f = transform[(face, new_face)]
                    x, y = f(x, y)
                    if grid[y][x] == '#':
                        break

                    # only change direction after we know that we can actually move to the new face
                    for rotation in rotate:
                        dir = change_dir(dir, rotation)

                    # recursive call for the same instruction but on the new face we just stepped onto
                    pos, path, dir = move2(grid, [x, y], dir, steps - step, path, i)
                    return pos, path, dir
                break

    # walking in the y direction
    elif dir == 'N' or dir == 'S':
        sign = translate[dir][1]
        face, ranges = get_face(pos)
        col = get_col2(pos, grid, ranges)
        start_i = pos[1] % 50
        start_y = pos[1]

        for step in range(0, steps + 1):
            next_i = + start_i + sign * step
            if 0 <= next_i < len(col):
                if col[next_i] != '#':
                    pos[1] = start_y + sign * step
                    path.append(pos.copy())
                else:
                    break
            else:
                x = pos[0]
                y = start_y + sign * step
                new_face = get_new_face(face, [x, y])
                if new_face != face:
                    rotate, f = transform[(face, new_face)]
                    x, y = f(x, y)
                    if grid[y][x] == '#':
                        break
                    # only change direction after we know that we can actually move to the new face
                    for rotation in rotate:
                        dir = change_dir(dir, rotation)
                    # recursive call for the same instruction but on the new face we just stepped onto
                    pos, path, dir = move2(grid, [x, y], dir, steps - step, path, i)
                    return pos, path, dir
                break
    else:
        print("wrong direction detected:", dir)
        return

    return pos, path, dir


def main():

    lines = parser.input_as_lines('inputs/dag22.txt')
    # lines = parser.input_as_lines('inputs/dag22_test.txt')
    ins = lines[-1]
    # grid creation
    grid = []
    for line in lines[:-2]:
        grid.append(line)

    # instruction parsing and splitting into 'R', 'L' and 'xsteps' instrustions
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

    # part 1
    pos = [50, 0]
    dir = 'E'
    path = []

    for i, ins in enumerate(instructions):
        if ins.isnumeric():
            pos, path = move(grid, pos, dir, int(ins), path)
        else:
            dir = change_dir(dir, ins)

    # calculating the final score
    dirs = ['E', 'S', 'W', 'N']
    col = pos[0] + 1
    row = pos[1] + 1

    print("part1:", 1000 * row + 4 * col + dirs.index(dir))

    # part 2
    pos = [50, 0]
    dir = 'E'
    path = []

    for i, ins in enumerate(instructions):
        if ins.isnumeric():
            pos, path, dir = move2(grid, pos, dir, int(ins), path, i)
        else:
            dir = change_dir(dir, ins)

    # calculating the final score
    dirs = ['E', 'S', 'W', 'N']
    col = pos[0] + 1
    row = pos[1] + 1

    print("part2:", 1000 * row + 4 * col + dirs.index(dir))


if __name__ == "__main__":
    main()