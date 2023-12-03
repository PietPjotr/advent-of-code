import sys
sys.path.append('..')
import my_parser as p
import re


def valid_num(num, lines, i):
    start = num.start()
    end = num.end()
    # loop over all indices of the number
    for j in range(start, end):
        # check all around the index in x range
        for x in range(j-1, j+2):
            # check if index is in range
            if x < len(lines[i]) and x >= 0:
                # loop over all indices in the y range
                for y in range(i-1, i+2):
                    if y < len(lines) and y >= 0:
                        if not lines[y][x].isdigit() and lines[y][x] != '.':
                            return True


def part1():
    lines = p.input_as_lines('inputs/inp.txt')
    nums = []
    for i, line in enumerate(lines):
        # find all the nums per line with the corresponding indices
        line = re.finditer(r'\d+', line)

        for num in line:
            if valid_num(num, lines, i):
                nums.append(int(num.group()))

    print(nums)
    print(sum(nums))

def part2():
    lines = p.input_as_lines('inputs/inp.txt')
    gears = {}

    # loop over all lines
    for i, line in enumerate(lines):
        # find all the numbers + indices
        line = re.finditer(r'\d+', line)

        # loop over all the nums and if it finds a gear to be adjacent
        # it ads the gear to the dict with the corresponding number
        for num in line:
            start = num.start()
            end = num.end()
            # loop over all indices of the number
            for j in range(start, end):
                # check all around the index in x range
                for x in range(j-1, j+2):
                    # check if index is in range
                    if x < len(lines[i]) and x >= 0:
                        # loop over all indices in the y range
                        for y in range(i-1, i+2):
                            if y < len(lines) and y >= 0:
                                # we find a gear and want to add this number to it
                                # in the dict
                                if lines[y][x] == '*':
                                    if (y, x) in gears:
                                        gears[(y, x)].append(int(num.group()))
                                    else:
                                        gears[(y, x)] = [int(num.group())]


    gearvalues = []
    for gear in gears:
        # assuming that no gear has the same number twice (also fixes the
        # problem that one number can be adjacent to the same gear twice
        # with this solution)
        nums = list(set(gears[gear]))
        if len(nums) == 2:
            gearvalues.append(nums[0] * nums[1])

    print(sum(gearvalues))


part1()
part2()








