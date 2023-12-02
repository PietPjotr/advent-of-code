import sys
sys.path.append('..')
import my_parser as p
import re

def part1():
    lines = p.input_as_lines('inputs/inp.txt')

    possibe = []
    for i, line in enumerate(lines):
        blue = 0
        red = 0
        green = 0

        # take only the line after the colon.
        line = line[line.find(':') + 2:]

        # split the lines on color and number of occurances only
        line = re.findall(r'[a-z0-9]+', line)

        j = 1
        pos = True

        while j < len(line):
            color = line[j]
            if color == 'red' and int(line[j - 1]) > 12:
                pos = False
                break
            if color == 'green' and int(line[j - 1]) > 13:
                pos = False
                break
            if color == 'blue' and int(line[j - 1]) > 14:
                pos = False
                break
            j += 2

        if pos:
            possibe.append(i + 1)

    print(sum(possibe))


def part2():
    lines = p.input_as_lines('inputs/inp.txt')

    powers = []
    for i, line in enumerate(lines):

        line = line[line.find(':') + 2:]

        # split the lines on color and number of occurances only
        line = re.findall(r'[a-z0-9]+', line)

        mingreen = 0
        minred = 0
        minblue = 0

        for j in range(1, len(line), 2):
            color = line[j]
            if color == 'red':
                if int(line[j - 1]) > minred:
                    minred = int(line[j - 1])
            if color == 'green':
                if int(line[j - 1]) > mingreen:
                    mingreen = int(line[j - 1])
            if color == 'blue':
                if int(line[j - 1]) > minblue:
                    minblue = int(line[j - 1])

        power = minred * mingreen * minblue
        powers.append(power)

    print(sum(powers))

part1()
part2()