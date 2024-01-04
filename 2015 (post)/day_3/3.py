import sys
sys.path.append('..')
import my_parser as p


def deel1(lines):
    x = 0
    y = 0
    xr = 0
    yr = 0
    length = 100
    grid = [[0 for i in range(length)] for j in range(length)]
    grid[x][y] += 1
    for i, char in enumerate(lines):
        if char == '>':
            x += 1
            grid[y][x] += 1
        if char == '<':
            x -= 1
            grid[y][x] += 1
        if char == '^':
            y -= 1
            grid[y][x] += 1
        if char == 'v':
            y += 1
            grid[y][x] += 1
    answer = 0
    for line in grid:
        for house in line:
            if house >= 1:
                answer += 1
    print(answer)


def deel2(lines):
    x = 0
    y = 0
    xr = 0
    yr = 0
    length = 500
    grid = [[0 for i in range(length)] for j in range(length)]
    grid[x][y] += 1
    for i, char in enumerate(lines):
        if i % 2 == 0:
            if char == '>':
                x += 1
                grid[y][x] += 1
            if char == '<':
                x -= 1
                grid[y][x] += 1
            if char == '^':
                y -= 1
                grid[y][x] += 1
            if char == 'v':
                y += 1
                grid[y][x] += 1
        elif i % 2 != 0:
            if char == '>':
                xr += 1
                grid[yr][xr] += 1
            if char == '<':
                xr -= 1
                grid[yr][xr] += 1
            if char == '^':
                yr-= 1
                grid[yr][xr] += 1
            if char == 'v':
                yr += 1
                grid[yr][xr] += 1
    answer = 0
    for line in grid:
        for house in line:
            if house >= 1:
                answer += 1
    print(answer)


def main():
    lines = p.input_as_string('inputs/inp.txt')
    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()
