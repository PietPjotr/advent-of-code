import sys
sys.path.append('..')
import my_parser as p


def solve(line):
    floor = 0
    p2 = 0
    for i, char in enumerate(line):
        if char == '(':
            floor += 1

        elif char == ')':
            floor -= 1
            if floor < 0 and p2 == 0:
                p2 = i + 1

    print(floor)
    print(p2)


line = p.input_as_string('inputs/inp.txt')
solve(line)
