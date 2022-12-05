import parser
import numpy as np


def deel1(coords, ins):
    xmax = 0
    ymax = 0
    for el in coords:
        if el[0] > xmax:
            xmax = el[0]
        if el[1] > ymax:
            ymax = el[1]

    grid = [['' for i in range(xmax+1)] for y in range(ymax+1)]

    #initialising
    for el in coords:
        grid[el[1]][el[0]] += '#'
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '':
                grid[i][j] += '.'


    for instruction in ins:
        split = instruction.split(' ')
        im = split[-1]

        if im[0] == 'x':
            number = int(im.split('=')[1])
            grid = fold_left(grid, number)
        elif split[-1][0] == 'y':
            number = int(im.split('=')[1])
            grid = fold_up(grid, number)

    line_s = ''
    for line in grid:
        for el in line:
            print("{}  ".format(el), end="", flush=True)
        print("\n")

    print(get_dots(grid))



def get_dots(grid):
    dots = 0
    for line in grid:
        for el in line:
            if el == '#':
                dots += 1
    return dots



def fold_up(grid, y):

    new_grid = [grid[i] for i in range(y)]
    for i in range(y + 1, len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                if new_grid[y-(i-y)][j] == '.':
                    new_grid[y-(i-y)][j] = '#'

    return new_grid


def fold_left(grid, x):

    new_grid = [[el for el in line[:x]] for line in grid]
    for i in range(len(grid)):
        for j in range(x + 1, len(grid[0])):
            if grid[i][j] == '#':
                if new_grid[i][x-(j-x)] == '.':
                    new_grid[i][x-(j-x)] = '#'

    return new_grid


def deel2(lines):
    pass


def main():
    # lines = parser.input_as_string('inputs/dag13.txt')
    lines = parser.input_as_lines('inputs/dag13.txt')
    # lines = parser.input_as_ints('inputs/dag13.txt')
    # lines = parser.input_as_grid('inputs/dag13.txt')
    coords = []
    ins = []
    for line in lines:
        if line and line[0].isdigit():
            split = line.split(',')
            coords.append([int(split[0]), int(split[1])])
        elif line:
            ins.append(line)
    print(ins)
    deel1(coords, ins)


if __name__ == "__main__":
    main()
