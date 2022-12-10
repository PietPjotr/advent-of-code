"""
Autor: Pjotr Piet
Date: 2018-12-09

Usage: for the testing of the porgram I wrote some print functions, these functions can be turned on by setting verbose
to True In both part 1 and 2 respectively. This displays the grid and the coordinates of the head and tail of the rope.
NOTE: I do recommend using verbose only on smaller inputs.
"""
import parser

# Global variables used for the visual representation of the grid of part 1
N = 6
x_offset = 0
y_offset = 0

# Global variables used for the visual representation of the grid of part 2
N = 27
x_offset = 12
y_offset = 6

"""Prints the grid with the current positions of all the knots of the rope."""
def print_grid(positions, visited):
    grid = [['.' for i in range(N)] for j in range(N)]
    xH, yH = positions[0]
    grid[yH + y_offset][xH + x_offset] = 'H'

    for i in range(1, len(positions)):
        xT, yT = positions[i]
        if grid[yT + y_offset][xT + x_offset] == '.':
            grid[yT + y_offset][xT + x_offset] = str(i)

    for row in grid[::-1]:
        print(''.join(row))

    print('')

"""Prints the grid with all the visited positions of the tail of the rope"""
def print_visited(visited):
    grid = [['.' for i in range(N)] for j in range(N)]
    for x, y in visited:
        grid[y + y_offset][x + x_offset] = '#'
    grid[0 + y_offset][0 + x_offset] = 's'
    for row in grid[::-1]:
        print(''.join(row))


"""Makes the tail follow the head and returns the new visited coordinates and the new coordinates of the tail."""
def follow(positions, visited):
    adjacent = False

    for i in range(0, len(positions) - 1):
        xH, yH = positions[i]
        xT, yT = positions[i + 1]

        for j in range(-1, 2):
            for k in range(-1, 2):
                if xT + j == xH and yT + k == yH:
                    adjacent = True

        if adjacent:
            continue

        else:
            dY = yH - yT
            dX = xH - xT
            if dY != 0:
                yT += dY // abs(dY)
            if dX != 0:
                xT += dX // abs(dX)

            positions[i + 1] = [xT, yT]

    visited.add(tuple(positions[-1]))
    return positions, visited



"""Moves the rope one position based on the direction of dir. Returns the new positions and the visited coordinates."""
def move_head(positions, visited, dir):
    if dir == 'U':
        positions[0][1] += 1
    elif dir == 'D':
        positions[0][1] -= 1
    elif dir == 'R':
        positions[0][0] += 1
    elif dir == 'L':
        positions[0][0] -= 1

    positions, visited = follow(positions, visited)

    return positions, visited


def deel1(lines, verbose=False):
    knots = 2
    visited = set()
    positions = [[0, 0] for _ in range(knots)]
    visited.add((positions[-1][0], positions[-1][1]))

    verbose = False
    for move in lines:
        [dir, steps] = move.split(' ')
        for i in range(int(steps)):
            positions, visited = move_head(positions, visited, dir)

        if verbose:
            print(positions, visited, dir)
            print_grid(positions, visited)

    # print_visited(visited)
    print(len(visited))

def deel2(lines, verbose=False):
    knots = 10
    visited = set()
    positions = [[0, 0] for _ in range(knots)]
    visited.add((positions[-1][0], positions[-1][1]))

    verbose = False
    for move in lines:
        [dir, steps] = move.split(' ')
        for i in range(int(steps)):
            positions, visited = move_head(positions, visited, dir)

        if verbose:
            print(positions, visited, dir)
            print_grid(positions, visited)

    # print_visited(visited)
    print(len(visited))


def main():
    lines = parser.input_as_lines('inputs/dag9.txt')
    # lines = parser.input_as_lines('inputs/dag9_test.txt')
    verbose = False
    deel1(lines, verbose)
    deel2(lines, verbose)



if __name__ == "__main__":
    main()