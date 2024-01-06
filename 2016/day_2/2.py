import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

dirs = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

grid1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
]
grid2 = [[0, 0, 1, 0, 0],
         [0, 2, 3, 4, 0],
         [5, 6, 7, 8, 9],
         [0, 'A', 'B', 'C', 0],
         [0, 0, 'D', 0, 0],
]


def solve(start, grid):
    r, c = start
    code = ''
    S = len(grid)
    for line in L:
        for el in line:
            delta = dirs[el]
            dr, dc = delta
            nr = r + dr
            nc = c + dc
            if 0 <= nr < S and 0 <= nc < S and grid[nr][nc] != 0:
                r, c = nr, nc
        code += str(grid[r][c])

    print(code)


solve((1, 1), grid1)
solve((2, 0), grid2)