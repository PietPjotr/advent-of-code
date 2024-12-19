import sys
sys.path.append('..')
import my_parser as p
import re
import numpy as np
import matplotlib.pyplot as plt


L = p.input_as_lines('inputs/inp.txt')

clay = set()

for line in L:
    a, b = line.split(', ')
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


rs = [el[0] for el in clay]
minr, maxr = min(rs), max(rs)

cs = [el[1] for el in clay]
minc, maxc = min(cs), max(cs)

# up right down left
# 0, 1,    2,   3
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


# continues in the current dir until either we can't or we can go down
# returns 0 if we cannot go down
# returns 1 if we can go down at any point
def cont(r, c, d, taken):
    r += DR[d]
    c += DC[d]
    while (r, c) not in taken:
        rd = r + DR[2]
        cd = c + DC[2]
        if (rd, cd) not in taken:
            return 1, (rd, cd)
        else:
            r = r + DR[d]
            c = c + DC[d]

    return 0, (r, c)


def inside(pos):
    r, c = pos
    return r >= minr and r <= maxr


source = (0, 500)
visited_sources = set()


def solve(source, clay, still, flowing):

    visited_sources.add(source)
    rs, cs = source
    rd, cd = source

    hor_stack = []
    # first build the stack horizontally:
    while (rd, cd) not in still | clay and rd <= maxr + 1:
        hor_stack.append((rd, cd))
        rd = rd + DR[2]
        cd = cd + DC[2]

    while hor_stack:
        r, c = hor_stack.pop()
        # we are done on this branch
        if r > maxr:
            # add vertical flowing water
            for nr in range(rs, maxr + 1):
                flowing.add((nr, c))
            return 1
        left = cont(r, c, 3, still | clay)
        right = cont(r, c, 1, still | clay)

        # we have overflown the current bucket
        if left[0] == 1 or right[0] == 1:

            # add vertical flowing water
            for nr in range(rs, r + 1):
                flowing.add((nr, c))
            # add horizontal flowing water:
            for nc in range(left[1][1], right[1][1] + 1):
                flowing.add((r, nc))

            rr, rl = 0, 0
            if left[0] == 1:
                if left[1] not in visited_sources and inside(left[1]):
                    rl = solve(left[1], clay, still, flowing)
                else:
                    rl = 1
            if right[0] == 1:
                if right[1] not in visited_sources and inside(right[1]):
                    rr = solve(right[1], clay, still, flowing)
                else:
                    rr = 1
            if rr == 1 or rl == 1:
                return 1
            else:
                hor_stack.append((r, c))

        else:
            for ret in [left, right]:
                code, pos = ret
                # reached the end to either left or right
                if code == 0:
                    rf, cf = pos
                    for nc in range(min(cs, cf), max(cs, cf)):
                        if (r, nc) not in clay:
                            still.add((r, nc))

    return 0


def visualize_grid(clay, still_water, flow_water):
    # Determine grid dimensions
    minr = min(r for r, _ in clay | still_water | flow_water)
    maxr = max(r for r, _ in clay | still_water | flow_water)
    minc = min(c for _, c in clay | still_water | flow_water)
    maxc = max(c for _, c in clay | still_water | flow_water)

    # Create an array to represent the grid
    grid = np.zeros((maxr - minr + 3, maxc - minc + 3))

    # Mark clay
    for r, c in clay:
        grid[r - minr + 1, c - minc + 1] = 1

    # Mark still water
    for r, c in still_water:
        grid[r - minr + 1, c - minc + 1] = 2

    # Mark flowing water
    for r, c in flow_water:
        grid[r - minr + 1, c - minc + 1] = 3

    # Plot the grid
    plt.imshow(grid, cmap='viridis', interpolation='nearest')
    plt.colorbar(ticks=[0, 1, 2, 3], label='0: Empty, 1: Clay, 2: Still Water, 3: Flowing Water')
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.title('Water Flow Visualization')
    plt.show()


# takes about 40 seconds to complete for both parts
def main():
    still = set()
    flowing = set()
    solve(source, clay, still, flowing)

    # remove all duplicates
    flowing -= still
    flowing -= clay
    # remove all out of bounds
    flowing = set([el for el in flowing if inside(el)])

    print(len(still) + len(flowing))
    print(len(still))

    visualize_grid(clay, still, flowing)


main()
