import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')

p1 = 0
p2 = 0
for l in L:
    l = l.replace('-', ' ')
    l = l.replace(':', '')
    l = l.split(' ')

    nums = [int(el) for el in l[0:2]]
    char = l[2]
    s = l[-1]

    ss = s[nums[0] - 1] + s[nums[1] - 1]
    if ss.count(char) == 1:
        p2 += 1
    if nums[0] <= s.count(char) <= nums[1]:
        p1 += 1

print(p1)
print(p2)