import sys
sys.path.append('..')
import my_parser as p
import re
from matplotlib import pyplot as plt

L = p.input_as_lines('inputs/inp.txt')

points = []
for line in L:
    nums = re.findall(r'-?\d+', line)
    nums = list(map(int, nums))
    points.append(nums)


def step(points, time):
    new = []
    for x, y, dx, dy in points:
        x += dx * time
        y += dy * time
        new.append([x, y, dx, dy])

    return new


xs = [point[0] for point in points]
min_x, max_x = round(min(xs)), round(max(xs))
ys = [point[1] for point in points]
min_y, max_y = round(min(ys)), round(max(ys))


def show(points):
    coords = [(round(point[0]), round(point[1])) for point in points]
    img = []
    xs = [point[0] for point in points]
    min_x, max_x = round(min(xs)), round(max(xs))
    ys = [point[1] for point in points]
    min_y, max_y = round(min(ys)), round(max(ys))

    for r in range(min_y, max_y + 1):
        row = []
        for c in range(min_x, max_x + 1):
            if (c, r) in coords:
                row.append(1)
            else:
                row.append(0)
        img.append(row)
    return img

steps = 0
while max_x - min_x > 100:
    steps += 1000
    points = step(points, 1000)
    xs = [point[0] for point in points]
    min_x, max_x = min(xs), max(xs)

for i in range(100):
    steps += 1
    points = step(points, 1)
    xs = [point[0] for point in points]
    min_x, max_x = min(xs), max(xs)
    if max_x - min_x < 100:
        print(steps)
        img = show(points)
        plt.imshow(img)
        plt.show()

# analytically determined
print(10003)

