import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

# up right down left
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def move(cart):
    r, c, d, state, status = cart
    if G[r][c] == '+':
        if state == 0:
            d = (d - 1) % 4
        elif state == 1:
            d = d
        elif state == 2:
            d = (d + 1) % 4
        state = (state + 1) % 3
    elif G[r][c] == '/':
        if d == 0:
            d = 1
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        elif d == 3:
            d = 2

    elif G[r][c] == '\\':
        if d == 0:
            d = 3
        elif d == 1:
            d += 1
        elif d == 2:
            d = 1
        elif d == 3:
            d = 0
    r += DR[d]
    c += DC[d]

    for i, val in enumerate((r, c, d, state, status)):
        cart[i] = val


def find_carts(grid):
    carts = []
    for r in range(R):
        for c in range(C):
            el = grid[r][c]
            if el == '^':
                grid[r][c] = '|'
                carts.append([r, c, 0, 0, 1])
            elif el == 'v':
                grid[r][c] = '|'
                carts.append([r, c, 2, 0, 1])
            elif el == '>':
                grid[r][c] = '-'
                carts.append([r, c, 1, 0, 1])
            elif el == '<':
                grid[r][c] = '-'
                carts.append([r, c, 3, 0, 1])
    carts = sorted(carts, key=lambda x: (x[0], x[1]))
    return carts, grid


def step(G, carts):
    for cart1 in carts:
        if cart1[-1] == 0:
            continue
        move(cart1)
        for cart2 in carts:
            if cart1 == cart2:
                continue
            if cart2[-1] == 0:
                continue
            if cart1[:2] == cart2[:2]:
                cart1[-1] = 0
                cart2[-1] = 0

    return sorted(carts, key=lambda x: (x[0], x[1]))


def solve(G):
    p1 = False
    carts, G = find_carts(G)
    while True:
        carts = step(G, carts)
        remaining = [cart for cart in carts if cart[-1] == 1]
        if len(remaining) < len(carts) and not p1:
            collision = [cart for cart in carts if cart[-1] == 0]
            collided_cart = collision[0]
            print(str(collided_cart[1]) + ',' + str(collided_cart[0]))
            p1 = True
        if len(remaining) == 1:
            last_cart = remaining[0]
            print(str(last_cart[1]) + ',' + str(last_cart[0]))
            return


solve(G)
