import sys
sys.path.append('..')
import my_parser as p
import heapq
import re

L = p.input_as_lines('inputs/inp.txt')

rules, mol =  L[0:-2], L[-1]

replacements = {}
for rule in rules:
    fro, to = rule.split(' => ')
    if fro in replacements:
        replacements[fro].append(to)
    else:
        replacements[fro] = [to]


def replace(mol):
    distinct = set()
    for i in range(len(mol)):
        for source in replacements:
            if mol[i:].startswith(source):
                for to in replacements[source]:
                    new = mol[:i] + to + mol[min(i + len(source), len(mol)):]
                    distinct.add(new)

    return distinct

def p1():
    p1 = replace(mol)
    print(len(p1))

p1()

def removals(mol):
    distinct = set()
    for source in replacements:
        for dest in replacements[source]:
            for i in range(len(mol)):
                if mol[i:].startswith(dest):
                    new = mol[:i] + source + mol[min(i + len(dest), len(mol)):]
                    distinct.add(new)
    return distinct


def solve2_luck():
    start = mol
    i = 0
    while start != 'e':
        print(i, len(start))
        shortest = start
        neighs = removals(start)
        shortest_len = float('inf')
        for neigh in neighs:
            if len(neigh) < shortest_len:
                shortest_len = len(neigh)
                shortest = neigh
        start = shortest
        i += 1
        if i > 207:
            break

    print(i)


# solve2_luck()

# wtf: https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju
def solve2():

    print(
        len(re.findall(r"[A-Z]", mol))
        - 2 * len(re.findall(r"Rn", mol))
        - 2 * len(re.findall(r"Y", mol))
        - 1
    )

solve2()