import sys
sys.path.append('..')
import my_parser as p
import re
import json

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

line = L[0]
nums = (map(int, re.findall(r'-?\d+', line)))
print(sum(nums))


def rec_sum(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(rec_sum(el) for el in obj)
    elif isinstance(obj, dict):
        if any(k == 'red' or v == 'red' for k, v in obj.items()):
            return 0
        return sum(rec_sum(k) + rec_sum(v) for k, v in obj.items())
    else:
        return 0


print(rec_sum(eval(line)))
