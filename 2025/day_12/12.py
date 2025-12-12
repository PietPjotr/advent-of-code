import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

S = p.input_as_string('inputs/inp.txt')

blocks = S.split('\n\n')
lines = blocks[-1]
shapes = []
for shape in blocks[0:6]:
    shape = shape.split()
    rows = shape[1:]
    shapes.append([r for r in rows])

def to_string(rows):
    return ''.join(rows)

sizes = []
for shape in shapes:
    sizes.append(to_string(shape).count('#'))

p1 = 0
for l in lines.splitlines():
    ns = u.get_all_numbers(l)
    w, h = ns[0:2]
    nshapes = ns[2:]

    surface = w * h
    min_used = 0
    for i, n in enumerate(nshapes):
        min_used += sizes[i] * n
    if min_used > surface:
        continue
    else:
        p1 += 1

print(p1)
