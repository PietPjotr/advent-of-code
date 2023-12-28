import sys
sys.path.append('..')
import my_parser as p
import heapq

map_dirs = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}

lines = p.input_as_lines('inputs/inp.txt')
G = [[el for el in line] for line in lines]
R = len(G)
C = len(G[0])

end = (R - 1, C - 2)
start = (0, 1, 0)

def p1():
    end = (R - 1, C - 2)
    start = (0, 1, 0)
    visited = set()
    stack = [(start, visited)]
    m = 0
    while stack:
        ((r, c, d), visited) = stack.pop()

        if (r, c) == end:
            m = max(m, d)
            continue

        visited.add((r, c))
        if G[r][c] in map_dirs:
            dr, dc = map_dirs[G[r][c]]
            if 0 <= r + dr < R and 0 <= c + dc < C and (r + dr, c + dc) not in visited:
                stack.append(((r + dr, c + dc, d + 1), visited.copy()))
        else:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r + dr < R and 0 <= c + dc < C and (r + dr, c + dc) not in visited and G[r + dr][c + dc] != '#':
                    stack.append(((r + dr, c + dc, d + 1), visited.copy()))

    print(m)

p1()


def p2():
    end = (R - 1, C - 2)
    start = (0, 1)

    # determine the junctions
    stack = [(start)]
    visited = set()
    junctions = [start, end]
    while stack:
        (r, c) = stack.pop(0)

        if (r, c) == end:
            break
        visited.add((r, c))

        neighs = []
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rn, cn = r + dr, c + dc
            if 0 <= rn < R and 0 <= cn < C and (rn, cn) not in visited and G[rn][cn] != '#':
                neighs.append((rn, cn))

        if len(neighs) > 1:
            junctions.append((r, c))
        for neigh in neighs:
            stack.append(neigh)

    # determine the length between all the junctions
    graph = {j:{} for j in junctions}
    for j in junctions:
        stack = [(j, 0)]
        visited = set()
        while stack:
            (r, c), d = stack.pop(0)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) != j and (r, c) in junctions:
                graph[j][(r, c)] = d
                continue
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                rn, cn = r + dr, c + dc
                if 0 <= rn < R and 0 <= cn < C and (rn, cn) not in visited and G[rn][cn] != '#':
                    stack.append(((rn, cn), d + 1))

    # find all the paths in the graph with dfs and remember the largest path:
    largest = 0
    stack = [(start, 0, set())]
    while stack:
        (r, c), d, visited = stack.pop()
        if (r, c) in visited:8
            continue
        visited.add((r, c))
        if (r, c) == end:
            if d > largest:
                largest = d
            continue
        for neigh in graph[(r, c)]:
            stack.append((neigh, d + graph[(r, c)][neigh], visited.copy()))
    print(largest)

p2()


