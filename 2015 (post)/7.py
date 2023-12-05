# voor een of andere reden werkt dit nog niet zopals ik wil maar misschien ligt
# het aan het feit dat de lines die geen waardes hebben ook al nodig zzijn om
# nieuwe waardes te vinden.

import parser
import numpy as np


def deel1(lines):
    wires = {}
    commands = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']

    for line in lines:
        if line[0].isdigit() and len(line) == 3:
            wires[line[-1]] = int(line[0])

    # print(wires)
    iterations = 1
    for i in range(iterations):
        for line in lines:
            cur_command = ''
            res = ''
            if line[-1] in wires.keys():
                continue
            for command in commands:
                if command in line:
                    cur_command = command

                if cur_command == 'AND' and line[0] in wires and line[2] in wires:
                    res = np.uint16(wires[line[0]]) & np.uint16(wires[line[2]])
                    # print(line)

                elif cur_command == 'OR' and line[0] in wires and line[2] in wires:
                    res = np.uint16(wires[line[0]]) | np.uint16(wires[line[2]])
                    # print(line)

                elif cur_command == 'LSHIFT' and line[0] in wires:
                    print(line)
                    res = np.uint16(wires[line[0]]) << int(line[2])
                    # print(res, line)

                elif cur_command == 'RSHIFT' and line[0] in wires:
                    res = np.uint16(wires[line[0]]) >> int(line[2])
                    # print(line)

                elif cur_command == 'NOT' and line[1] in wires:
                    res = ~ np.uint16(wires[line[1]])
                    # print(line)

                # else:
                    # print("one of the two wires has no value yet", line)
                if res != '':
                    print("new wire found:", line)
                    wires[line[-1]] = res

    # lx -> a
    # lw and lv ->lx
    # lc LSHIFT 1 -> lw
    # lb OR la -> lc
    # kh LSHIFT 1 -> lb
    # kg OR kf -> kh

    print(len(wires))
    print(wires)


def deel2(lines):
    pass


def main():
    # lines = parser.input_as_string('inputs/7.txt')
    lines = parser.input_as_lines('inputs/7.txt')
    # lines = parser.input_as_ints('inputs/7.txt')
    # lines = parser.input_as_grid('inputs/7.txt')
    lines_c = []
    for line in lines:
        lines_c.append(line.split(' '))
    lines = lines_c
    # print(lines)
    deel1(lines)


if __name__ == "__main__":
    main()
