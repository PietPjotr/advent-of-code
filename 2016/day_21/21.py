import sys
sys.path.append('..')
import my_parser as p
from itertools import permutations

L = p.input_as_lines('inputs/inp.txt')


def rotate_right(string, swaps):
    return string[-swaps:] + string[:-swaps]


def solve(part=1):
    if part == 1:
        inputs = ['abcdefgh']
    else:
        inputs = permutations(list('abcdefgh'))
    for inp in inputs:
        inp = list(inp)
        unscrambled = [el for el in inp]
        for line in L:
            line = line.split()
            command = line[0]
            if command == 'swap':
                if line[1] == 'position':
                    i = int(line[2])
                    j = int(line[-1])
                    temp = inp[i]
                    inp[i] = inp[j]
                    inp[j] = temp
                elif line[1] == 'letter':
                    letter1 = line[2]
                    letter2 = line[-1]
                    i = inp.index(letter1)
                    j = inp.index(letter2)
                    inp[i] = letter2
                    inp[j] = letter1
            elif command == 'rotate':
                if line[1] == 'left':
                    steps = int(line[2])
                    inp = inp[steps:] + inp[:steps]
                elif line[1] == 'right':
                    steps = int(line[2])
                    inp = rotate_right(inp, steps)
                elif line[1] == 'based':
                    letter = line[-1]
                    i = inp.index(letter)
                    inp = rotate_right(inp, 1)
                    inp = rotate_right(inp, i)
                    if i >= 4:
                        inp = rotate_right(inp, 1)
            elif command == 'reverse':
                start = int(line[2])
                end = int(line[-1])
                to_reverse = inp[start:end + 1]
                inp = inp[:start] + to_reverse[::-1] + inp[end+1:]
            elif command == 'move':
                i = int(line[2])
                j = int(line[-1])
                el = inp[i]
                inp.remove(el)
                inp = inp[:j] + [el] + inp[j:]


        res = ''.join(inp)
        if part == 2 and res == 'fbgdceah':
            print(''.join(unscrambled))
            break
        if part == 1:
            print(res)

solve(1)
solve(2)