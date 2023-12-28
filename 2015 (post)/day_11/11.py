import sys
sys.path.append('..')
import my_parser as p
import re
import itertools

L = p.input_as_lines('inputs/test.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

alphabet = 'abcdefghijklmnopqrstuvwxyz'

pairs = set([el + el for el in alphabet])

seqs = set([alphabet[i: i+3] for i in range(len(alphabet) - 2)])

def is_valid(string):
    seq = False
    for i in range(len(string)):
        if string[i] in ['i', 'o', 'l']:
            return False
        if string[i:i+3] in seqs:
            seq = True

    pattern = re.compile(r'(.)\1')
    matches = pattern.findall(string)
    pairs = len(matches)
    return pairs >= 2 and seq


def increment(string):
    input_list = list(string)

    input_list[-1] = chr(ord(input_list[-1]) + 1)

    for i in range(len(input_list) - 1, 0, -1):
        if input_list[i] > 'z':
            input_list[i] = 'a'
            input_list[i - 1] = chr(ord(input_list[i - 1]) + 1)

    if input_list[0] > 'z':
        input_list[0] = 'a'

    return ''.join(input_list)

pwd = 'hepxcrrq'

found_passwords = 0
valid = False
j = 0
while True:
    j += 1
    pwd = increment(pwd)
    valid = is_valid(pwd)
    if valid:
        found_passwords += 1
        print(pwd)
    if found_passwords == 2:
        break
