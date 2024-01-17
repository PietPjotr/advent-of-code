import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

ks = []
for l in L:
    nums = re.findall(r'\d+', l)
    ks.append(tuple([int(el) for el in nums]))

ordered = sorted(zip(L, ks), key=lambda x: x[1])
sort = [el[0] for el in ordered]

guards = {}
guard = 0
sleep = 0
for line in sort:
    times, rest = line.split('[ ')
    guard = re.findall(r'\d+', rest)
    times = [int(el) for el in re.findall(r'\d+', times)]
    if guard:
        guard = int(guard)
        if guard not in guards:
            guards[guard] = [0 for _ in range(60)]
    else:
        # find if we have a wakes up and add all the numbers in the
        # the range wakes up - sleep to the minute in list of the guard
        # in the guards dict


