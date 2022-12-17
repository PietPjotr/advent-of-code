import parser
def max_right(rock):
    return max([x for x, y in rock])
def max_left(rock):
    return min([x for x, y in rock])

def min_y(rock):
    return min([y for x, y in rock])

def bottom_row(rock):
    minimal_y = min_y(rock)
    return [(x, y) for x, y in rock if y == minimal_y]

def rock_len(rock):
    ys = set([y for x, y in rock])
    return len(ys)

def drop_rock(line, i, rock, tunnel, stack_height, rock_number=0):
    rock = [(x + 2, y + stack_height + 4) for x, y in rock]
    drops = 0
    while True:
        instruction = line[i % len(line)]

        if instruction == '>':
            if max_right(rock) + 1 < 7:
                test = [(x + 1, y) for x, y in rock]
                if all([(x, y) not in tunnel for x, y in test]):
                    rock = test
        elif instruction == '<':
            if max_left(rock) - 1 > -1:
                test = [(x - 1, y) for x, y in rock]
                if all([(x, y) not in tunnel for x, y in test]) or len(tunnel) == 0:
                    rock = test

        test = [(x, y - 1) for x, y in rock]
        if all([(x, y) not in tunnel for x, y in test]) and min_y(rock) > 0:
            rock = test
            drops += 1
        else:
            i += 1
            break
        i += 1

    tunnel = tunnel.union(rock)
    stack_height = max(stack_height + rock_len(rock) + 3 - drops, stack_height)
    return tunnel, i % len(line), stack_height

def print_tunnel(tunnel):
    tunnel = sorted(list(tunnel), key=lambda x: x[1])
    y_max = tunnel[-1][1]
    result = []
    for i in range(y_max + 1):
        row = ''
        for j in range(7):
            if (j, i) in tunnel:
                row += '#'
            else:
                row += '.'
        result.append(row)
    print('\n'.join(result[::-1]))

def main():
    lines = parser.input_as_lines('inputs/dag17.txt')
    # lines = parser.input_as_lines('inputs/dag17_test.txt')
    line = lines[0]

    # rocks defined by (x, y) starting from the bottom left
    rock1 = [(0, 0), (1, 0), (2, 0), (3, 0)]
    rock2 = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
    rock3 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    rock4 = [(0, 0), (0, 1), (0, 2), (0, 3)]
    rock5 = [(0, 0), (1, 0), (0, 1), (1, 1)]

    rocks = [rock1, rock2, rock3, rock4, rock5]
    height = -1
    tunnel = set()
    j = 0
    for i in range(2022):
        rock = rocks[i % 5]
        tunnel, j, height = drop_rock(line, j, rock, tunnel, height, i)
    part1 = height + 1

    # loop to start identifying the cycle
    tunnel = set()
    height = -1
    j = 0
    states = []
    rock_drops = 2160
    for i in range(rock_drops):
        rock = rocks[i % 5]
        tunnel, j, height = drop_rock(line, j, rock, tunnel, height, i)
        states.append((i % 5, j, height))

    # used to find the cycle in the states (find a number for rock_drops where the cycle starts and manually copy the
    # start and end index in the start cycle and end cycle variables)
    for i in range(len(states)):
        for j in range(i + 1, len(states)):
            if states[i][0:-1] == states[j][0:-1]:
                print(i, j)


    # using the cycle to find the length of many many more iterations
    start_cycle = 389
    end_cycle = 2114

    cycle_length = end_cycle - start_cycle
    cycle_height = states[end_cycle][2] - states[start_cycle][2]
    start_height = states[start_cycle][2]

    iterations = 1000000000000
    cycles = (iterations - start_cycle) // cycle_length
    rest = iterations % cycle_length
    rest_height = states[rest][2] - states[start_cycle][2]
    final_height = cycles * cycle_height + rest_height + start_height

    print("part1: ", part1)
    print("part2: ", final_height)


if __name__ == "__main__":
    main()