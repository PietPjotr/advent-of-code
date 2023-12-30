import sys
sys.path.append('..')
import my_parser as p
import heapq

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
    sources = replacements.keys()
    distinct = set()
    for i in range(len(mol)):
        for source in sources:
            if mol[i:].startswith(source):
                for to in replacements[source]:
                    new = mol[:i] + to + mol[min(i + len(source), len(mol)):]
                    distinct.add(new)

    return distinct

def p1():
    p1 = replace(mol)
    print(len(p1))


def removals(mol):
    distinct = set()
    for source in replacements:
        for dest in replacements[source]:
            for i in range(len(mol)):
                if mol[i:].startswith(dest):
                    new = mol[:i] + source + mol[min(i + len(dest), len(mol)):]
                    distinct.add(new)
    # return sorted(list(distinct), key=lambda x: len(x))
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

def solve2(mol):
    init_len = len(mol)
    start = mol
    i = 1
    hq = [(len(start), 0, start, i)]
    heapq.heapify(hq)
    while hq:
        cur_len, same, mol, i = heapq.heappop(hq)
        print(i, len(mol))
        if mol == 'e':
            print(i - 1)
        if same > 2:
            continue
        neighs = removals(mol)
        for neigh in neighs:
            if len(neigh) == len(mol):
                same += 1
            else:
                same = 0
            heapq.heappush(hq, ((init_len - len(neigh)) / i, same, neigh, i + 1))

# solve2(mol)

