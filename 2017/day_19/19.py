import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

# up right down left
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

start = (0, G[0].index('|'), 2)
letters = []
pos = start
steps = 0
while True:
    r, c, d = pos
    el = G[r][c]
    if el == '+':
        for nd in [0, 1, 2, 3]:
            if nd == (d + 2) % 4:
                continue
            nr = r + DR[nd]
            nc = c + DC[nd]
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != ' ':
                pos = (nr, nc, nd)
                break
    else:
        nr = r + DR[d]
        nc = c + DC[d]
        if el.isalpha():
            letters.append(el)
        elif el == ' ':
            break
        pos = (nr, nc, d)
    steps += 1

print(''.join(letters))
print(steps)



