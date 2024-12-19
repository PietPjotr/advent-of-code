import sys
sys.path.append('..')
import my_parser as p
import re
from collections import defaultdict
import matplotlib.pyplot as plt


W, H = 101, 103
# W, H = 11, 7

L = p.input_as_lines('inputs/inp.txt')

bots = []

for line in L:
    nums = [int(el) for el in re.findall(r'-?\d+', line)]
    bots.append(nums)


def show(bots):
    pos_bots = [(x, y) for x, y, _, _ in bots]
    plt.scatter(*zip(*pos_bots))
    plt.draw()


iterations = 10000
for it in range(iterations):

    # Update the positions of all bots
    for i, (x, y, dx, dy) in enumerate(bots):
        nx = (x + dx) % W  # Wrap around horizontally
        ny = (y + dy) % H  # Wrap around vertically
        bots[i] = [nx, ny, dx, dy]

    x_pos = defaultdict(int)
    y_pos = defaultdict(int)

    for x, y, _, _ in bots:
        x_pos[x] += 1
        y_pos[y] += 1

    # Check if any x position has more than 20 bots
    for x, count in x_pos.items():
        for y, count_y in y_pos.items():
            if count > 20 and count_y > 20:
                print(f'Christmas tree found at iteration {it + 1}')
                show(bots)
                plt.show()
                break


qs = [0, 0, 0, 0]
for x, y, _, _ in bots:
    if x < W // 2:
        if y < H // 2:
            qs[0] += 1
        elif y > H // 2:
            qs[1] += 1
    elif x > W // 2:
        if y < H // 2:
            qs[2] += 1
        elif y > H // 2:
            qs[3] += 1

p1 = 1
for n in qs:
    p1 *= n

print(p1)
