import sys
sys.path.append('..')
import my_parser as p
import numpy as np
import re


L = p.input_as_lines('inputs/inp.txt')


def solve(commands, all_args, part=1):
    wires = {}
    part2 = False

    while 'a' not in wires:
        for command, args in zip(commands, all_args):

            res = ''
            # if we already know the value we go next
            if args[-1] in wires.keys():
                continue

            if command == '':

                if args[0] in wires:
                    res = wires[args[0]]
                elif args[0].isdigit():
                    res = int(args[0])
                else:
                    continue

                # set the value of b to the value of a for the first part
                if part != 1 and args[-1] == 'b' and not part2:
                    res = part
                    part2 = True

            if command == 'AND':
                if args[0] in wires and args[1] in wires:
                    res = np.uint16(wires[args[0]]) & np.uint16(wires[args[1]])
                elif args[0].isdigit() and args[1] in wires:
                    res = np.uint16(args[0]) & np.uint16(wires[args[1]])
                elif args[1].isdigit() and args[0] in wires:
                    res = np.uint16(wires[args[0]]) & np.uint16(args[1])
                elif args[0].isdigit() and args[1].isdigit():
                    res = np.uint16(args[0]) & np.uint16(args[1])
                else:
                    continue

            elif command == 'OR' and args[0] in wires and args[1] in wires:
                res = np.uint16(wires[args[0]]) | np.uint16(wires[args[1]])
            elif command == 'LSHIFT' and args[0] in wires:
                res = np.uint16(wires[args[0]]) << int(args[1])
            elif command == 'RSHIFT' and args[0] in wires:
                res = np.uint16(wires[args[0]]) >> int(args[1])
            elif command == 'NOT' and args[0] in wires:
                res = ~ np.uint16(wires[args[0]])

            if res != '':
                wires[args[-1]] = res

    print(wires['a'])
    return wires['a']


commands = []
all_args = []
for args in L:
    command = re.findall('[A-Z]+', args)
    arg = re.findall('[a-z0-9]+', args)
    if not command:
        command = ''
    else:
        command = command[0]

    commands.append(command)
    all_args.append(arg)


p1 = solve(commands, all_args)
p2 = solve(commands, all_args, p1)
