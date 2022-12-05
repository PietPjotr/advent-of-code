import parser
import copy


def print_grid(lines):
    for line in lines:
        new = ''
        for char in line:
            new += char

        print(new)
    print('')


SOUTH = 'v'
EAST = '>'
def main():
    lines = parser.input_as_lines('inputs/dag25.txt')

    board = []
    for line in lines:
        row = [char for char in line]
        board.append(row)


    i = 0
    while True:
        moved1 = True
        (board, moved) = move(board)
        i += 1
        if not moved:
            break

    print("stopped at iteration: {}".format(i))


def move(grid):
    x_max = len(grid[0])
    y_max = len(grid)
    moved = False

    temp = copy.deepcopy(grid)

    # Firstly all the east facing cucumbers move
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == EAST:
                if row[(j + 1) % x_max] == '.':
                    temp[i][(j + 1) % x_max] = char
                    temp[i][j] = '.'
                    moved = True

    ret = copy.deepcopy(temp)

    # Secondly all the south facing cucumbers move
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == SOUTH:
                if temp[(i + 1) % y_max][j] == '.':
                    ret[(i + 1) % y_max][j] = char
                    ret[i][j] = '.'
                    moved = True

    return (ret, moved)


if __name__ == "__main__":
    main()
