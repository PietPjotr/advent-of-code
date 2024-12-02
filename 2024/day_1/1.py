import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/test.txt')
L = p.input_as_grid('inputs/inp.txt')

l1 = [el[0] for el in L]
l2 = [el[1] for el in L]

l1.sort()
l2.sort()

# p1
p1 = 0
for i in range(len(l1)):
    p1 += abs(l1[i] - l2[i])

print(p1)

# p2
p2 = 0
for el in l1:
    p2 += el * l2.count(el)

print(p2)
