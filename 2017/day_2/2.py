import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])


def div(l):
    for num1 in l:
        for num2 in l:
            if num1 % num2 == 0 and num1 != num2:
                return num1 // num2

p1 = 0
p2 = 0
for l in L:
    l = l.split()
    l = [int(el) for el in l]
    p1 += max(l) - min(l)
    p2 += div(l)

print(p1)
print(p2)
