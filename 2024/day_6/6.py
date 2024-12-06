import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict

# up, right, down, left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

G = p.input_as_grid('inputs/inp.txt')
R = len(G)
C = len(G[0])

spos = None
for r in range(R):
    for c in range(C):
        el = G[r][c]
        if el == '^':
            spos = r, c
            break

visited = set()

r, c = spos
visited.add(spos)
i_dir = 0
while True:
    dr, dc = dirs[i_dir % 4]
    nr = r + dr
    nc = c + dc
    if not (0 <= nr < R and 0 <= nc < C):
        break
    if G[nr][nc] != '#':
        r, c = nr, nc
        visited.add((nr, nc))
    elif G[nr][nc] == '#':
        i_dir += 1

print("p1:", len(visited))

p2 = 0
loop_pos = set()
for rl in range(R):
    for cl in range(C):
        if G[rl][cl] != '#':
            temp = G[rl][cl]
            G[rl][cl] = '#'
        else:
            continue

        visited = set()
        collapsed = set((spos[0], spos[1], -1, 0))

        r, c = spos
        visited.add(spos)
        i_dir = 0
        while True:
            dr, dc = dirs[i_dir % 4]
            nr = r + dr
            nc = c + dc
            key = (r, c, dr, dc)

            if key in collapsed:
                loop_pos.add((rl ,cl))
                p2 += 1
                break
            else:
                collapsed.add(key)

            if not (0 <= nr < R and 0 <= nc < C):
                break
            if G[nr][nc] != '#':
                r, c = nr, nc
                visited.add((nr, nc))
            elif G[nr][nc] == '#':
                i_dir += 1

        G[rl][cl] = temp
    print(f'{round(rl / len(G), 4) * 100}%')

print("p2:", p2)
