import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict

# left up right down
DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
ARROWS = ['<','^', '>', 'v']
FILENAME = 'inputs/inp.txt'


def load_file(filename):
    S = p.input_as_string(filename)

    m, inss = S.split('\n\n')

    inss = [el for el in inss.split()]
    inss = ''.join(inss)

    G = [[el for el in line] for line in m.split()]
    R = len(G)
    C = len(G[0])
    return G, inss, R, C


def get_startpos(G, R, C):
    for r in range(R):
        for c in range(C):
            if G[r][c] == '@':
                return r, c
    return


def score1(G, R, C):
    s = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == 'O':
                s += 100 * r + c
    return s


def p1():
    G, inss, R, C = load_file(FILENAME)
    r, c  = get_startpos(G, R, C)
    for ins in inss:
        dr, dc = DIRS[ARROWS.index(ins)]
        nr, nc = r + dr, c + dc

        if G[nr][nc] == '.':
            G[nr][nc] = '@'
            G[r][c] = '.'
            r, c = nr, nc
        elif G[nr][nc] == 'O':
            endr, endc = nr, nc
            while G[endr][endc] == 'O':
                endr += dr
                endc += dc
            if G[endr][endc] == '#':
                continue
            else:
                G[endr][endc] = 'O'
                G[r][c] = '.'
                G[nr][nc] = '@'
                r, c = nr, nc
        elif G[nr][nc] == '#':
            continue

    print(score1(G, R, C))


p1()


def update_grid(G, R, C):
    grid_str = ''.join(''.join(row) for row in G)

    grid_str = (grid_str
                .replace('#', '##')
                .replace('O', '[]')
                .replace('.', '..')
                .replace('@', '@.'))

    updated_grid = [list(grid_str[2 * C * i: (i + 1) * 2 * C]) for i in range(R)]

    R = len(updated_grid)
    C = len(updated_grid[0])

    return updated_grid, R, C


def step(G, R, C, ins, pos):
    r, c = pos
    dr, dc = DIRS[ARROWS.index(ins)]
    nr, nc = r + dr, c + dc

    if G[nr][nc] != '#':
        ogr, ogc = r, c
        stack = [(r, c)]
        visited = set(stack)
        while stack:
            r, c = stack.pop()
            nr, nc = r + dr, c + dc
            if G[nr][nc] == '#':
                return ogr, ogc
            if G[r][c] in '[]':
                if G[r][c] == '[':
                    addr, addc = r, c + 1
                elif G[r][c] == ']':
                    addr, addc = r, c - 1
                if (addr, addc) not in visited:
                    stack.append((addr, addc))
                    visited.add((addr, addc))
            # check next position
            if G[nr][nc] in '[]' and (nr, nc) not in visited:
                stack.append((nr, nc))
                visited.add((nr, nc))

        # this method of sorting ensures proper order for updating the visited positions
        for r, c in sorted(list(visited), key=lambda tup: (-dr * tup[0], -dc * tup[1])):
            nr, nc = r + dr, c + dc
            G[nr][nc]  = G[r][c]
            G[r][c] = '.'

        return ogr + dr, ogc + dc

    return r, c


def score2(G):
    s = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == '[':
                s += 100 * r + c
    return s


G, inss, R, C = load_file(FILENAME)
G, R, C = update_grid(G, R, C)

r, c = get_startpos(G, R, C)
for ins in inss:
    r, c = step(G, R, C, ins, (r, c))

print(score2(G))
