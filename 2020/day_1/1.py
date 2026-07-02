import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')
nums = [int(el) for el in L]


def p1():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            n1, n2 = nums[i], nums[j]
            if n1 + n2 == 2020:
                print(n1 * n2)
                return


def p2():
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                n1, n2, n3 = nums[i], nums[j], nums[k]
                if n1 + n2 + n3 == 2020:
                    print(n1 * n2 * n3)
                    return


p1()
p2()
