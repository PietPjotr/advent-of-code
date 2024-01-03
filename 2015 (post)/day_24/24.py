import sys
sys.path.append('..')
import my_parser as p
import itertools as it

L = p.input_as_lines('inputs/inp.txt')
lines = [int(el) for el in L]


def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p


def entanglement(nums, groups=3):
    score = sum(nums) // groups
    for i in range(2, len(nums)):
        contenders = []
        combs = it.combinations(nums, i)
        for comb in combs:
            if sum(comb) == score:
                contenders.append(comb)

        if contenders:
            contenders = sorted(contenders, key=lambda x: (len(x), prod(x)))
            group1 = contenders[0]
            return prod(group1)

print(entanglement(lines, 3))
print(entanglement(lines, 4))