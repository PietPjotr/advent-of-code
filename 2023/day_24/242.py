import sys
sys.path.append('..')
import my_parser as p
import numpy as np

lines = p.input_as_lines('inputs/test.txt')
lines = [((eval(one)), (eval(two))) for line in lines for one, two in [line.split(' @ ')]]

# decide for some x what the y value is
a_bound = 200000000000000
b_bound = 400000000000000

a_bound = 7
b_bound = 27

def intersect(p, v, q, u):
    p, v, q, u = np.array(p), np.array(v), np.array(q), np.array(u)
    a = np.cross(v, u)
    dot = np.dot(a, a)
    if dot == 0:
        return None, None, None
    b = np.cross(q - p, u)
    t = np.dot(b, a) / dot
    if t < 0:
        return None, None, None
    point = p + t * v
    return point


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
    p, v = line1
    for line2 in lines[i + 1:]:
        q, u = line2
        intersection = intersect(p, v, q, u)
        if all([el is None for el in intersection]):
            continue
        elif all([a_bound < el < b_bound for el in intersection]):
            print(line1)
            print(line2)
            print('intersection found at point {}'.format(intersection))
            res += 1
        else:
            continue
print(res)

