import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

lines = p.input_as_lines('inputs/inp.txt')
lines = [[char for char in row] for row in lines]

def tilt_north(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            el = lines[i][j]
            if el == 'O':
                toti = i - 1
                while toti >= 0 and lines[toti][j] == '.':
                    lines[toti][j] = 'O'
                    lines[toti + 1][j] = '.'
                    toti -= 1

    return lines


def tilt_west(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            el = lines[i][j]
            if el == 'O':
                totj = j - 1
                while totj >= 0 and lines[i][totj] == '.':
                    lines[i][totj] = 'O'
                    lines[i][totj + 1] = '.'
                    totj -= 1

    return lines


def tilt_south(lines):
    R = len(lines)
    C = len(lines[0])
    for r in range(R-1, -1, -1):
        for c in range(C):
            el = lines[r][c]
            if el == 'O':
                totr = r + 1
                while totr < R and lines[totr][c] == '.':
                    lines[totr][c] = 'O'
                    lines[totr-1][c] = '.'
                    totr += 1
    return lines


def tilt_east(lines):
    R = len(lines)
    C = len(lines[0])
    for r in range(R):
        for c in range(C-1, -1, -1):
            el = lines[r][c]
            if el == 'O':
                totc = c + 1
                while totc < C and lines[r][totc] == '.':
                    lines[r][totc] = 'O'
                    lines[r][totc-1] = '.'
                    totc += 1
    return lines


def state_equal(lines1, lines2):
    for i in range(len(lines1)):
        for j in range(len(lines1[0])):
            if lines1[i][j] != lines2[i][j]:
                return False
    return True


def get_states(lines):
    start_state = deepcopy(lines)
    all_states = [start_state]
    tilts = 0

    for cycle in range(1, 120):
        dirs = ['north', 'west', 'south', 'east']
        for dir in dirs:
            if dir == 'north':
                lines = tilt_north(lines)
            if dir == 'west':
                lines = tilt_west(lines)
            if dir == 'south':
                lines = tilt_south(lines)
            if dir == 'east':
                lines = tilt_east(lines)
            tilts += 1

        all_states.append(deepcopy(lines))

    return all_states


def find_cycle(all_states):
    reti, retj =  0, 0
    for i in range(len(all_states)):
        si = all_states[i]
        for j in range(i + 1, len(all_states)):
            sj = all_states[j]
            if state_equal(si, sj):
                reti, retj = i, j
                break
    return reti, retj


def get_final_state(all_states):
    start_cycle, end_cycle = find_cycle(all_states)
    delta = end_cycle - start_cycle
    tot_cycles = 1000000000

    final_state_i = start_cycle + ((tot_cycles-start_cycle) % delta)

    final_state = all_states[final_state_i]
    return final_state


def get_score(lines):
    res = 0
    R = len(lines)
    C = len(lines[0])
    for r in range(R):
        for c in range(C):
            if lines[r][c] == 'O':
                res += R - r

    return res


def part1():
    lines = p.input_as_lines('inputs/inp.txt')
    lines = [[char for char in row] for row in lines]

    lines = tilt_north(lines)
    res = get_score(lines)
    print(res)


def part2():
    lines = p.input_as_lines('inputs/inp.txt')
    lines = [[char for char in row] for row in lines]

    states = get_states(lines)
    lines = get_final_state(states)
    res = get_score(lines)
    print(res)


part1()
part2()



