import parser


def show(grid, x_max=5, y_max=5):
    x_min, y_min = 1, 1
    print('#.' + x_max * '#')
    for y in range(y_min, y_max + 1):
        row = '#'
        for x in range(x_min, x_max + 1):
            amount = 0
            char = 'O'
            for dir in ['>', 'v', '<', '^']:
                if (dir, x, y) in grid:
                    amount += 1
                    char = dir
            if amount == 0:
                row += '.'
            elif amount == 1:
                row += char
            else:
                row += str(amount)

        print(row + '#')
    print(x_max * '#' + '.#')


def show_pos(positions, x_max, y_max):
    x_min, y_min = 1, 1
    print('#.' + x_max * '#')
    for y in range(y_min, y_max + 1):
        row = '#'
        for x in range(x_min, x_max + 1):
            if (x, y) in positions:
                row += 'o'
            else:
                row += '.'
        print(row + '#')
    if (x_max, y_max + 1) in positions:
        print(x_max * '#' + 'o#')
    else:
        print(x_max * '#' + '.#')


def update_blizzards(blizzards, x_max=5, y_max=5):
    x_min, y_min = 1, 1
    next_ = set()
    for bliz in blizzards:
        if bliz[0] == '>':
            if bliz[1] == x_max:
                new_x = x_min
            else:
                new_x = bliz[1] + 1
            next_.add(('>', new_x, bliz[2]))
        elif bliz[0] == '<':
            if bliz[1] == x_min:
                new_x = x_max
            else:
                new_x = bliz[1] - 1
            next_.add(('<', new_x, bliz[2]))
        elif bliz[0] == 'v':
            if bliz[2] == y_max:
                new_y = y_min
            else:
                new_y = bliz[2] + 1
            next_.add(('v', bliz[1], new_y))
        elif bliz[0] == '^':
            if bliz[2] == y_min:
                new_y = y_max
            else:
                new_y = bliz[2] - 1
            next_.add(('^', bliz[1], new_y))
    return next_.copy()


def find_path(blizzards, x_max, y_max, start_pos, target_pos):
    neighs = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    current_positions = {start_pos}
    # arbitrary loop value, should never be exceeded
    for i in range(1000):
        next_positions = set()
        blizzards = update_blizzards(blizzards, x_max, y_max)
        occupied = set([el[1:] for el in blizzards])
        positions = get_available_positions(occupied, x_max, y_max)

        for pos in current_positions:
            x, y = pos
            if pos == target_pos:
                return blizzards, i

            for neigh in neighs:
                new_pos = (x + neigh[0], y + neigh[1])
                if new_pos in positions:
                    next_positions.add(new_pos)

        current_positions = next_positions.copy()


def get_available_positions(positions, x_max, y_max):
    x_min, y_min = 1, 1
    available = set()
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if (x, y) not in positions:
                available.add((x, y))
    target_pos = (x_max, y_max + 1)
    start = (1, 0)
    available.add(target_pos)
    available.add(start)
    return available


def main():
    lines = parser.input_as_lines('inputs/dag24.txt')
    # lines = parser.input_as_lines('inputs/dag24_test.txt')
    blizzards = set()

    for i, line in enumerate(lines):
        for j, el in enumerate(line):
            if el in ['>', 'v', '<', '^']:
                blizzards.add((el, j, i))

    x_max = len(lines[0]) - 2
    y_max = len(lines) - 2

    start_pos = (1, 0)
    end_pos = (x_max, y_max + 1)

    time = 0
    blizzards, i = find_path(blizzards, x_max, y_max, start_pos, end_pos)
    time += i
    print("part1:", time)

    blizzards, i = find_path(blizzards, x_max, y_max, end_pos, start_pos)
    time += i

    blizzards, i = find_path(blizzards, x_max, y_max, start_pos, end_pos)
    time += i

    print("part2:", time + 2)


if __name__ == "__main__":
    main()