from typing import List

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
