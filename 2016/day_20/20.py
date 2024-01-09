import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

a = 0
b = 4294967295

lines = [[int(el) for el in line.split('-')] for line in L]
lines.sort(key=lambda x: x[0])

for start, end in lines:
    if start <= a and a < end < b:
        a = end + 1

print(a)

a = 0
b = 4294967295
not_allowed = 0
for start, end in lines:
    if a > b:
        break
    if end < a or start > b:
        continue
    if a <= start <= b:
        if end <= b:
            not_allowed += end - start + 1
        elif end > b:
            not_allowed += b - start + 1
        a = end + 1
    elif start < a:
        if a <= end < b:
            not_allowed += end - a + 1
        elif end >= b:
            not_allowed += b - a + 1
        a = end + 1

print(4294967295 - not_allowed + 1)
