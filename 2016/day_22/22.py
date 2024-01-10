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
print(p1)

R = max([node[0][1] for node in nodes]) + 1
C = max([node[0][0] for node in nodes]) + 1

max_avail = max([node[3] for node in nodes])
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


target = (0, C - 1)
stack = [[0 + C - 1, 0, start, target]]
DP = set((start, target))
while stack:
    p, steps, pos, target = heapq.heappop(stack)
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
                p = target[0] + target[1]

            heapq.heappush(stack, (p, steps + 1, npos, ntarget))