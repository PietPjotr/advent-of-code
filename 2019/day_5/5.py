import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

instructions = L[0].split(',')
og_instructions = [int(el) for el in instructions]

for inp in [1, 5]:
    instructions = og_instructions.copy()
    out = -1
    pos = 0
    while True:
        modi = str(instructions[pos])
        modi = (5 - len(modi)) * '0' + modi
        opcode = int(modi[-2:])
        rest = list(map(int, modi[0:-2][::-1]))

        if opcode == 1 or opcode == 2:
            one = instructions[pos + 1]
            two = instructions[pos + 2]
            three = instructions[pos + 3]

            v1 = instructions[one] if rest[0] == 0 else one
            v2 = instructions[two] if rest[1] == 0 else two

            if opcode == 1:
                value = v1 + v2
            if opcode == 2:
                value = v1 * v2
            instructions[three] = value
            pos += 4
        elif opcode == 3:
            one = instructions[pos + 1]
            value = inp  # different inputs for p1 and p2
            instructions[one] = value
            pos += 2
        elif opcode == 4:
            one = instructions[pos + 1]
            value = instructions[one]
            out = value
            pos += 2
        elif opcode == 5:
            one = instructions[pos + 1]
            two = instructions[pos + 2]

            v1 = instructions[one] if rest[0] == 0 else one
            v2 = instructions[two] if rest[1] == 0 else two
            if v1 != 0:
                pos = v2
            else:
                pos += 3
        elif opcode == 6:
            one = instructions[pos + 1]
            two = instructions[pos + 2]

            v1 = instructions[one] if rest[0] == 0 else one
            v2 = instructions[two] if rest[1] == 0 else two

            if v1 == 0:
                pos = v2
            else:
                pos += 3
        elif opcode == 7:
            one = instructions[pos + 1]
            two = instructions[pos + 2]
            three = instructions[pos + 3]

            v1 = instructions[one] if rest[0] == 0 else one
            v2 = instructions[two] if rest[1] == 0 else two

            if v1 < v2:
                instructions[three] = 1
            else:
                instructions[three] = 0

            pos += 4
        elif opcode == 8:
            one = instructions[pos + 1]
            two = instructions[pos + 2]
            three = instructions[pos + 3]

            v1 = instructions[one] if rest[0] == 0 else one
            v2 = instructions[two] if rest[1] == 0 else two

            if v1 == v2:
                instructions[three] = 1
            else:
                instructions[three] = 0

            pos += 4
        elif opcode == 99:
            print(out)
            break
        else:
            print('invalid instruction:', opcode)
            break
