import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
inp = L[0]

p1 = 0
p2 = 0
for i in range(len(inp) - 1):
    w1 = inp[i] + inp[(i + 1) % len(inp)]
    if w1[0] == w1[1]:
        p1 += int(w1[0])
    w2 = inp[i] + inp[(i + len(inp) // 2) % len(inp)]
    if w2[0] == w2[1]:
        p2 += int(w2[1])

print(p1)
print(p2)