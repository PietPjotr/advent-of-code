import parser
from collections import deque

def deel1(lines):
    pass

def deel2(lines):
    pass

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


def find_path(blizzards, x_max, y_max, target_pos, start_pos):
    current_positions = {start_pos}
    for i in range(1000):
        next_positions = set()
        blizzards = update_blizzards(blizzards, x_max, y_max)
        occupied = set([el[1:] for el in blizzards])
        positions = get_available_positions(occupied, x_max, y_max)

        for pos in current_positions:
            x, y = pos
            if pos == target_pos:
                print("exit found:", i)
                return blizzards, i

            if (x, y) in positions:
                next_positions.add((x, y))
            if (x + 1, y) in positions:
                next_positions.add((x + 1, y))
            if (x - 1, y) in positions:
                next_positions.add((x - 1, y))
            if (x, y + 1) in positions:
                next_positions.add((x, y + 1))
            if (x, y - 1) in positions:
                next_positions.add((x, y - 1))
        # s = sorted(list(positions), key=lambda x: (x[1], x[0]))
        # print("available positions:", s)
        # sn = sorted(list(next_positions), key=lambda x: (x[1], x[0]))
        # print("next positions:", sn)
        # sc = sorted(list(current_positions), key=lambda x: (x[1], x[0]))
        # print("current positions:", sc)

        current_positions = next_positions.copy()

        # show(blizzards, x_max, y_max)
        # show_pos(current_positions, x_max, y_max)
        print(i + 1)


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

    time = 0
    target_pos = (x_max, y_max + 1)
    start_pos = (1, 0)
    blizzards, i = find_path(blizzards, x_max, y_max, target_pos, start_pos)
    time += i

    target_pos = (1, 0)
    start_pos = (x_max, y_max + 1)
    blizzards, i = find_path(blizzards, x_max, y_max, target_pos, start_pos)
    time += i

    target_pos = (x_max, y_max + 1)
    start_pos = (1, 0)
    blizzards, i = find_path(blizzards, x_max, y_max, target_pos, start_pos)
    time += i

    print("time:", time + 2)




    # res = find_path(all_available, target_pos)
    # print(res)
    # print(target_pos)


if __name__ == "__main__":
    main()