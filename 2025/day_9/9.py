import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')

cs = []
for l in L:
    ns = u.get_all_numbers(l)
    cs.append(ns)

xs = sorted([el[0] for el in cs])
MINX, MAXX = xs[0], xs[-1]
ys = sorted([el[1] for el in cs])
MINY, MAXY = ys[0], ys[-1]

best = (0, 0, 0)
for i in range(len(cs)):
    a, b = cs[i]
    for j in range(i + 1, len(cs)):
        c, d = cs[j]
        area = (abs(a - c) + 1) * (abs(b - d) + 1)
        if area > best[0]:
            best = (area, i, j)

print(best[0])


def get_points(one, two):
    minx, maxx = sorted((one[0], two[0]))
    miny, maxy = sorted((one[1], two[1]))
    p1 = minx, miny
    p2 = minx, maxy
    p3 = maxx, maxy
    p4 = maxx, miny
    return [p1, p2, p3, p4]


# in this function i want to check if the lines p1p2 and p3p4 intersect
def intersect(p1, p2, p3, p4):
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

    return ccw(p1, p3, p4) != ccw(p2, p3, p4) and ccw(p1, p2, p3) != ccw(p1, p2, p4)


# use raycasting to check if point is inside the polygon
def inside(p, cs):
    ray_end = (MAXX + 10, p[1] + 0.1)
    intersections = 0
    for i in range(len(cs)):
        p1 = cs[i]
        p2 = cs[(i + 1) % len(cs)]
        if intersect(p, ray_end, p1, p2):
            intersections += 1

    return intersections % 2 == 1


def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def get_rectangle_points(p1, p2):
    minx, maxx = sorted((p1[0], p2[0]))
    miny, maxy = sorted((p1[1], p2[1]))
    # Shrink inward by 0.5 to avoid edge cases
    return [(minx + 0.5, miny + 0.5), (minx + 0.5, maxy - 0.5), (maxx - 0.5, maxy - 0.5), (maxx - 0.5, miny + 0.5)]


# hard coded cheese figured out by plotting which indices will surely
# be part of the largest rectangle denoted by p_up and p_down.
p_up = cs[248]
p_down = cs[249]
pup = sorted([el for el in cs if el[1] >= p_up[1]], key=lambda x: x[1], reverse=True)
pdown = sorted([el for el in cs if el[1] <= p_down[1]], key=lambda x: x[1])


# Find best rectangle above p_up
best_up = (0, None)
for point in pup:
    if point != p_up:
        rect_points = get_rectangle_points(p_up, point)
        inside_check = [inside(p, cs) for p in rect_points]
        if all(inside_check):
            rect_area = area(p_up, point)
            if rect_area > best_up[0]:
                best_up = (rect_area, point)

# Find best rectangle below p_down
best_down = (0, None)
for point in pdown:
    if point != p_down:
        rect_points = get_rectangle_points(p_down, point)
        inside_check = [inside(p, cs) for p in rect_points]
        if all(inside_check):
            rect_area = area(p_down, point)
            if rect_area > best_down[0]:
                best_down = (rect_area, point)

# Print the best area
print(max(best_up[0], best_down[0]))
