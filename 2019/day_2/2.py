import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

instructions = L[0].split(',')
og_instructions = [int(el) for el in instructions]

part_one = 0
part_two = 0

for i in range(0, 100):
    for j in range(0, 100):
        instructions = og_instructions.copy()
        instructions[1] = i
        instructions[2] = j

        pos = 0
        while True:
            opcode = instructions[pos]
            one = instructions[pos + 1]
            two = instructions[pos + 2]
            three = instructions[pos + 3]

            if opcode == 1:
                value = instructions[one] + instructions[two]
                instructions[three] = value
            elif opcode == 2:
                value = instructions[one] * instructions[two]
                instructions[three] = value
            else:
                break

            pos += 4

        if instructions[0] == 19690720:
            part_two = 100 * i + j

        if i == 12 and j == 2:
            part_one = instructions[0]

print(part_one)
print(part_two)