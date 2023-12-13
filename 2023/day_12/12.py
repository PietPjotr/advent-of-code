import sys
sys.path.append('..')
import my_parser as p
import re


def all_matches(string, d):
    matches = []
    i = 0
    while i < len(string):
        cur = string[i]
        if cur == '#' or cur == '?':
            match = re.match(r'^[#?]{%d}([?.]|$)' % d, string[i:])
            if match:
                start, end = match.span()
                matches.append((i + start, i + end))
        i += 1
        if string[i-1] == '#':
            break

    return matches


def find_arrangements(spring, ds):
    no_arrangements = 0
    stack = {(spring, *ds): 1}
    d = 0
    rests = {}
    while stack:
        cur = list(stack.keys())[0]
        i = stack.pop(cur)
        spring, ds = cur[0], list(cur[1:])
        if len(ds) == 0:
            if '#' in spring:
                continue
            no_arrangements += i
            continue

        for start, end in all_matches(spring, ds[0]):
            next_spring = spring[end:]
            next_ds = ds[1:]
            if len(next_spring) < sum(next_ds) - len(next_ds):
                d += 1
                break
            if (next_spring, *next_ds) in stack:
                stack[(next_spring, *next_ds)] += i
            else:
                stack[(next_spring, *next_ds)] = i

    return no_arrangements


def get_lines():
    lines = p.input_as_lines('inputs/inp.txt')
    springs2 = []
    dss2 = []
    for line in lines:
        spring, ds = line.split()
        spring = (spring + '?') * 4 + spring
        ds = (ds + ',') * 4 + ds
        ds = [int(el) for el in ds.split(',')]

        springs2.append(spring)
        dss2.append(ds)

    return springs2, dss2


def part1():
    res = 0
    lines = p.input_as_lines('inputs/inp.txt')
    for line in lines:
        spring, ds = line.split()
        ds = [int(el) for el in ds.split(',')]
        num = find_arrangements(spring, ds)
        res += num

    print(res)


def part2():
    res = 0
    lines = p.input_as_lines('inputs/inp.txt')
    for i, line in enumerate(lines):
        spring, ds = line.split()
        spring = '?'.join([spring] * 5)
        ds = [int(el) for el in ','.join([ds] * 5).split(',')]
        num = find_arrangements(spring, ds)
        res += num

    print(res)


part1()
part2()
