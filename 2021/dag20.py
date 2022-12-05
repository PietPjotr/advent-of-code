import parser
import copy


def find_neighs(grid, x, y):
    i_lim = len(grid) - 1
    j_lim = len(grid[0]) - 1

    neighs = [grid[i][j] for i in range(x-1, x+2)
              for j in range(y-1, y+2)
              if i >= 0 and i <= i_lim and j >= 0 and j <= j_lim]

    return neighs


def im_to_bin(grid):
    binary = ''
    for line in grid:
        for el in line:
            if el == '.':
                binary += '0'
            else:
                binary += '1'

    return int(binary, 2)


def pad(grid, header, iteration):
    new = []
    pad = 2
    if header[0] == '#':
        if iteration % 2 == 0:
            s = header[-1]
        else:
            s = header[0]
    else:
        s = '.'

    for _ in range(pad):
        new.append((len(grid) + 2 * pad) * s)

    for line in grid:
        new.append(pad*s + line + pad*s)

    for _ in range(pad):
        new.append((len(grid) + 2 * pad) * s)

    return new


def cache_pad(grid, header, iteration):
    new = []
    pad = 2
    if header[0] == '#':
        if iteration % 2 == 0:
            s = header[-1]
            inner = header[0]
        else:
            s = header[0]
            inner = header[-1]
    else:
        s = '.'

    inner

    new.append((len(grid) + 2 * pad) * s)

    for _ in range(pad-1):
        new.append(s + (len(grid)+pad)*inner + s)
    for line in grid:
        new.append(s+(pad-1)*inner + line + (pad-1)*inner + s)
    for _ in range(pad-1):
        new.append(s + (len(grid)+pad)*inner + s)

    new.append((len(grid) + 2 * pad) * s)

    return new

def unpad(grid, size):
    new = []
    or_size = len(grid)
    pad = int((or_size - size) / 2)

    for line in grid[pad:or_size - pad]:
        new.append(line[pad:or_size - pad])

    return new


def enhance(grid, mapping, iteration):
    grid = cache_pad(grid, mapping, iteration)
    new = []
    length = len(grid)

    for i in range(length):
        line = ''

        for j in range(length):
            area = find_neighs(grid, i, j)
            convert_num = im_to_bin(area)
            line += mapping[convert_num]

        new.append(line)

    return new


def light(grid):
    light = 0
    for line in grid:
        for el in line:
            if el == '#':
                light += 1
    print(light)


def main():
    lines = parser.input_as_lines('inputs/dag20.txt')
    header = lines[0]
    grid = lines[2:]
    og_size = len(grid)

    padded = cache_pad(grid, header, 1)

    # for line in padded:
    #     print(line)


    its = 50
    for i in range(its):
        grid = enhance(grid, header, i)

    end = unpad(grid, og_size + its * 2)
    print(len(end), len(end[0]))
    light(end)



if __name__ == "__main__":
    main()
