import sys
sys.path.append('..')
import my_parser as p
import re

lines = p.input_as_lines('inputs/inp.txt')

instructions = lines[0]
nodes = lines[2:]
n = {}

for node in nodes:
    nodes = re.findall(r'[A-Z]+', node)
    n[nodes[0]] = [nodes[1], nodes[2]]

current = 'AAA'
starting_nodes = [node for node in n if node.endswith('A')]
profiles = []

a_index = starting_nodes.index('AAA')

for current in starting_nodes:
    cycle = 0
    profile = []
    for i in range(10**8):

        ins = instructions[i % len(instructions)]

        if ins == 'L':
            current = n[current][0]
        elif ins == 'R':
            current = n[current][1]

        cycle += 1

        if current.endswith('Z'):
            if cycle in profile:
                profiles.append(profile[0])
                break
            profile.append(cycle)
            cycle = 0

# This was not the original code, but the answer of 1 was used for
# part two so I'll just be lazy and keep it like this.
print(profiles[a_index])

import math
res = math.lcm(*profiles)

print(res)




