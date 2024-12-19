import sys
sys.path.append('..')
import my_parser as p
import re
from collections import defaultdict
import matplotlib.pyplot as plt


W, H = 101, 103
L = p.input_as_lines('inputs/inp.txt')
bots = []

for line in L:
    nums = [int(el) for el in re.findall(r'-?\d+', line)]
    bots.append(nums)


def show(bots):
    pos_bots = [(x, -y + 100) for x, y, _, _ in bots]
    plt.scatter(*zip(*pos_bots), s=5)
    plt.draw()


def update(bots):
    for i, (x, y, dx, dy) in enumerate(bots):
        nx = (x + dx) % W
        ny = (y + dy) % H
        bots[i] = [nx, ny, dx, dy]
    return bots


def find_christmas_tree(bots):
    iterations = 10000
    for it in range(1, iterations):

        bots = update(bots)

        x_pos = defaultdict(int)
        y_pos = defaultdict(int)

        for x, y, _, _ in bots:
            x_pos[x] += 1
            y_pos[y] += 1

        # Check if there are an x and y pos with both more than 20 bots
        for x, count in x_pos.items():
            for y, count_y in y_pos.items():
                if count > 20 and count_y > 20:
                    show(bots)
                    plt.show()
                    return it + 100  # already start with 100 iterations a



def get_quartiles(bots):
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
    return qs


def score(quartiles):
    p1 = 1
    for n in quartiles:
        p1 *= n

    return p1


for i in range(100):
    bots = update(bots)

qs = get_quartiles(bots)
p1 = score(qs)
print(p1)

p2 = find_christmas_tree(bots)
print(p2)
