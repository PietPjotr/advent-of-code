import sys
sys.path.append('..')
import my_parser as p
import math
import cProfile

L = p.input_as_lines('inputs/inp.txt')
rules = [line.split(' => ') for line in L]
rules = {source: dest for source, dest in rules}
grid = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
R = C = len(grid)


def flip(grid):
    return [row[::-1] for row in grid]


def rotate(grid):
    R = C = len(grid)
    return [[grid[r][c] for r in range(R)][::-1] for c in range(C)]


def show(grid):
    for row in grid:
        print(''.join(row))


def score(grid):
    score = 0
    for row in grid:
        for el in row:
            if el == '#':
                score += 1
    return score


def get_state(grid):
    state = ''
    for row in grid:
        state += ''.join(row) + '/'
    return state[:-1]


def get_variants(grid):
    states = []
    for g in [grid, flip(grid)]:
        states.append(get_state(g))
        for i in range(3):
            g = rotate(g)
            states.append(get_state(g))
    return states


def get_subgrid_map(rules):
    subgrid_map = {}

    # Precompute variants for 3x3 grids
    for i in range(2**9):  # There are 2^9 possible states for a 3x3 grid
        state = format(i, '09b')
        state = state.replace('0', '.')
        state = state.replace('1', '#')
        grid = [list(state[j:j+3]) for j in range(0, 9, 3)]

        variants = get_variants(grid)

        # Add variants to mapping
        subgrid_map[get_state(grid)] = variants

    # Precompute variants for 2x2 grids
    for i in range(2**4):  # There are 2^4 possible states for a 2x2 grid
        state = format(i, '04b')
        state = state.replace('0', '.')
        state = state.replace('1', '#')

        grid = [list(state[j:j+2]) for j in range(0, 4, 2)]

        variants = get_variants(grid)

        # add variants to mapping
        subgrid_map[get_state(grid)] = variants

    # map all variants to the same destination
    for k, v in subgrid_map.items():
        skip = False
        for state in v:
            if skip:
                break
            if state in rules:
                dest = rules[state]
                for variant in v:
                    subgrid_map[variant] = dest
                skip = True

    return subgrid_map


def state_to_grid(state):
    return [[el for el in row] for row in state.split('/')]


def combine(grids):
    ret = []
    no_subgrids = len(grids)
    size = int(no_subgrids ** 0.5)
    for r in range(size):
        subgrids = grids[r*size:(r+1)*size]
        for sr in range(len(subgrids[0])):
            row = []
            for subgrid in subgrids:
                row += subgrid[sr]
            ret.append(row)
    return ret


def split_grid(grid, no_subgrids, size):
    ret = []
    for r in range(no_subgrids):
        subrows = grid[r*size:(r+1)*size]
        for c in range(no_subgrids):
            subgrid = [subrow[c*size:(c+1)*size] for subrow in subrows]
            ret.append(subgrid)
    return ret


def split(grid):
    ret = []
    size = len(grid)
    if size % 2 == 0:
        ret = split_grid(grid, size//2, 2)
    elif size % 3 == 0:
        if size == 3:
            return [grid]
        ret = split_grid(grid, size//3, 3)
    return ret


def solve(grid, n):
    subgrid_map = get_subgrid_map(rules)
    for i in range(n):
        subgrids = split(grid)
        resulting_subgrids = []
        for subgrid in subgrids:
            resulting_subgrids.append(state_to_grid(subgrid_map[get_state(subgrid)]))

        grid = combine(resulting_subgrids)

    return grid


def main():
    print(score(solve(grid, 5)))
    print(score(solve(grid, 18)))


if __name__ == "__main__":
    # Run the profiler
    main()
    # cProfile.run('main()', sort='cumulative')
