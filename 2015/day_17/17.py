import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

liters = 150

lines = [int(el) for el in L]

combs = set()
DP = set()
stack = []
for i in range(len(lines)):
    over = list(range(len(lines)))
    over.remove(i)
    stack.append(([i], over))


def solve1():
    while stack:
        cont, over = stack.pop()
        DP.add(tuple(sorted(cont)))
        if sum([lines[i] for i in cont]) == liters:
            combs.add(tuple(sorted(cont)))
            continue
        for neigh in over:
            new_cont = cont + [neigh]
            new_over = over.copy()
            new_over.remove(neigh)
            if sum([lines[i] for i in new_cont]) <= liters and tuple(sorted(new_cont)) not in DP:
                stack.append((new_cont, new_over))

    print(len(combs))
    return combs


res = solve1()


def solve2():
    p2 = 0
    m = min([len(el) for el in res])
    for el in res:
        if len(el) == m:
            p2 += 1
    print(p2)


solve2()