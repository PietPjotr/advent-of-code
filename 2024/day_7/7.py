import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

L = p.input_as_lines('inputs/inp.txt')
# G = p.input_as_grid('inputs/inp.txt')
# R = len(G)
# C = len(G[0])

p1 = 0
for line in L:
    res, nums = line.split(': ')
    nums = [int(el) for el in nums.split()]

    possibilities = 2 ** (len(nums) - 1)
    for i in range(possibilities):
        b = bin(i)
        b = b[2:]
        b = (len(nums) - 1 - len(b)) * '0' + b
        cur = nums[0]
        for i, el in enumerate(nums[1:]):
            op = int(b[i])
            if op == 0:
                cur += el
            else:
                cur *= el
        if cur == int(res):
            p1 += int(res)
            break

print(p1)


p2 = 0
for line in L:
    res, nums = line.split(': ')
    nums = [int(el) for el in nums.split()]

    possibilities = 3 ** (len(nums) - 1)
    for i in range(possibilities):
        b = ""
        while i > 0:
            b = str(i % 3) + b
            i //= 3
        b = (len(nums) - 1 - len(b)) * '0' + b

        cur = nums[0]
        for i, el in enumerate(nums[1:]):
            op = int(b[i])
            if op == 0:
                cur += el
            elif op == 1:
                cur *= el
            elif op == 2:
                cur = int(str(cur) + str(el))

        if cur == int(res):
            p2 += int(res)
            break

print(p2)