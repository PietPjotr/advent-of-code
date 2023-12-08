# voor een of andere reden werkt dit nog niet zopals ik wil maar misschien ligt
# het aan het feit dat de lines die geen waardes hebben ook al nodig zzijn om
# nieuwe waardes te vinden.

import parser
import numpy as np
import re

def deel1(commands, all_args):
    wires = {}

    iterations = 1000
    for i in range(iterations):
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

                print("initiated wire: ", args)

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
                print(command, args)
                res = np.uint16(wires[args[0]]) >> int(args[1])
                print(args)

            elif command == 'NOT' and args[0] in wires:
                res = ~ np.uint16(wires[args[0]])

            if res != '':
                print("new wire found:", args)
                wires[args[-1]] = res

    print(len(wires))
    print(wires)


def main():
    lines = parser.input_as_lines('inputs/7.txt')
    commands = []
    all_args = []
    for args in lines:
        command = re.findall('[A-Z]+', args)
        arg = re.findall('[a-z0-9]+', args)
        if not command:
            command = ''
        else:
            command = command[0]

        commands.append(command)
        all_args.append(arg)

    deel1(commands, all_args)


if __name__ == "__main__":
    main()
