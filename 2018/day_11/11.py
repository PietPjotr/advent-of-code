import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')[0]
L = int(L)


def get_power(x, y, number):
    rack_ID = x + 10
    power = rack_ID * y
    power += number
    power *= rack_ID
    power = list(str(power))
    if len(power) >= 3:
        power = int(power[-3])
    else:
        power = 0
    power -= 5
    return power


def create_grid():
    powers = [[0 for _ in range(300)] for _ in range(300)]
    for x in range(0, 300):
        for y in range(0, 300):
            powers[y][x] = get_power(x, y, L)
    return powers


def solve(size, powers):
    m = 0
    mpos = (0, 0)
    for r in range(300 - size + 1):
        rows = powers[r: r + size]
        for c in range(300 - size + 1):
            grid = [row[c: c + size] for row in rows]
            val = sum([sum(row) for row in grid])
            if val > m:
                m = val
                mpos = (c, r)
                mgrid = grid
    return m, mpos


grid = create_grid()
p1 = str(solve(3, grid)[1])
print(p1[1:-1].replace(' ', ''))


def p2():
    m = 0
    msize = 0
    mpos = 0
    grid = create_grid()
    for size in range(3, 20):  # apparently it doesn't get better after this
        fuel, pos = solve(size, grid)
        if fuel > m:
            m = fuel
            msize = size
            mpos = pos

    return (mpos[0], mpos[1], msize)

p2 = str(p2())
print(p2[1:-1].replace(' ', ''))
