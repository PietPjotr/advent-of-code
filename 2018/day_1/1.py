import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

lines = [int(el) for el in L]
print(sum(lines))
visited = set([0])
i = 0
freq = 0
while True:
    line = lines[i % len(lines)]
    freq += line
    if freq in visited:
        print(freq)
        break
    visited.add(freq)
    i += 1

