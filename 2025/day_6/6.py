import sys
sys.path.append('..')
import my_parser as p
import utils as u
from utils import prod
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')

# look at operators and use those to split the blocks
c_split = [-1]
ops = [L[-1][0]]
for i in range(len(L[-1][:-1])):
    j = i + 1
    one, two = L[-1][i], L[-1][j]
    if one == ' ' and two in '*+':
        c_split.append(i)
        ops.append(two)
c_split.append(len(L[0]))

# loop over the seperated blocks
p1 = p2 = 0
idx = 0
for i, j in zip(c_split[:-1], c_split[1:]):
    block = []
    for r in range(len(L) - 1):
        block.append(L[r][i + 1:j])

    # go colwise for p2
    nums2 = []
    for c in range(len(block[0])):
        num_str = ''
        for r in range(len(block)):
            num_str += block[r][c]
        nums2.append(int(num_str))

    # map to int for p1
    nums1 = [int(row) for row in block]

    # calc
    op = ops[idx]
    if op == '*':
        tp1 = prod(nums1)
        tp2 = prod(nums2)
    elif op == '+':
        tp1 = sum(nums1)
        tp2 = sum(nums2)

    p1 += tp1
    p2 += tp2
    idx += 1

print(p1)
print(p2)
