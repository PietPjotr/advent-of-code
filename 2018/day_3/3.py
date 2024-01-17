import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')

visited = set()
overlap = set()
for claim in L:
    nums = re.findall(r'\d+', claim)
    ID, cs, rs, w, h = [int(el) for el in nums]
    over = True
    for r in range(rs, rs + h):
        for c in range(cs, cs + w):
            if (r, c) in visited:
                over = False
                overlap.add((r, c))
            else:
                visited.add((r, c))

print(len(overlap))

p2 = 0
for claim in L:
    nums = re.findall(r'\d+', claim)
    ID, cs, rs, w, h = [int(el) for el in nums]
    over = True
    for r in range(rs, rs + h):
        for c in range(cs, cs + w):
            if (r, c) in overlap:
                over = False

    if over:
        p2 = ID

print(p2)
