import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

def valid(line):
    for i, el in enumerate(line):
        for j, el2 in enumerate(line[i+1:]):
            if el == el2:
                return False
    return True


def valid2(line):
    for i, el in enumerate(line):
        for j, el2 in enumerate(line[i+1:]):
            if sorted(el) == sorted(el2):
                return False
    return True


p1 = 0
p2 = 0
for line in L:
    line = line.split()
    if valid(line):
        p1 += 1
    if valid2(line):
        p2 += 1

print(p1)
print(p2)
