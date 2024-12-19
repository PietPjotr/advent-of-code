import sys
from math import prod


def calc_new_position(x, y, dx, dy, w, h, seconds):
    x2 = (x + dx * seconds) % w
    y2 = (y + dy * seconds) % h
    x = x2 if x2 >= 0 else x2 + w
    y = y2 if y2 >= 0 else y2 + h
    return (x, y)


def calc_quadrant(x, y):
    qx = x // (w // 2)
    qy = y // (h // 2)
    quad = qx + 1 if qx < 2 else qx
    quad += 2 if qy > 0 else 0
    return quad


data = open('inputs/inp.txt').read().strip()
# data = open(sys.argv[1]).read().strip()

w, h = 101, 103
seconds = 100

quad_counter = [0, 0, 0, 0]
neighbors_counter = []
for i in range(10000):
    neighbors = 0
    positions = set()
    for robot in data.split("\n"):
        pos, velocity = robot.split(" ")
        x, y = map(int, pos.replace("p=", "").split(","))
        dx, dy = map(int, velocity.replace("v=", "").split(","))
        new_x, new_y = calc_new_position(x, y, dx, dy, w, h, i + 1)
        positions.add((new_x, new_y))

        if i == 99:
            if new_x == w // 2 or new_y == h // 2:
                continue
            quad = calc_quadrant(new_x, new_y)
            quad_counter[quad - 1] = quad_counter[quad - 1] + 1

    for x, y in positions:
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (x2, y2) in positions:
                neighbors += 1
    neighbors_counter.append(neighbors)

print(f"Part 1: {prod(quad_counter)}")
print(f"Part 2: {neighbors_counter.index(max(neighbors_counter)) + 1}")