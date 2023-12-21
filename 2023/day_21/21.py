import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

s = (0, 0)
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            s = (r, c)

stack = set([s])
for i in range(64):
    new_stack = set()
    for r, c in stack:
        for dr, dc in ((0,1), (1,0), (-1,0), (0,-1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and G[nr][nc] == '.' and (nr,nc) and (nr,nc):
                new_stack.add((nr, nc))
    stack = new_stack



def show_visited(visited):
    for r in range(R):
        for c in range(C):
            if (r,c) in visited:
                print('O', end='')
            else:
                print(G[r][c], end='')
        print()

show_visited(stack)
show_visited(visited)

print(len(set(stack)) + 1)