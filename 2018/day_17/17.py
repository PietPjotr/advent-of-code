"""Potential new idea:

1. recursively create a stack for as long as we can move down.
2. When we change direction from either left or right to down:
3. Add a new source to the higher level source stack.
4. if the current source ends up in the visited: continue with the inner stack

6 nvfm: we again have the same problem of ending up in flowing water and
    breaking: TODO: think about solution between still water and flowing water
    in dfs/bfs appoach.

"""

import sys
sys.path.append('..')
import my_parser as p
import re
from collections import deque
import heapq

L = p.input_as_lines('inputs/test.txt')

clay = set()
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
    # print(' ', end='')
    # for i in range(max(450, mic), min(550, mac + 1)):
    #     i = str(i)
    #     print(i[-1], end='')
    # print()
    for r in range(0, min(100, maxr + 1)):
        # print(str(r)[-1], end='')
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


def create_still_water(clay):
    water = set()
    stack = [source]
    for sf in range(70):
    # while stack:
        print(len(water))
        s = stack.pop()
        r, c = s
        if r > maxr or c < mic or c > mac:
            # print('source {} discontinued'.format(s))
            continue
        d = 2
        rb = None
        lb = None
        li = 0
        new = False
        while True:
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
            # we reach outside of the grid so we discontinue
            if nr > maxr or nc < mic or nc > mac:
                if d == 3:
                    d = 1
                    r = r + DR[d]
                    c = c + DC[d]
                    continue
                else:
                    new = True
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
                # we start going down so we add this position as the new
                # source and continue with the next frame.
                elif dd == 2:
                    stack.append((r, c))
                    new = True
                    break
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
        if not new:
            stack.append(s)

    print(stack)
    return set([pos for pos in water if pos[0] <= maxr and mic <= pos[1] <= mac])

# continues in the current dir until either we can't or we can go down
def cont(r, c, d, taken):
    for dd in [2, d]:
        nr = r + DR[dd]
        nc = c + DC[dd]
        if (nr, nc) not in taken:
            if dd == 2:
                return 2
            elif dd == d:
                return 1
    return 0


# looking good so far, I think this might become the solution
source = (0, 500)
def solve_still(clay):
    visited = set()
    sources = set(source)
    source_q = [(-source[0], -source[1])]
    for sq in range(10):
    # while source_q:
        # print(len(visited))
        s = heapq.heappop(source_q)
        rs, cs = -s[0], -s[1]
        if rs > maxr or cs < mic or cs > mac:
            # print('source {} discontinued'.format((rs, cs)))
            continue
        fill_stack = [(rs, cs, 2)]
        while fill_stack:
            # show(visited, [(-s[0], -s[1]) for s in source_q])

            r, c, d = fill_stack.pop()


            if d != 2:
                start = (r - DR[d], c - DC[d])
                hor = set([(r, c)])
                var = cont(r, c, d, clay | visited)
                while var == 1:
                    r = r + DR[d]
                    c = c + DC[d]
                    hor.add((r, c))
                    var = cont(r, c, d, clay | visited)
                if var == 2:
                    if (r, c) not in sources:
                        heapq.heappush(source_q, (-r, -c))
                        sources.add((r, c))
                elif var == 0:
                    visited |= hor
                    visited.add(start)

            else:
                for dd in [2, 3, 1][::-1]:
                    nr = r + DR[dd]
                    nc = c + DC[dd]
                    if (nr, nc) not in clay | visited and nr < maxr and mic < nc < mac:
                        fill_stack.append((nr, nc, dd))
    return visited


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

    return set([pos for pos in visited if pos[0] <= maxr and mic <= pos[1] <= mac])


def p1():
    # still_water = still_stack(clay)
    # show(still_water)

    still_water = solve_still(clay)
    flow_water = create_flow_water(clay, still_water)
    show(still_water, flow_water)
    print('still:', len(still_water))
    print('flow:', len(flow_water))
    print(len(still_water) + len(flow_water))

p1()