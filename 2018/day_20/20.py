import sys
sys.path.append('..')
import my_parser as p
import re
from collections import deque

L = p.input_as_lines('inputs/inp.txt')[0]
L = L[1:-1]

mapping = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

# represents all the possible connections between positions
G = {}

s = (0, 0)

def create_graph(directions, G):
    stack = []
    r, c = (0, 0)
    i = 0
    while i < len(directions):
        char = directions[i]
        if char == '(':
            stack.append((r, c))
        elif char == ')':
            r, c = stack.pop()
        elif char == '|':
            r, c = stack[-1]
        else:
            nr = r + mapping[char][0]
            nc = c + mapping[char][1]
            if (r, c) in G:
                G[(r, c)].add((nr, nc))
            else:
                G[(r, c)] = set([(nr, nc)])
            if (nr, nc) in G:
                G[(nr, nc)].add((r, c))
            else:
                G[(nr, nc)] = set([(r, c)])
            r = nr
            c = nc
        i += 1

create_graph(L, G)


def bfs(G):
    p2 = 0
    q = deque([(0, (0, 0))])
    visited = set([(0, 0)])
    while q:
        steps, pos = q.popleft()
        if steps >= 1000:
            p2 += 1
        for npos in G[pos]:
            if npos not in visited:
                q.append((steps + 1, npos))
                visited.add(npos)

    print(steps)
    print(p2)


bfs(G)
