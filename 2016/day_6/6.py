import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

p1 = ''
p2 = ''
for i in range(len(L[0])):
    col = [el[i] for el in L]
    freq = sorted(col, key=lambda x: (-col.count(x), x))
    p1 += freq[0]
    p2 += freq[-1]

print(p1)
print(p2)
