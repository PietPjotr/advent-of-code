import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')
state = L[0]
rules = L[2:]
og_state = state.split()[2]
rules = {line.split(' => ')[0]: line.split(' => ')[1] for line in rules}


def score(state):
    ret = 0
    for i, el in enumerate(state):
        if el == '#':
            ret +=  i - n
    return ret


scores = []
n = 200
p1 = 0
state = n * '.' + og_state + n * '.'
for j in range(n):
    new = ''
    p1 += score(state)
    padded = '..' + state + '..'
    for i in range(len(padded) - 4):
        window = padded[i: i + 5]
        if window in rules:
            new += rules[window]
        else:
            new += '.'
    state = new

    cur_score = score(state)
    scores.append(cur_score)


print(scores[19])

deltas = [s2 - s1 for s1, s2 in zip(scores[:-1], scores[1:])]
if deltas[-2] == deltas[-1]:
    print(cur_score + (50000000000 - n) * deltas[-1])
else:
    print('increase the n value for part2')
