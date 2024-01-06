import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')


def ABBA(string):
    for i in range(len(string) - 3):
        window = string[i:i+4]
        if window[0] == window[-1] and window[0] != window[1] and window[1] == window[2]:
            return True
    return False


def ABA(string):
    abas = []
    for i in range(len(string) - 2):
        window = string[i:i+3]
        # print('window', window)
        if window[0] == window[2]:
            abas.append(window)
    return abas


def BAB(string, aba):
    abas = []
    for i in range(len(string) - 2):
        window = string[i:i+3]
        if aba[1] == window[0] and aba[1] == window[2] and aba[0] == window[1]:
            return True
    return False


p1 = 0
p2 = 0
for line in L[:]:
    nex = False
    found2 = False
    inside = re.findall(r'\[([a-z]+)\]', line)
    outside = re.findall(r'(?:^|\])([a-z]+)(?:$|\[)', line)

    abass = []
    for match in outside:
        abas = ABA(match)
        abass.extend(abas)

    for match in inside:
        if ABBA(match):
            nex = True
        if not found2:
            for aba in abass:
                if BAB(match, aba):
                    p2 += 1
                    found2 = True
                    break

    if not nex:
        for match in outside:
            if ABBA(match):
                p1 += 1
                break

print(p1)
print(p2)
