import sys
sys.path.append('..')
import my_parser as p
import re
import matplotlib.pyplot as plt
import numpy as np

L = p.input_as_lines('inputs/inp.txt')
bots = []
for l in L:
    nums = [int(el) for el in re.findall(r'-?\d+', l)]
    bots.append(nums)


def distance(b1, b2):
    return sum([abs(b1[i] - b2[i]) for i in range(3)])


def p1():
    ranges = [bot[-1] for bot in bots]
    maxr = max(ranges)
    maxb = bots[ranges.index(maxr)]

    print(sum([1 if distance(maxb, b) <= maxr else 0 for b in bots]))


p1()


def inside_of(bots, point):
    inside = 0
    for bot in bots:
        if sum([abs(bot[i] - point[i]) for i in range(3)]) <= bot[-1]:
            inside += 1
    return inside


# try some maximization over all dimensions by slowly decreasing the range
# every time, for some reason this works when only using 1 point per dimension
# per range decrease
# NOTE: there is a chance that the no_points or fraction variables need some
# tinkering per input, no_points higher or more importantly: fraction higher:
# but still between 1 and 0, otherwise the code will not terminate
def p2(bots):
    a = 10**8
    point = [0, 0, 0]
    inside = 0
    no_points = 2
    fraction = 0.9
    # as long as the range that we consider is greater than 0
    while a > 0:

        # loop over every dimension
        for d in range(3):
            best = -1

            # loop over no_points within the range of the current dimension point
            for nd in range(-a + point[d], a + point[d] + 1, max(1, int(2 * a / no_points))):
                npoint = point.copy()
                npoint[d] = nd
                ninside = inside_of(bots, npoint)

                if ninside > inside or (ninside == inside and nd < point[d]):
                    best = nd
                    inside = ninside

            if best != -1:
                point[d] = best

        # decrease the range
        a = int(fraction * a)

    print(sum([abs(point[i]) for i in range(3)]))


p2(bots)
