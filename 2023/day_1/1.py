import sys
sys.path.append('..')
import my_parser as p
import re

lines = p.input_as_lines('inputs/inp.txt')

def part1():
    nums = []
    for line in lines:
        for i, c in enumerate(line):
            if c.isdigit():
                first = int(c)
                break
        for i, c in enumerate(line[::-1]):
            if c.isdigit():
                last = int(c)
                break

        num = str(first) + str(last)
        nums.append(int(num))

    print(sum(nums))


def part2():

    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    nums = []
    for line in lines:

        i1 = float('inf')
        i2 = 0

        for i, c in enumerate(line):
            if c.isdigit():
                first = int(c)
                i1 = i
                break
        for i, c in enumerate(line):
            if c.isdigit():
                last = int(c)
                i2 = i

        for digit in digits:
            if line.find(digit) != -1:
                if line.find(digit) < i1:
                    first = digits.index(digit) + 1
                    i1 = line.find(digit)

        for digit in digits:
            res = [i.start() for i in re.finditer(digit, line)]
            if res:
                if res[-1] > i2:
                    last = digits.index(digit) + 1
                    i2 = res[-1]


        num = str(first) + str(last)
        nums.append(int(num))

    print(sum(nums))

part1()
part2()