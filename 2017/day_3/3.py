import sys
sys.path.append('..')
import my_parser as p
import math

L = p.input_as_lines('inputs/inp.txt')
inp = int(L[0])


def get_dist(num, struct = {}):
    struct = {}
    # find the whole roots it falls between:
    if num == 1:
        return 0
    i = 1
    j = 0
    while i*i < num:
        i += 2
        j += 1
    high = i ** 2
    # diagonals:
    corners = [high - j * (i - 1) for j in range(1, 5)]
    corners = [high] + corners
    if num in corners:
        return 2 * j
    # find the side the num lies on:
    lci = 0
    corner = corners[lci]
    while num < corner:
        lci += 1
        corner = corners[lci]

    if lci == 1:
        y = -j
        x = j - corners[lci - 1] + num
    elif lci == 2:
        x = -j
        y = -j + corners[lci - 1] - num
    elif lci == 3:
        y = j
        x = -j + corners[lci - 1] - num
    elif lci == 4:
        x = j
        y = -j + corners[lci - 1] - num

    if (x, y) not in struct:
        struct[(x, y)] = num
    return abs(x) + abs(y), struct


print(get_dist(inp)[0])

# apparently there is a website for all different kind of integer sequences:
# https://oeis.org/A141481/b141481.txt

print(349975)

