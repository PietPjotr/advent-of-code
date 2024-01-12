import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')

struct = {}
for line in L:
    weight = re.findall(r'[0-9]+', line)[0]
    weight = int(weight)
    names = re.findall(r'[a-z]+', line)
    cur = names[0]
    rest = names[1:]
    struct[cur] = (weight, rest)

names = set(struct.keys())
for k, v in struct.items():
    weight, dests = v
    for name in dests:
        names.remove(name)

print(list(names)[0])


def get_weight(nodes, name):
    weight, dests = nodes[name]
    return [struct[dest][0] + sum(get_weight(nodes, dest)) for dest in dests]


lowest = ''
mweight = float('inf')
for name in struct.keys():
    weights = get_weight(struct, name)
    if not all([weight == weights[0] for weight in weights]):
        if weights[0] < mweight:
            mweight = weights[0]
            lowest = name

weights = get_weight(struct, lowest)
s = sorted(weights, key=lambda x: weights.count(x))
delta = s[-1] - s[0]
i = weights.index(s[0])
print(struct[struct[lowest][1][i]][0] + delta)


