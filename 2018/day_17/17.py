import sys
sys.path.append('..')
import my_parser as p
import re
from collections import deque
sys.setrecursionlimit(40)
import time

L = p.input_as_lines('inputs/test2.txt')

clay = set()
source = (0, 500)
verbose = 0

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
mir, maxr = min(r), max(r)

c = [el[1] for el in clay]
mic, mac = min(c), max(c)


def show(still_water=[], flow_water=[]):
    for r in range(0, min(100, maxr + 1)):
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


# to update: change source whenever we can start going down, and start dropping
# layers from there, do that to/from both sides: right and left.
def create_still_water(clay):
    water = set()
    i = 0
    # for layer in range(52):
    while True:
        r, c = source
        d = 2
        rb = None
        lb = None
        li = 0
        while True:
            if r > maxr:
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

    return water


def create_flow_water(clay, still_water):
    flow_water = []
    queue = deque([(source[0], source[1])])
    visited = set()
    while queue:
        r, c = queue.popleft()
        if r > maxr + 1:
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
        if verbose:
            time.sleep(0.1)
            show(still_water, visited)

    return set([pos for pos in visited if pos[0] <= maxr])


# unfixable
def still_stack(clay):
    visited = set()
    # while True:
    for layer in range(6):
        stack = [(source[0], source[1])]
        while stack:
            show(visited)
            r, c = stack.pop()
            if r > maxr or c < mic or c > mac:
                return visited
            dd = 2
            nr = r + DR[dd]
            nc = c + DC[dd]
            # we can go down so we just go down
            if (nr, nc) not in clay | visited and (nr, nc) not in stack:
                stack.append((nr, nc))
                continue
            else:
                for dd in [3, 1][::-1]:
                    nr = r + DR[dd]
                    nc = c + DC[dd]
                    if (nr, nc) not in clay | visited and (nr, nc) not in stack:
                        visited.add((nr, nc))
                        stack.append((nr, nc))


def p1():
    # still_water = still_stack(clay)
    # show(still_water)

    still_water = create_still_water(clay)
    flow_water = create_flow_water(clay, still_water)
    show(still_water, flow_water)
    print(len(still_water) + len(flow_water))

p1()