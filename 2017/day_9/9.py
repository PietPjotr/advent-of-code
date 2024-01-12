import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')[0]
L = re.sub(r'(!.)', '', L)
L1 = re.sub(r'\"|\'', '', L)
L1 = re.sub(r'<(.*?)>', '', L1)
L1 = re.sub(r'[^{}]', '', L1)


def get_score(line):
    score = 0
    level = 0
    for char in line:
        if char == '{':
            level += 1
        elif char == '}':
            score += level
            level -= 1

    return score


def get_score2(line):
    score = 0
    i = 0
    while i < len(line):
        el = line[i]
        if el == '<':
            i += 1
            el = line[i]
            while el != '>':
                score += 1
                i += 1
                el = line[i]
            i += 1
        i += 1

    return score


print(get_score(L1))
print(get_score2(L))
