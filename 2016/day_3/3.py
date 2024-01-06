import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

L = [[int(el) for el in line.split()] for line in L]

p1 = 0
for tri in L:
    tri = sorted(tri)
    if tri[0] + tri[1] > tri[2]:
        p1 += 1

print(p1)

p2 = 0
for j in range(len(L[0])):
    col = [line[j] for line in L]
    for i in range(len(col) // 3):
        tri = col[3 * i: 3 * i + 3]
        tri.sort()
        if tri[0] + tri[1] > tri[2]:
            p2 += 1

print(p2)
