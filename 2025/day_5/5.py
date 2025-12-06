import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')

res = 0
ranges = []
for l in L:
    if '-' in l:
        one, two = [int(el) for el in l.split('-')]
        ranges.append((one, two))

    if '-' not in l and l:
        id = u.get_all_numbers(l)
        for s, e in ranges:
            if s <= id <= e:
                res += 1
                break
print(res)

ranges.append((float('inf'), float('inf')))
ranges.sort()

p2 = 0
i = 0
s1, e1 = ranges[i]
j = 1
while j < len(ranges):
    s2, e2 = ranges[j]
    to_add = False

    # overlap: generate one big range
    if s2 <= e1 and e2 > e1:
        e1 = e2
        to_add = True
    # no overlap: go to the next pair and add current to the score p2
    elif s2 > e1:
        p2 += e1 - s1 + 1
        i = j
        s1, e1 = ranges[i]
    j += 1

# if we end with overlap we still need to add the overlapped range
if to_add:
    p2 += e1 - s1 + 1
print(p2)
