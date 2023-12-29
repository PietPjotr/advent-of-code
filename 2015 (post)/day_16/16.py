import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

target = {'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1}

aunts = []
for line in L:
    words = re.findall(r'[a-z]+', line)
    numbers = [int(el) for el in re.findall(r'[0-9]+', line)]
    aunt = {}
    for i in range(1, len(words)):
        aunt[words[i]] = numbers[i]
    aunts.append(aunt)


def find_aunt():
    for i, aunt in enumerate(aunts):
        valid = []
        for k, v in aunt.items():
            # if k in target:
            if v != 0 and v != target[k]:
                break
            else:
                valid.append(1)
        if len(valid) == len(aunt):
            print(i + 1)
            break

find_aunt()

lt = {'cats', 'trees'}
gt = {'pomeranians', 'goldfish'}
def find_aunt2():
    for i, aunt in enumerate(aunts):
        valid = []
        for k, v in aunt.items():
            if k in lt:
                if v <= target[k]:
                    break
                valid.append(1)
            elif k in gt:
                if v >= target[k]:
                    break
                valid.append(1)
            else:
                if target[k] != v:
                    break
                valid.append(1)

        if len(valid) == len(aunt):
            print(i + 1)
            continue

find_aunt2()
