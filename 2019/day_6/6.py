import sys
sys.path.append('..')
import my_parser as p

from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')

els = set()
rhs = set()
orbits = defaultdict(set)
for l in L:
    left, right = l.split(')')
    els.add(left)
    els.add(right)
    rhs.add(right)
    orbits[left].add(right)


def part1():
    p1 = 0
    for el in els:
        cur = el
        while cur in rhs:
            for k, v in orbits.items():
                if cur in v:
                    p1 += 1
                    cur = k
    print(p1)


part1()

# part2
# path from YOU to COM in order (list)
# path from SAN to COM in order (list)
end = 'COM'
ss = ['YOU', 'SAN']
ps = []
for el in ss:
    p = []
    cur = el
    while cur in rhs:
        for k, v in orbits.items():
            if cur in v:
                cur = k
                p.append(cur)
    ps.append(p)

# find last similarity:
for i in range(1, len(ps[0])):
    a = ps[0][-i]
    b = ps[1][-i]
    if a != b:
        break

p1, p2 = ps
part2 = len(p1) - i + len(p2) - i + 2
print(part2)
