import parser
import heapq
from queue import PriorityQueue
import time


def find_neighs(lines, tup, x_lim, y_lim):
    (i, j) = tup
    neighbors = {}

    if i > 0:
        neighbors[i - 1, j] = lines[i-1][j]
    if j > 0:
        neighbors[i, j-1] = lines[i][j-1]

    if i < x_lim - 1:
        neighbors[i + 1, j] = lines[i+1][j]
    if j < y_lim - 1:
        neighbors[i, j + 1] = lines[i][j+1]

    return neighbors


def shortest_path_it(lines):
    i_max = len(lines)
    j_max = len(lines[0])
    init = (0, 0)
    distances = {(i, j): float('inf')
                 for i in range(i_max) for j in range(j_max)}
    distances[init] = 0
    pq = [(0, init)]
    visited = set(init)

    while pq:
        cur_d, pos = heapq.heappop(pq)

        if pos[0] == i_max - 1 and pos[1] == j_max - 1:
            return distances #cur_d

        neighs = find_neighs(lines, pos, i_max, j_max)

        for neigh in neighs:
            if neigh not in visited:
                delta_d = neighs[neigh]
                tot_d = cur_d + delta_d

                heapq.heappush(pq, (tot_d, neigh))
                visited.add(neigh)
                if tot_d < distances[neigh]:
                    distances[neigh] = tot_d


def big_boi(lines):
    with open('big_boi.txt', 'a') as f:
        for line in lines:
            for i in range(5):
                for x in line:
                    if x + i > 9:
                        f.write(str(x + i - 9).strip())
                    else:
                        f.write(str(x + i).strip())
            f.write('\n')

    lines = parser.input_as_grid('big_boi.txt')
    with open('big_boi.txt', 'a') as f:
        for i in range(1, 5):
            for line in lines:
                for x in line:
                    if x + i > 9:
                        f.write(str(x + i - 9).strip())
                    else:
                        f.write(str(x + i).strip())
                f.write('\n')


def main():
    # lines = parser.input_as_grid('big_boi.txt')
    times = []
    # test1('inputs/dag15.txt')
    # n = 100
    # for i in range(n):
    #     times.append(test1('inputs/dag15.txt'))
    # print("avg of {} tests: {}".format(n, sum(times)/n))

    d = test1('big_boi.txt')



def test1(filename):
    lines = parser.input_as_grid(filename)

    start = time.time()
    distances2 = shortest_path_it(lines)
    end = time.time()
    print(end - start)

    # print(distances2[(len(lines) - 1, len(lines[0]) - 1)])

    return end - start


if __name__ == "__main__":
    main()
