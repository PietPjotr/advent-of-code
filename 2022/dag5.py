import parser
import numpy as np


def move(s1, s2):
    s2.append(s1.pop(-1))


def move_multiple(s1, s2, n):
    temp = []
    for i in range(n):
        temp.append(s1.pop(-1))

    s2.extend(temp[::-1])


def main():
    # lines = parser.input_as_string('inputs/.txt')
    lines = parser.input_as_lines('inputs/dag5.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    # deel1(lines)


    #creation of the starting stacks
    grid = []
    for line in lines:
        if line == '':
            break
        row = [char for i, char in enumerate(line) if (i - 1) % 4 == 0]
        grid.append(row)


    grid.pop(-1)
    grid = np.transpose(grid)
    res = []
    for row in grid:
        new = list(filter(lambda x: x != ' ', row))
        res.append(new[::-1])

    all = res

    # actual loop over the commands
    s = 10
    for i, line in enumerate(lines[s:]):
        data = line.split(' ')
        amount = int(data[1])
        fro = int(data[3]) - 1
        to = int(data[5]) - 1

        if amount == 1:
            move(all[int(fro)], all[int(to)])
        # only added for part 2
        elif amount > 1:
            move_multiple(all[int(fro)], all[int(to)], amount)

    # final result string
    result = ''
    for stack in all:
        if stack:
            result += stack[-1]

    print(result)


if __name__ == "__main__":
    main()