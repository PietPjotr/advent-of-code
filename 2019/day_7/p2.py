import sys
sys.path.append('..')
import my_parser as p

from itertools import permutations
import multiprocessing

# Read the input
L = p.input_as_lines('inputs/inp.txt')
instructions = L[0].split(',')
og_instructions = [int(el) for el in instructions]


def run(queue_out, queue_in, MAX):
    inp_count = 0
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
            value = queue_in.get()
            instructions[one] = value
            pos += 2
        elif opcode == 4:
            one = instructions[pos + 1]
            value = instructions[one]
            out = value
            if out > MAX.value:
                MAX.value = out
            queue_out.put(out)
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
            return out
        else:
            print('invalid instruction:', opcode)
            break


def process_handler(queue_in, queue_out, MAX):
    run(queue_out, queue_in, MAX)


def solve2():
    manager = multiprocessing.Manager()  # Create a manager to share data
    MAX = manager.Value('i', -float('inf'))  # Shared value for MAX, initialized to negative infinity

    for setting in permutations('56789', 5):
        setting = [int(el) for el in setting]
        queues = [multiprocessing.Queue() for _ in range(5)]
        for i, q in enumerate(queues):
            q.put(setting[i])

        # Set initial input value for p1
        queues[0].put(0)  # p1 starts with 0

        processes = []
        for i in range(5):
            next_idx = (i + 1) % 5  # cyclic link: p5 -> p1
            p = multiprocessing.Process(target=process_handler, args=(queues[i], queues[next_idx], MAX))
            processes.append(p)
            p.start()

        # Wait for all processes to finish
        for p in processes:
            p.join()

    print(MAX.value)

solve2()
