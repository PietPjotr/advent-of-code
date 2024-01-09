import sys
sys.path.append('..')
import my_parser as p

num = int(p.input_as_lines('inputs/inp.txt')[0])


def p1(num):
    elves = [i for i in range(1, num + 1)]
    while len(elves) > 1:
        new_elves = []
        for i in range(0, len(elves), 2):
            new_elves.append(elves[i])

        if len(elves) > 2 and len(elves) % 2 == 1:
            new_elves.pop(0)
        elves = new_elves

    print(elves[0])


def p2(num):
    i = 1

    while i * 3 < num:
        i *= 3

    print(num - i)


p1(num)
p2(num)
