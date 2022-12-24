import parser

def deel1(elves):
    dirs = ['N', 'S', 'W', 'E']

    for i in range(10):
        suggestions = get_suggestions(elves, dirs)

        for elf, suggestion in suggestions.items():
            elves.remove(elf)
            elves.add(suggestion)

        s = dirs.pop(0)
        dirs.append(s)

    print("part1: {}".format(get_res(elves)))

def deel2(elves):
    dirs = ['N', 'S', 'W', 'E']

    for i in range(10000):
        suggestions = get_suggestions(elves, dirs)
        if len(suggestions) == 0:
            break

        for elf, suggestion in suggestions.items():
            elves.remove(elf)
            elves.add(suggestion)

        s = dirs.pop(0)
        dirs.append(s)

    print("part2: {}".format(i + 1))

def print_elves(elves):
    x_max = 0
    x_min = 0
    y_max = 0
    y_min = 0
    offset = 2
    for elf in elves:
        x, y = elf
        if x > x_max:
            x_max = x
        elif x < x_min:
            x_min = x
        if y > y_max:
            y_max = y
        elif y < y_min:
            y_min = y

    x_max = 10
    x_min = 0
    y_max = 10
    y_min = 0


    grid = [['.' for _ in range(x_min, x_max + offset + 1)] for _ in range(y_min, y_max + offset + 1)]
    for elf in elves:
        x, y = elf
        grid[y + offset][x + offset] = '#'

    res = []
    for row in grid:
        ress = ''
        for el in row:
            ress += el
        res.append(ress)

    for row in res:
        print(row)


def update_suggestions(suggestions, invalid_positions, pos, elf):
    if pos in suggestions.values():
        invalid_positions.add(pos)
        for elf1, suggestion in suggestions.items():
            if suggestion == pos:
                break
        suggestions.pop(elf1)
    elif pos not in invalid_positions:
        suggestions[elf] = pos

    return suggestions, invalid_positions

def get_suggestions(elves, dirs):
    suggestions = {}
    invalid_positions = set()
    for elf in elves:
        x, y = elf
        neighs = []
        for i in [1, 0, -1]:
            for j in [1, 0, -1]:
                if i == 0 and j == 0:
                    continue
                if (x + i, y + j) not in elves:
                    neighs.append(False)
                else:
                    neighs.append(True)

        if not any(neighs):
            continue
        else:
            for dir in dirs:
                neighs = False
                if dir == 'N':
                    for i in [1, 0, -1]:
                        if (x + i, y - 1) in elves:
                            neighs = True
                    if not neighs:
                        pos = (x, y - 1)
                        update_suggestions(suggestions, invalid_positions, pos, elf)
                        break
                elif dir == 'S':
                    for i in [1, 0, -1]:
                        if (x + i, y + 1) in elves:
                            neighs = True
                    if not neighs:
                        pos = (x, y + 1)
                        update_suggestions(suggestions, invalid_positions, pos, elf)
                        break
                elif dir == 'W':
                    for j in [1, 0, -1]:
                        if (x - 1, y + j) in elves:
                            neighs = True
                    if not neighs:
                        pos = (x - 1, y)
                        update_suggestions(suggestions, invalid_positions, pos, elf)
                        break
                elif dir == 'E':
                    for j in [1, 0, -1]:
                        if (x + 1, y + j) in elves:
                            neighs = True
                    if not neighs:
                        pos = (x + 1, y)
                        update_suggestions(suggestions, invalid_positions, pos, elf)
                        break

    return suggestions


def get_res(elves):
    x_max = 0
    x_min = float('inf')
    y_max = 0
    y_min = float('inf')
    for elf in elves:
        x, y = elf
        if x > x_max:
            x_max = x
        elif x < x_min:
            x_min = x
        if y > y_max:
            y_max = y
        elif y < y_min:
            y_min = y

    res = 0
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if (i, j) not in elves:
                res += 1
    return res


def main():
    lines = parser.input_as_lines('inputs/dag23.txt')
    # lines = parser.input_as_lines('inputs/dag23_test.txt')

    elves = set()
    for i, line in enumerate(lines):
        for j, el in enumerate(line):
            if el == '#':
                elves.add((j, i))

    deel1(elves.copy())
    deel2(elves.copy())


if __name__ == "__main__":
    main()