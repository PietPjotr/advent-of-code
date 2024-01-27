import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
target = (7, 770)
depth = 10647

# target = (10, 10)
# depth = 510


def geo_i(x, y, erosions):
    if (x, y) == target or (x, y) == (0, 0):
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        # print(x, y)
        return erosions[y][x - 1] * erosions[y - 1][x]


def create_erosions():
    erosions = [[] for _ in range(target[1] + 1)]
    for y in range(target[1] + 1):
        for x in range(target[0] + 1):
            i = geo_i(x, y, erosions)
            erosion_level = (i + depth) % 20183
            erosions[y].append(erosion_level)

    return erosions


erosions = create_erosions()
p1 = 0
G = []
for row in erosions:
    nrow = []
    for el in row:
        if el % 3 == 0:
            nrow.append('.')
            p1 += 0
        elif el % 3 == 1:
            nrow.append('=')
            p1 += 1
        elif el % 3 == 2:
            nrow.append('|')
            p1 += 2
    G.append(nrow)

# for row in G:
#     print(''.join(row))

print(p1)

