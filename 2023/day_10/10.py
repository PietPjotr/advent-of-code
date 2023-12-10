import sys
sys.path.append('..')
import my_parser as p

lines = p.input_as_lines('inputs/inp.txt')
lines = [[char for char in line] for line in lines]


def find_start(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'S':
                return (i, j)


def starting_directions(lines, start):
    i, j = start
    directions = []
    if lines[i-1][j] in ['|', '7', 'F']:
        directions.append((i-1, j))
    if lines[i+1][j] in ['|', 'L', 'J']:
        directions.append((i+1, j))
    if lines[i][j-1] in ['-', 'F', 'L']:
        directions.append((i, j-1))
    if lines[i][j+1] in ['-', '7', 'J']:
        directions.append((i, j+1))
    return directions


start = find_start(lines)
starting_dirs = starting_directions(lines, start)

distances = {}
distances[start] = 0
distances[starting_dirs[0]] = 1
distances[starting_dirs[1]] = 1

for pos in starting_dirs:
    prev_pos = start
    visited = set([start, pos])
    while True:
        i, j = pos
        char = lines[i][j]
        if char == '|':
            if prev_pos == (i-1, j):
                pos = (i+1, j)
            elif prev_pos == (i+1, j):
                pos = (i-1, j)
            else:
                raise Exception('Invalid direction')
        if char == '-':
            if prev_pos == (i, j-1):
                pos = (i, j+1)
            elif prev_pos == (i, j+1):
                pos = (i, j-1)
            else:
                raise Exception('Invalid direction')
        if char == 'F':
            if prev_pos == (i+1, j):
                pos = (i, j+1)
            elif prev_pos == (i, j+1):
                pos = (i+1, j)
            else:
                raise Exception('Invalid direction')
        if char == 'L':
            if prev_pos == (i-1, j):
                pos = (i, j+1)
            elif prev_pos == (i, j+1):
                pos = (i-1, j)
            else:
                raise Exception('Invalid direction')
        if char == 'J':
            if prev_pos == (i-1, j):
                pos = (i, j-1)
            elif prev_pos == (i, j-1):
                pos = (i-1, j)
            else:
                raise Exception('Invalid direction')
        if char == '7':
            if prev_pos == (i+1, j):
                pos = (i, j-1)
            elif prev_pos == (i, j-1):
                pos = (i+1, j)
            else:
                raise Exception('Invalid direction')
        if char == 'S':
            break

        prev_pos = (i, j)
        visited.add(pos)
        if pos in distances:
            distances[pos] = min(distances[pos], distances[prev_pos] + 1)
        else:
            distances[pos] = distances[prev_pos] + 1

max_dist = 0
for key, value in distances.items():
    if value > max_dist:
        max_dist = value

print(max_dist)
lines[start[0]][start[1]] = '|'  # change start to a pipe

loop = set(distances.keys())
inside = 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        loop_left = 0
        if (i, j) not in loop:
            for k in range(j):
                if (i, k) in loop and lines[i][k] in ['|', 'F', '7']:
                    loop_left += 1

        if loop_left % 2 == 1:
            inside += 1

print(inside)












