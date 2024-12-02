import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
L = [int(el) for el in L]

# part 1
print(sum([el // 3 - 2 for el in L]))

# part 2
tot = 0
for el in L:
    score = 0
    while el > 0:
        el = el // 3 - 2
        score += max(el, 0)

    tot += score

print(tot)