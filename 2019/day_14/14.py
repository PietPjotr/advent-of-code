import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict
import numpy as np

L = p.input_as_lines('inputs/test.txt')

dep = {}

for line in L:
    result = line.split(line.split('=>')[-1])
    assert len(result) == 2, f"result: {result}"   # only one result per reaction
    words = get_all_words(line)
    numbers = get_all_numbers(line)

    dep[words[-1]] = [words[:-1], [numbers[-1]] + numbers[:-1]]


target = 'FUEL'
cost = 0

d = {target: 1}
next_d = {}

while d:
    print(d)
    next_d = {}
    for agent, amount in d.items():
        next_agents, nums = dep[agent]
        div = nums[0]
        next_nums = nums[1:]
        reactions = int(np.ceil(amount / div))
        if next_agents[0] == 'ORE':
            cost += next_nums[-1] * reactions

        for next_agent, react_num in zip(next_agents, next_nums):
            if next_agent in next_d:
                next_d[next_agent] += reactions * react_num
            else:
                next_d[next_agent] = reactions * react_num

    d = next_d

print(cost)