import sys
sys.path.append('..')
import my_parser as p
import numpy as np
from numpy.linalg import inv

lines = p.input_as_lines('inputs/inp.txt')
lines = [((eval(one)), (eval(two))) for line in lines for one, two in [line.split(' @ ')]]

# decide for some x what the y value is
a_bound = 200000000000000
b_bound = 400000000000000

# a_bound = 7
# b_bound = 27

def get_coefficients(x, vx, y, vy):
    a = vy / vx
    b = y - a * x
    return a, b

def intersect(a, c, b, d):
    if a == b:
        if c != d:
            return None, None
        else:
            return True, True

    x = (d - c) / (a - b)
    y = a * x + c
    return x, y


def in_future(x_intersect, x1, x2, xv1, xv2):
    one = False
    two = False
    if x_intersect < x1 and xv1 < 0 or x_intersect > x1 and xv1 > 0:
        one = True
    if x_intersect < x2 and xv2 < 0 or x_intersect > x2 and xv2 > 0:
        two = True
    return one and two


res = 0
for i, line1 in enumerate(lines):
    # print(line1)
    x1, y1 = line1[0][:2]
    xv1, yv1 = line1[1][:2]
    a1, b1, = get_coefficients(x1, xv1, y1, yv1)
    for line2 in lines[i + 1:]:
        x2, y2 = line2[0][:2]
        xv2, yv2 = line2[1][:2]
        a2, b2, = get_coefficients(x2, xv2, y2, yv2)
        x_intersect, y_intersect = intersect(a1, b1, a2, b2)
        if x_intersect is None and y_intersect is None:
            continue
        elif x_intersect == True and y_intersect == True:
            res += 1
        elif a_bound < x_intersect < b_bound and a_bound < y_intersect < b_bound:
            if not in_future(x_intersect, x1, x2, xv1, xv2):
                continue
            res += 1
        else:
            continue
print(res)

# part2
# thank god for https://www.reddit.com/r/adventofcode/comments/18q40he/2023_day_24_part_2_a_straightforward_nonsolver/
# eq for X and Y = (dy'-dy) X + (dx-dx') Y + (y-y') DX + (x'-x) DY = x' dy' - y' dx' - x dy + y dx
# eq for X and Z = (dz'-dz) X + (dx-dx') Z + (z-z') DX + (x'-x) DZ = x' dz' - z' dx' - x dz + z dx
A = []
B = []
C = []
D = []
for i in range(1):
    p, v = lines[i]
    x, y, z = p
    dx, dy, dz = v
    for j in range(i + 1, i + 5):
        q, u = lines[j]
        x_, y_, z_ = q
        dx_, dy_, dz_ = u
        A.append([dy_ - dy, dx - dx_, y - y_, x_ - x])
        B.append(x_ * dy_ - y_ * dx_ - x * dy + y * dx)

        C.append([dz_ - dz, dx - dx_, z - z_, x_ - x])
        D.append(x_ * dz_ - z_ * dx_ - x * dz + z * dx)

# solving linear system xy in xy variable
A = np.array(A)
B = np.array(B)
xy = inv(A) @ B

# solving linear system xz in xz variable
C = np.array(C)
D = np.array(D)
xz = inv(C) @ D

final = np.array([xy[0], xy[1], xz[1], xy[2], xy[3], xz[3]])

# some fp errors could occur since int rounds down and not to nearest but for my case it works
assert final[0] + final[1] + final[2] == int(final[0] + final[1] + final[2])
print(int(final[0] + final[1] + final[2]))
