import sys
sys.path.append('..')
import my_parser as p
from itertools import groupby

lines = p.input_as_lines('inputs/inp.txt')

lines = [list(sub) for ele, sub in groupby(lines, key = bool) if ele]


def find_all_mirror_lines(line):
    prev = ''
    ret = []
    for i, row in enumerate(line):
        t, b = i - 1, i
        tops = []

        tstart, bstart = t, b
        while row == prev:

            t = t - 1
            b = b + 1
            if b >= len(line) or t < 0:
                ret.append(tstart + 1)
                break
            row = line[b]
            prev = line[t]

        prev = line[i]
    return ret


def part1():
    res = 0
    for i, line in enumerate(lines):
        row_result = find_all_mirror_lines(line)

        linecol = list(map(list, zip(*line)))
        linecol = [''.join(l) for l in linecol]
        col_result = find_all_mirror_lines(linecol)

        res += 100 * row_result[0] if row_result else 0 + col_result[0] if col_result else 0

    print(res)


def find_smudge(grid):
    grid = [[el for el in row] for row in grid]
    rows = find_all_mirror_lines(grid)

    linecol = list(map(list, zip(*grid)))
    cols = find_all_mirror_lines(linecol)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            el = grid[i][j]
            if el == '#':
                grid[i][j] = '.'
            if el == '.':
                grid[i][j] = '#'

            new_rows = find_all_mirror_lines(grid)
            new_cols = find_all_mirror_lines(list(map(list, zip(*grid))))

            for new in new_rows:
                if new not in rows:
                    return 100 * new

            for new in new_cols:
                if new not in cols:
                    return new

            grid[i][j] = el

    return None


def part2():
    res = 0
    for grid in lines:
        new_res = find_smudge(grid)
        res += new_res

    print(res)


part1()
part2()
