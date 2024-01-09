import sys
sys.path.append('..')
import my_parser as p

inp = 1352
R = 100
C = 100
start = (1, 1)
end = (39, 31)


def f(x, y):
    return x*x + 3*x + 2*x*y + y + y*y


def create_grid():
    grid = [['-' for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            num = f(c, r) + inp
            bin_num = "{0:b}".format(num)
            if bin_num.count('1') % 2 == 0:
                grid[r][c] = '.'
            else:
                grid[r][c] = '#'

    return grid


def shortest_path(s, e, grid):
    stack = [(0, s)]
    visited = set()
    p2 = set()
    while stack:
        steps, coord = stack.pop(0)
        r, c = coord
        if coord == e:
            print(steps)
            print(len(p2))
            return visited
        if steps <= 50:
            p2.add((r, c))
        visited.add(coord)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if (nr, nc) in visited or nr < 0 or nr >= R or nc < 0 or nc >= C or grid[nr][nc] == '#':
                continue

            stack.append((steps + 1, (nr, nc)))


grid = create_grid()
visited = shortest_path(start, end, grid)
