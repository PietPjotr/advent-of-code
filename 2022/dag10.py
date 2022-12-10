import parser

def deel1(lines):
    cycle = 0
    reg1 = 1
    vals = []

    for line in lines:
        line = line.split(' ')
        cycle += 1

        if cycle == 20 or (cycle - 20) % 40 == 0:
            vals.append(reg1 * cycle)

        if line[0] == 'addx':
            cycle += 1

            if cycle == 20 or (cycle - 20) % 40 == 0:
                vals.append(reg1 * cycle)

            reg1 += int(line[1])

    print(sum(vals))

def deel2(lines):
    cycle = 0
    reg1 = 1
    screen = []

    row = ''
    for line in lines:
        line = line.split(' ')
        cycle += 1
        offset = 40 * len(screen) + 1

        if cycle in range(reg1 - 1 + offset, reg1 + 2 + offset):
            row += '#'
        else:
            row += '.'

        if cycle % 40 == 0:
            screen.append(row)
            row = ''

        if line[0] == 'addx':
            cycle += 1
            offset = 40 * len(screen) + 1

            if cycle in range(reg1 - 1 + offset, reg1 + 2 + offset):
                row += '#'
            else:
                row += '.'

            if cycle % 40 == 0:
                screen.append(row)
                row = ''

            reg1 += int(line[1])

    for row in screen:
        print(row)


def main():
    lines = parser.input_as_lines('inputs/dag10.txt')
    # lines = parser.input_as_lines('inputs/dag10_test.txt')

    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()