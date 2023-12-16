import sys
sys.path.append('..')
import my_parser as p

lines = p.input_as_lines('inputs/inp.txt')
lines = [[char for char in line] for line in lines]


def show(visited):
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            for d in ['r', 'l', 'u', 'd']:
                if (r, c, d) in visited:
                    if visited[(r, c, d)] > 1:
                        print(str(visited[(r,c,d)]), end='')
                    else:
                        print('#', end='')
                    break
            else:
                print('.', end='')
        print()


def sides():
    sides = []
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if r == 0 and c == 0:
                sides.append((r, c, 'r'))
                sides.append((r, c, 'd'))
            elif r == 0 and c == len(lines[0])-1:
                sides.append((r, c, 'l'))
                sides.append((r, c, 'd'))
            elif r == len(lines)-1 and c == 0:
                sides.append((r, c, 'r'))
                sides.append((r, c, 'u'))
            elif r == len(lines)-1 and c == len(lines[0])-1:
                sides.append((r, c, 'l'))
                sides.append((r, c, 'u'))
            elif r == 0:
                sides.append((r, c, 'd'))
            elif r == len(lines)-1:
                sides.append((r, c, 'u'))
            elif c == 0:
                sides.append((r, c, 'r'))
            elif c == len(lines[0])-1:
                sides.append((r, c, 'l'))
    return sides


def find_energized(stack):
    # stack = [(0, 0, 'r')]
    visited = {}
    i = 0
    while stack:
        r, c, d = stack.pop(-1)
        if c < 0 or c >= len(lines[0]) or r < 0 or r >= len(lines):
            continue
        if (r, c, d) in visited:
            continue
        else:
            visited[(r, c, d)] = 1
        if lines[r][c] == '.':
            if d == 'r':
                stack.append((r, c+1, d))
            elif d == 'l':
                stack.append((r, c-1, d))
            elif d == 'u':
                stack.append((r-1, c, d))
            elif d == 'd':
                stack.append((r+1, c, d))
        elif lines[r][c] == '/':
            if d == 'l':
                stack.append((r+1, c, 'd'))
            elif d == 'r':
                stack.append((r-1, c, 'u'))
            elif d == 'u':
                stack.append((r, c+1, 'r'))
            elif d == 'd':
                stack.append((r, c-1, 'l'))
        elif lines[r][c] == '\\':
            if d == 'l':
                stack.append((r-1, c, 'u'))
            elif d == 'r':
                stack.append((r+1, c, 'd'))
            elif d == 'u':
                stack.append((r, c-1, 'l'))
            elif d == 'd':
                stack.append((r, c+1, 'r'))
        elif lines[r][c] == '|':
            if d == 'u':
                stack.append((r-1, c, d))
            elif d == 'd':
                stack.append((r+1, c, d))
            elif d == 'r':
                stack.append((r-1, c, 'u'))
                stack.append((r+1, c, 'd'))
            elif d == 'l':
                stack.append((r-1, c, 'u'))
                stack.append((r+1, c, 'd'))
        elif lines[r][c] == '-':
            if d == 'l':
                stack.append((r, c-1, d))
            elif d == 'r':
                stack.append((r, c+1, d))
            elif d == 'u':
                stack.append((r, c-1, 'l'))
                stack.append((r, c+1, 'r'))
            elif d == 'd':
                stack.append((r, c-1, 'l'))
                stack.append((r, c+1, 'r'))
    return visited


def calc_energized(visited):
    pos = set()
    for el in visited:
        pos.add((el[0], el[1]))

    return len(pos)


def part1():
    stack = [(0, 0, 'r')]
    visited = find_energized(stack)
    energized = calc_energized(visited)
    print(energized)


part1()


def part2():
    sidess = sides()
    # print(sidess)
    max_energized = 0
    for pos in sidess:
        stack = [pos]
        visited = find_energized(stack)
        energized = calc_energized(visited)
        if energized > max_energized:
            max_energized = energized
    print(max_energized)

part2()
