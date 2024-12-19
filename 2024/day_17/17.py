import sys
sys.path.append('..')
import my_parser as p
import re


# analysis of my program (and maybe similar as others idk):
# 2,4: B = A % 8          # B becomes remainder of A / 8
# 1,1: B = B XOR 1        # flips rightmost bit of B
# 7,5: C = A // 2 ** B    # C <- integer of A / 2 ** B
# 4,4: B = B XOR C        # Bi flip if Ci == Bi or Ci=1 and Bi=0
# 1,4: B = B XOR 4        # flip third bit: 0..0x00
# 0,3: A = A // 2 ** 3    # Divide A by 8
# 5,5: output B % 8       # return B % 8
# 3,0: Go again if a!=0


inp = open('inputs/inp.txt').read()
nums = [int(el) for el in re.findall(r'\d+', inp)]
registers = nums[:3]
program = nums[3:]


def get_combo(registers, arg):
    if 0 <= arg <= 3:
        combo = arg
    elif 4 <= arg <= 6:
        combo = registers[arg - 4]
    else:
        print('invalid combo')
    return combo


def run(registers, program):
    outputs = []
    program_counter = 0
    while program_counter < len(program):
        opcode = program[program_counter]
        arg = program[program_counter + 1]
        combo = get_combo(registers, arg)

        if opcode == 0:
            numerator = registers[0]
            registers[0] = numerator // 2 ** combo
        elif opcode == 1:
            registers[1] = registers[1] ^ arg
        elif opcode == 2:
            res = combo % 8
            registers[1] = combo % 8
        elif opcode == 3:
            a = registers[0]
            if a != 0:
                program_counter = combo - 2
        elif opcode == 4:
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5:
            res = combo % 8
            outputs.append(res)
        elif opcode == 6:
            numerator = registers[0]
            registers[1] = numerator // 2 ** combo
        elif opcode == 7:
            numerator = registers[0]
            registers[2] = numerator // 2 ** combo

        program_counter += 2

    return outputs


print(','.join(str(el) for el in run(registers, program)))


# realised that every index of the output of the program per index, changes
# only after an increase of 8 ** index. this can then be used to look both
# ways at every index by going 8 steps of 8 ** index in both directions. These
# the outputs of these values can then be compared to the program. If the output
# is desired, then the value will be passed on to the next iteration in bfs
# fashion. This now allows us reduce the search space significantly, and also
# ensures that we actually find the desired value. Now we brute force over
# these possibilities. Oh and we see mod 8 and // 8, so I figured out by 'hand'
# that that is the total amount of possible different values per index.
def find_a(program):
    base = 8
    index = len(program) - 1
    a = base ** index
    a_s = set([a])
    # go per index:
    for i in range(index, -1, -1):
        d = base ** i
        new_a_s = set()
        for ac in a_s:
            for j in range(-base + 1, base):
                a = ac + j * d
                if a < 0:
                    continue
                ret = run([a, 0, 0], program)
                str_ret = ''.join(str(el) for el in ret)
                str_program = ''.join(str(el) for el in program)
                if len(ret) == len(program) and str_ret[i:] == str_program[i:]:
                    new_a_s.add(a)

        a_s = new_a_s

    if a_s:
        return min(a_s)
    else:
        return None
    return min(a_s)


print(find_a(program))
