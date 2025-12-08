import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict
from sortedcontainers import SortedList

L = p.input_as_lines('inputs/inp.txt')


def dist(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i] - b[i])**2
    return d

js = []
for l in L:
    nums = u.get_all_numbers(l)
    js.append(tuple(nums))

top_ds = SortedList(key=lambda x: x[0])
top = SortedList(key=lambda x: x[0])

for i in range(len(js)):
    one = js[i]
    for j in range(i + 1, len(js)):
        two = js[j]
        d = dist(one, two)
        top_ds.add((d, i, j))
        top.add((d, i, j))

        if len(top_ds) > 1000:
            top_ds.pop(-1)


def reduce(ds, p2=False):
    ccs = []
    visited = set()
    for d, a, b in ds:
        if a in visited and b in visited:
            ca = set()
            for c in ccs:
                if a in c:
                    ca = c
                    break
            if a in ca and b in ca:
                continue
            cb = set()
            for c in ccs:
                if b in c:
                    cb = c
                    break
            ca |= cb
            if cb in ccs:
                ccs.remove(cb)
        elif a in visited:
            for c in ccs:
                if a in c:
                    c.add(b)
                    visited.add(b)
        elif b in visited:
            for c in ccs:
                if b in c:
                    c.add(a)
                    visited.add(a)
        elif a not in visited and b not in visited:
            ccs.append(set([a, b]))
            visited.add(a)
            visited.add(b)

        if p2:
            if len(ccs) == 1 and len(ccs[0]) == 1000:
                p2 = js[a][0] * js[b][0]
                return p2
    else:
        return ccs


p1ccs = reduce(top_ds)
p1ccs.sort(key=lambda x: -len(x))
p1 = u.prod(len(el) for el in p1ccs[:3])
print(p1)

p2 = reduce(top, True)
print(p2)
