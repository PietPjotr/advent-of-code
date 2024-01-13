import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')

g = [[] for _ in range(len(L))]
for line in L:
    nums = [int(el) for el in re.findall(r'[0-9]+', line)]
    for num in nums[1:]:
        g[nums[0]].append(num)

groups = set()
for i in range(len(L)):
    connected = set()
    stack = [i]
    while stack:
        el = stack.pop(0)
        connected.add(el)
        for dest in g[el]:
            if dest not in connected:
                stack.append(dest)

    if i == 0:
        print(len(connected))
    groups.add(tuple(sorted(connected)))

print(len(groups))








