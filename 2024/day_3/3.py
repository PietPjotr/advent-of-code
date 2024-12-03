import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_string('inputs/inp.txt')

# p1
x = re.findall(r'mul\((\d+),(\d+)\)', L)
x = [(int(el[0]), int(el[1])) for el in x]

print(sum([el[0] * el[1] for el in x]))

# p2
L = L.split('do()')
x = []
for l in L:
    l = l.split("don't()")
    x.extend(re.findall(r'mul\((\d+),(\d+)\)', l[0]))

x = [(int(el[0]), int(el[1])) for el in x]

print(sum([el[0] * el[1] for el in x]))
