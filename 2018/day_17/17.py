# final idea:
#
#   'beacon scanning' for still water:
#       first drop layer by layer using one beacon.
#       whenever we start going left or right, we check if we have already have a
#       left/right 'boundary' position, if not we store the current pos as the
#       right/left boundary position, else we fill all the positions between the
#       right and left boundary positions
#
#   obligatory bfs 'custom flood fill' for the non still water volumes
import sys
sys.path.append('..')
import my_parser as p
import re
from collections import deque
sys.setrecursionlimit(30)

L = p.input_as_lines('inputs/test.txt')

clay = set()
source = (0, 500)

for l in L:
    a, b = l.split(', ')
    if a[0] == 'x':
        c = int(a[2:])
        start, end = [int(el) for el in re.findall(r'-?\d+', b)]
        for r in range(start, end + 1):
            clay.add((r, c))
    elif a[0] == 'y':
        r = int(a[2:])
        start, end = [int(el) for el in re.findall(r'-?\d+', b)]
        for c in range(start, end + 1):
            clay.add((r, c))


r = [el[0] for el in clay]
mir, mar = min(r), max(r)

c = [el[1] for el in clay]
mic, mac = min(c), max(c)


def show(still_water=[], flow_water=[]):
    for r in range(0, min(100, mar + 1)):
        for c in range(max(450, mic), min(550, mac + 1)):
            if (r, c) == source:
                print('+', end='')
            elif (r, c) in clay:
                print('#', end='')
            elif (r, c) in still_water:
                print('~', end='')
            elif (r, c) in flow_water:
                print('|', end= '')
            else:
                print('.', end='')
        print()
    print()


# up right down left
# 0, 1,    2,   3
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


# wrong, only walks off the left side off a overflown bucket
def create_still_water(clay):
    water = set()
    i = 0
    for layer in range(52):
    # while True:
        r, c = source
        d = 2
        rb = None
        lb = None
        li = 0
        while True:
            if r > mar:
                return water
            if d == 2:
                dds = [2, 3, 1]
            elif d == 3:
                dds = [2, 3, 1]
            elif d == 1:
                dds = [2, 1, 3]

            end = True
            for dd in dds:
                nr = r + DR[dd]
                nc = c + DC[dd]
                if (nr, nc) not in water | clay:
                    end = False
                    break
            # we can't go anywhere so we only add the single water volume
            if end:
                water.add((r, c))
                break
            # if we start going a different direction
            if dd != d:
                # if we start going right
                if dd == 1:
                    # already seen so we add the layer
                    if (r, c) == lb:
                        for c in range(lb[1], rb[1] + 1):
                            water.add((r, c))
                    # not yet seen so we change the boundary point
                    else:
                        lb = (r, c)
                # if we start going left
                elif dd == 3:
                    # already seen right boundary so we add the layer
                    if (r, c) == rb:
                        for c in range(lb[1], rb[1] + 1):
                            water.add((r, c))
                    # not yet seen right boundary so we update the boundary
                    else:
                        rb = (r, c)
            r = nr
            c = nc
            d = dd

        i += 1
    return water


def create_flow_water(clay, still_water):
    flow_water = []
    queue = deque([(source[0], source[1])])
    visited = set()
    while queue:
        r, c = queue.popleft()
        if r > mar + 1:
            break
        dd = 2  # check if we can go down:
        nr = r + DR[dd]
        nc = c + DC[dd]
        if (nr, nc) not in clay | still_water and (nr, nc) not in visited:
            queue.append((nr, nc))
            visited.add((nr, nc))
        else:
            for dd in [1, 3]:
                nr = r + DR[dd]
                nc = c + DC[dd]
                if (nr, nc) not in still_water | clay and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))

    return set([pos for pos in visited if pos[0] <= mar])


def still_rec(clay, water, r, c, d):
    show(water)
    if r > mar + 1:
        return

    for dd in [2, 3, 1]:
        nr = r + DR[dd]
        nc = c + DC[dd]
        if (nr, nc) not in water | clay:
            water.add((nr, nc))
            still_rec(clay, water, nr, nc, dd)
    return


def p1():
    # still_water = set()
    # still_water = still_rec(clay,still_water, *source, 2)
    still_water = create_still_water(clay)
    flow_water = create_flow_water(clay, still_water)
    show(still_water, flow_water)
    print(len(still_water) + len(flow_water))

p1()