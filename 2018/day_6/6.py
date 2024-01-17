import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

coords = [tuple(int(el) for el in line.split(', ')[::-1]) for line in L]
rs = [r for r, c in coords]
cs = [c for r, c in coords]

min_r = min(rs)
max_r = max(rs)

min_c = min(cs)
max_c = max(cs)


def find_closest(pos):
    """Gets the closest coord to a given point returns None if there are is a
    tie between two or more coords"""
    r, c = pos
    distances = []
    for coord in coords:
        distances.append(tuple((abs(coord[0] - r) + abs(coord[1] - c), coord)))
    distances.sort()
    if distances[0][0] == distances[1][0]:
        return None
    else:
        return distances[0][1]


def get_infinite_coords():
    """Creates the set of all coords that have infinite area"""
    infinite = set()
    for r in range(min_r - 1, max_r + 2):
        for c in [min_c, max_c]:
            closest = find_closest((r, c))
            if closest:
                infinite.add((r, c))
    for c in range(min_c - 1, max_c + 2):
        for r in [min_r, max_r]:
            closest = find_closest((r, c))
            if closest:
                infinite.add((r, c))

    return infinite


def get_points_to_coord():
    """Creates a dict with for every coord all the points that are closest to
    that coord"""
    points = {coord: set() for coord in coords}
    for r in range(min_r - 1, max_r + 2):
        for c in range(min_c - 1, max_c + 2):
            closest = find_closest((r, c))
            if closest:
                points[closest].add((r, c))
    return points


def p1():
    infinite = get_infinite_coords()
    points = get_points_to_coord()
    p1 = 0
    for k, v in points.items():
        if k in infinite:
            continue
        if len(v) > p1:
            p1 = len(v)

    print(p1)


p1()


def get_distances(pos):
    r, c = pos
    return [abs(coord[0] - r) + abs(coord[1] - c) for coord in coords]


def p2():
    p2 = 0
    for r in range(min_r - 1, max_r + 2):
        for c in range(min_c - 1, max_c + 2):
            distances = get_distances((r, c))
            if sum(distances) < 10000:
                p2 += 1

    print(p2)


p2()
