from typing import List
import copy


def input_as_string(filename: str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")


def input_as_lines(filename: str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")


def input_as_ints(filename: str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    def line_as_int(l): return int(l.rstrip('\n'))
    return list(map(line_as_int, lines))


def input_as_grid(lines, row):
    grids = []
    for y in range(0, int(len(lines) / (row + 1) + 1) - 1):
        grid = []
        for x in range((row + 1) * y + 1, (row + 1) * y + row + 1):
            grid.append([int(z) for z in lines[x].split()])
        grids.append(grid)

    return grids


def deel1():
    # lines = input_as_lines('dag1_input.txt')
    # print(lines)

    # lines = input_as_ints('dag1_input.txt')
    # print(lines)

    lines = input_as_lines('dag9_input.txt')
    lines_n = 0
    lowest = []
    basins = []
    for line in lines:
        for i, char in enumerate(line):
            if lines_n == 0:
                if i == 0:
                    if line[i + 1] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
                elif i < len(lines[0]) - 1:
                    if line[i + 1] > char and line[i - 1] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
                else:
                    if line[i - 1] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
            elif lines_n < len(lines) - 1:
                if i == 0:
                    if line[i + 1] > char and lines[lines_n + 1][i] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
                elif i < len(lines[0]) - 1:
                    if line[i + 1] > char and line[i - 1] > char and lines[lines_n - 1][i] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
                else:
                    if line[i - 1] > char and lines[lines_n - 1][i] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
            else:
                if i == 0:
                    if line[i - 1] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
                elif i < len(lines[0]) - 1:
                    if line[i + 1] > char and line[i - 1] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
                else:
                    if line[i - 1] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
        lines_n += 1

    low_sum = 0
    for low in lowest:
        low_sum += int(low[0]) + 1
    print(low_sum)
    print(lowest)




def deel2():
    lines = input_as_lines('dag9_input.txt')
    lines_n = 0
    lowest = []
    basins = []
    for line in lines:
        for i, char in enumerate(line):
            if lines_n == 0:
                if i == 0:
                    if line[i + 1] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
                elif i < len(lines[0]) - 1:
                    if line[i + 1] > char and line[i - 1] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
                else:
                    if line[i - 1] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
            elif lines_n < len(lines) - 1:
                if i == 0:
                    if line[i + 1] > char and lines[lines_n + 1][i] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
                elif i < len(lines[0]) - 1:
                    if line[i + 1] > char and line[i - 1] > char and lines[lines_n - 1][i] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
                else:
                    if line[i - 1] > char and lines[lines_n - 1][i] > char and lines[lines_n + 1][i] > char:
                        lowest.append([char, i, lines_n])
            else:
                if i == 0:
                    if line[i - 1] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
                elif i < len(lines[0]) - 1:
                    if line[i + 1] > char and line[i - 1] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
                else:
                    if line[i - 1] > char and lines[lines_n - 1][i] > char:
                        lowest.append([char, i, lines_n])
        lines_n += 1

    max_basin = 0
    basins = []
    basin_lines = [[int(x) for x in line] for line in lines]
    for low in lowest:
        basin_lines = copy.deepcopy(basin_lines)
        basin = bfs([int(low[0])], basin_lines, low[2], low[1])
        basins.append(basin)

    basin_len = []
    for basin in basins:
        basin_len.append(len(basin))
    sorted_b = sorted(basin_len, reverse=True)
    print(sorted_b)
    print(sorted_b[0] * sorted_b[1] * sorted_b[2])


deel2()
