import sys
sys.path.append('..')
import my_parser as p
import re
from copy import deepcopy
import heapq

L = p.input_as_lines('inputs/inp.txt')

nodes = []

for line in L[2:]:
    nums = re.findall(r'[0-9]+', line)
    x, y, size, used, avail, use = [int(n) for n in nums]
    nodes.append([(x, y), size, used, avail, use])

p1 = 0
for node1 in nodes:
    used = node1[2]
    for node2 in nodes:
        avail = node2[3]
        if node1 != node2 and used != 0 and used <= avail:
            p1 += 1

# print(p1)

avail = sorted([node[3] for node in nodes], reverse=True)
R = max([node[0][1] for node in nodes]) + 1
C = max([node[0][0] for node in nodes]) + 1

max_avail = avail[0]
graph = [['-' for c in range(C)] for r in range(R)]
start = (0, 0)
for node in nodes:
    x, y = node[0]
    if node[2] <= max_avail:
        graph[y][x] = '.'
    else:
        graph[y][x] = '#'
    if node[3] == max_avail:
        start = node[0][::-1]


def show(graph, pos, target):
    for r, row in enumerate(graph):
        for c, node in enumerate(row):
            if (r, c) == target:
                print('G', end=' ')
            elif (r, c) == pos:
                print('-', end=' ')
            else:
                print(node, end=' ')
        print()
    print()


target = (0, C - 1)
stack = [[0 + C - 1, 0, start, target]]
DP = set((start, target))
while stack:
    # Use heapq to pop the node with the smallest priority
    _, steps, pos, target = heapq.heappop(stack)
    if (pos, target) in DP:
        continue
    DP.add((pos, target))
    if target == (0, 0):
        print(steps)
        break
    r, c = pos
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C and graph[nr][nc] != '#':
            npos = (nr, nc)
            ntarget = deepcopy(target)
            # check if the target gets swapped
            if npos == target:
                ntarget = deepcopy(pos)

            # Use heapq to push the node with the updated priority
            heapq.heappush(stack, (target[0] + target[1], steps + 1, npos, ntarget))
