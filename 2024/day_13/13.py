import sys
sys.path.append('..')
import my_parser as p
import re
import numpy as np


S = p.input_as_string('inputs/inp.txt')
parts = [el for el in S.split('\n\n')]


# derived solve function for more complexity and slower solve time ;)
def solve(x1, y1, x2, y2, x3, y3):
    a = (y3 * x2 - x3 * y2) / (x2 * y1 - x1 * y2)
    b = (y3 * x1 - x3 * y1) / (x1 * y2 - x2 * y1)
    return a, b


p1 = 0
for p in parts:
    x1, y1, x2, y2, x3, y3 = [int(el) for el in re.findall(r'\d+', p)]

    A = np.array([[x1, x2], [y1, y2]])
    B = np.array([x3, y3])
    a, b = np.linalg.solve(A, B)

    if abs(round(a) - a) < 0.0001 and abs(round(b) - b) < 0.0001 and a <= 100 and b <= 100:
        a = round(a)
        b = round(b)
        p1 += a * 3 + b

print(p1)


p2 = 0
N = 10000000000000
for p in parts:
    x1, y1, x2, y2, x3, y3 = [int(el) for el in re.findall(r'\d+', p)]

    x3 += N
    y3 += N

    A = np.array([[x1, x2], [y1, y2]])
    B = np.array([x3, y3])
    a, b = np.linalg.solve(A, B)

    if abs(round(a) - a) < 0.0001 and abs(round(b) - b) < 0.0001:
        a = round(a)
        b = round(b)
        p2 += a * 3 + b

print(p2)
