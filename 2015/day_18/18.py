import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])


def get_neighbours(r, c, G):
    on = 0
    for nr in range(r-1, r+2):
        for nc in range(c-1, c+2):
            if nr < 0 or nr >= R or nc < 0 or nc >= C or (nc == c and nr == r):
                continue
            if G[nr][nc] == '#':
                on += 1

    return on


def get_score(grid):
    on = 0
    for r in range(R):
        for c in range(C):
            el = grid[r][c]
            if el == '#':
                on += 1

    print(on)


def solve(part, G):
    iterations = 100
    for i in range(iterations):
        new = [['-' for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                el = G[r][c]
                on = get_neighbours(r, c, G)
                if el == '#':
                    if on == 3 or on == 2:
                        new[r][c] = '#'
                    else:
                        new[r][c] = '.'
                elif el == '.':
                    if on == 3:
                        new[r][c] = '#'
                    else:
                        new[r][c] = '.'
        if part == 2:
            new[0][0] = '#'
            new[0][C-1] = '#'
            new[R-1][0] = '#'
            new[R-1][C-1] = '#'
        G = new

    res = get_score(G)

solve(1, G)
solve(2, G)