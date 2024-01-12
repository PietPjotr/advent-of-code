import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')[0]
lines = [int(el) for el in L.split()]


def distribute(lines, i):
    el = lines[i]
    lines[i] = 0
    j = i + 1
    while el > 0:
        lines[j % len(lines)] += 1
        el -= 1
        j += 1
    return lines


seen = {}
p1 = 0
while tuple(lines) not in seen:
    seen[(tuple(lines))] = p1
    i = lines.index(max(lines))
    lines = distribute(lines, i)
    p1 += 1

print(p1)
print(p1 - seen[tuple(lines)])
