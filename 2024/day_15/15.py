import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict

# left up right down
dirs = [
    (0, -1), (-1, 0), (0, 1), (1, 0),
]
arrows = ['<','^', '>', 'v']


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
    G, inss, R, C = load_file('inputs/inp.txt')
    r, c  = get_startpos(G, R, C)
    for ins in inss:
        dr, dc = dirs[arrows.index(ins)]
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


# p1()


def update_grid(G, R, C):
    # alter the map
    r = 0
    for _ in range(R):
        c = 0
        for _ in range(C):
            if G[r][c] == '#':
                G[r].insert(c + 1, '#')
            elif G[r][c] == 'O':
                G[r][c] = '['
                G[r].insert(c + 1, ']')
            elif G[r][c] == '.':
                G[r].insert(c + 1, '.')
            elif G[r][c] == '@':
                G[r].insert(c + 1, '.')
            c += 2
        r += 1
    R = len(G)
    C = len(G[0])
    return G, R, C


def step(G, R, C, ins, pos):
    r, c = pos
    dr, dc = dirs[arrows.index(ins)]
    nr, nc = r + dr, c + dc

    def swap(G, r, c, rn, cn):
        G[r][c], G[rn][cn] = G[rn][cn], G[r][c]

    if G[nr][nc] == '.':
        swap(G, r, c, nr, nc)
        return nr, nc
    elif G[nr][nc] in '[]':
        # recursive pushing?
        if ins in '^v':
            ognr, ognc = nr, nc
            ogr, ogc = r, c
            stack = [(nr, nc)]
            visited = set(stack)
            while stack:
                r, c = stack.pop()
                nr, nc = r + dr, c + dc
                if G[r][c] == '[':
                    addr, addc = r, c + 1
                    if (addr, addc) not in visited:
                        stack.append((addr, addc))
                        visited.add((addr, addc))
                if G[r][c] == ']':
                    addr, addc = r, c - 1
                    if (addr, addc) not in visited:
                        stack.append((addr, addc))
                        visited.add((addr, addc))
                if G[nr][nc] in '[]':
                    stack.append((nr, nc))
                    visited.add((nr, nc))
                if G[nr][nc] == '#':
                    return ogr, ogc

            # we can move the robot and corresponding boxes
            # change top down
            if ins == '^':
                for r, c in sorted(list(visited)):
                    nr, nc = r - 1, c
                    G[nr][nc]  = G[r][c]
                    G[r][c] = '.'
            # change bottom up
            elif ins == 'v':
                for r, c in sorted(list(visited), reverse=True):
                    nr, nc = r + 1, c
                    G[nr][nc] = G[r][c]
                    G[r][c] =  '.'
            # lastly swap the robot with the new position
            swap(G, ogr, ogc, ognr, ognc)
            return ognr, ognc

        elif ins in '<>':
            endr, endc = nr, nc
            while G[endr][endc] in '[]':
                endr += dr
                endc += dc
            if G[endr][endc] == '#':
                return r, c
            else:
                if ins == '<':
                    G[r].pop(endc)
                    G[r].insert(c, '.')
                    G[r][c] = '.'
                    G[nr][nc] = '@'
                else:  # ins == '>':
                    G[r].pop(endc)
                    G[r].insert(c, '.')
                    G[r][c] = '.'
                    G[nr][nc] = '@'
                return nr, nc

    else: #if G[nr][nc] == '#':
        return r, c


def score2(G):
    s = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == '[':
                s += 100 * r + c
    return s


filename = 'inputs/inp.txt'

G, inss, R, C = load_file(filename)
G, R, C = update_grid(G, R, C)

r, c = get_startpos(G, R, C)
for i, ins in enumerate(inss):
    r, c = step(G, R, C, ins, (r, c))

print(score2(G))
