import sys
sys.path.append('..')
import my_parser as p

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
            # print('parallel')
            # print(line1)
            # print(line2)
            # print('intersection found at {}, {}'.format(x_intersect, y_intersect))
        elif a_bound < x_intersect < b_bound and a_bound < y_intersect < b_bound:
            if not in_future(x_intersect, x1, x2, xv1, xv2):
                continue
            res += 1
            # print(line1)
            # print(line2)
            # print('intersection found at {}, {}'.format(x_intersect, y_intersect))
        else:
            continue
print(res)

