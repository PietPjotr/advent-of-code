import parser
import heapq
from queue import PriorityQueue
import time

def find_neighs(lines, tup, x_lim, y_lim):
    (i, j) = tup
    neighbors = {}

    cur = lines[i][j]
    if cur == 'S':
        cur = 'a'
    if cur == 'E':
        cur = 'z'

    if i > 0:
        neigh = lines[i-1][j]
        # print(cur, neigh)
        if ord(neigh) - ord(cur) <= 1:
            neighbors[i - 1, j] = lines[i-1][j]
    if j > 0:
        # print(cur, neigh)
        neigh = lines[i][j-1]
        if ord(neigh) - ord(cur) <= 1:
            neighbors[i, j-1] = lines[i][j-1]

    if i < x_lim - 1:
        # print(cur, neigh)
        neigh = lines[i+1][j]
        if ord(neigh) - ord(cur) <= 1:
            neighbors[i + 1, j] = lines[i+1][j]
    if j < y_lim - 1:
        # print(cur, neigh)
        neigh = lines[i][j+1]
        if ord(neigh) - ord(cur) <= 1:
            neighbors[i, j + 1] = lines[i][j+1]

    return neighbors


def shortest_path_it(grid, start, end):
    i_max = len(grid)
    j_max = len(grid[0])
    init = start
    distances = {(i, j): float('inf')
                 for i in range(i_max) for j in range(j_max)}
    distances[init] = 0
    pq = [(0, init)]
    visited = set(init)

    while pq:
        cur_d, pos = heapq.heappop(pq)

        if pos[0] == end[0] and pos[1] == end[1]:
            return distances #cur_d

        neighs = find_neighs(grid, pos, i_max, j_max)

        for neigh in neighs:
            if neigh not in visited:
                # every neighbor is always 1 away
                delta_d = 1
                tot_d = cur_d + delta_d

                heapq.heappush(pq, (tot_d, neigh))
                visited.add(neigh)
                if tot_d < distances[neigh]:
                    distances[neigh] = tot_d

def deel1(grid):
    start = []
    end = []
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == 'S':
                start = (i, j)
            elif el == 'E':
                end = (i, j)

    print(shortest_path_it(grid, start, end)[end])


def deel2(grid):
    paths = []
    starts = []
    end = []
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            if el == 'S':
                starts.append((i, j))
            elif el == 'a':
                starts.append((i, j))
            elif el == 'E':
                end = (i, j)


    for start in starts:
        distances = shortest_path_it(grid, start, end)
        if distances:
            paths.append(distances[end])

    print(min(paths))


def main():
    lines = parser.input_as_lines('inputs/dag12.txt')
    grid = [[el for el in line] for line in lines]
    deel1(grid)
    deel2(grid)


if __name__ == "__main__":
    main()