import sys
sys.path.append('..')
import my_parser as p


def turn_on(grid, x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    for i in range(delta_x + 1):
        for j in range(delta_y + 1):
            grid[x1+i][y1+j] = True

    return grid


def turn_off(grid, x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    for i in range(delta_x + 1):
        for j in range(delta_y + 1):
            grid[x1+i][y1+j] = False

    return grid


def toggle(grid, x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    for i in range(delta_x + 1):
        for j in range(delta_y + 1):
            if grid[x1+i][y1+j] == True:
                grid[x1+i][y1+j] = False
            else:
                grid[x1+i][y1+j] = True
    return grid


def deel1(lines):
    grid = [[False for i in range(1000)] for j in range(1000)]
    for line in lines:
        if line[0] == 'turn':
            [x1, y1] = [int(line[2].split(',')[0]), int(line[2].split(',')[1])]
            [x2, y2] = [int(line[-1].split(',')[0]),
                        int(line[-1].split(',')[1])]

            if line[1] == 'on':
                # print(x1,y1,x2,y2)
                grid = turn_on(grid, x1, y1, x2, y2)
            else:
                grid = turn_off(grid, x1, y1, x2, y2)
        else:
            # print(line[1])
            [x1, y1] = [int(line[1].split(',')[0]), int(line[1].split(',')[1])]
            [x2, y2] = [int(line[-1].split(',')[0]),
                        int(line[-1].split(',')[1])]
            grid = toggle(grid, x1, y1, x2, y2)

    lights = 0
    for line in grid:
        for light in line:
            if light == True:
                lights += 1
    print(lights)


def turn_on2(grid, x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    for i in range(delta_x + 1):
        for j in range(delta_y + 1):
            grid[x1+i][y1+j] += 1

    return grid


def turn_off2(grid, x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    for i in range(delta_x + 1):
        for j in range(delta_y + 1):
            if grid[x1+i][y1+j] >= 1:
                grid[x1+i][y1+j] -= 1

    return grid


def toggle2(grid, x1, y1, x2, y2):
    delta_x = abs(x1 - x2)
    delta_y = abs(y1 - y2)

    for i in range(delta_x + 1):
        for j in range(delta_y + 1):
            grid[x1+i][y1+j] += 2

    return grid


def deel2(lines):
    grid = [[False for i in range(1000)] for j in range(1000)]
    for line in lines:
        if line[0] == 'turn':
            [x1, y1] = [int(line[2].split(',')[0]), int(line[2].split(',')[1])]
            [x2, y2] = [int(line[-1].split(',')[0]),
                        int(line[-1].split(',')[1])]

            if line[1] == 'on':
                grid = turn_on2(grid, x1, y1, x2, y2)
            else:
                grid = turn_off2(grid, x1, y1, x2, y2)
        else:
            [x1, y1] = [int(line[1].split(',')[0]), int(line[1].split(',')[1])]
            [x2, y2] = [int(line[-1].split(',')[0]),
                        int(line[-1].split(',')[1])]
            grid = toggle2(grid, x1, y1, x2, y2)

    lights = 0
    for line in grid:
        for light in line:
            lights += light
    print(lights)


def main():
    lines = p.input_as_lines('inputs/inp.txt')

    lines_a = []
    for line in lines:
        lines_a.append(line.split(' '))
    lines = lines_a
    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()
