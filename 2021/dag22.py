import parser
import re
import numpy as np


def deel1(lines):
    pass


def deel2(lines):
    pass


def turn_on(coords, space, on):
    og_coords = coords
    # print("og coords: ", coords)
    # to account for the fact that the positions are between -50 - 50
    coords = list(map(lambda x: x + 50, coords))
    # print("mapped coords: ", coords)
    truth = list(map(lambda x: True if x <= 100 and x >= 0 else False, coords))
    # print(truth, coords, all(truth))
    if all(truth):
        s_x = coords[0] if coords[0] < coords[1] else coords[1]
        s_y = coords[2] if coords[2] < coords[3] else coords[3]
        s_z = coords[4] if coords[4] < coords[5] else coords[5]

        dx = abs(coords[0] - coords[1])
        dy = abs(coords[2] - coords[3])
        dz = abs(coords[4] - coords[5])

        for x in range(s_x, s_x + dx + 1):
            for y in range(s_y, s_y + dy + 1):
                for z in range(s_z, s_z + dz + 1):
                    try:
                        if space[x][y][z] == 0:
                            space[x][y][z] = 1
                            on += 1
                    except:
                        print(x - 50, y - 50, z - 50)


    return space, on


def turn_off(coords, space, on):
    coords = list(map(lambda x: x + 50, coords))
    truth = list(map(lambda x: True if x <= 100 and x >= 0 else False, coords))
    if all(truth):
        s_x = coords[0] if coords[0] < coords[1] else coords[1]
        s_y = coords[2] if coords[2] < coords[3] else coords[3]
        s_z = coords[4] if coords[4] < coords[5] else coords[5]

        dx = abs(coords[0] - coords[1])
        dy = abs(coords[2] - coords[3])
        dz = abs(coords[4] - coords[5])

        for x in range(s_x, s_x + dx + 1):
            for y in range(s_y, s_y + dy + 1):
                for z in range(s_z, s_z + dz + 1):
                    if space[x][y][z] == 1:
                        space[x][y][z] = 0
                        on -= 1
    return space, on


def main():
    lines = parser.input_as_lines('inputs/dag22.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    space = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    on = 0

    for line in lines:
        coords = []
        for el in line:
            coords = list(map(int, re.findall(r'-?\d+', line)))
        if line.split()[0] == 'on':
            space, on = turn_on(coords, space, on)
        else:
            space, on = turn_off(coords, space, on)

    print(on)

if __name__ == "__main__":
    main()
