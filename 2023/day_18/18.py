import sys
sys.path.append('..')
import my_parser as p

lines = p.input_as_lines('inputs/test.txt')
lines = [line.split(' ') for line in lines]

DR = [1, 0, -1, 0]
DC = [0, 1, 0, -1]


def parse1(line):
    map_dir = {
        'U': 0,
        'R': 1,
        'D': 2,
        'L': 3
    }

    d, l, _ = line
    d = map_dir[d]
    return d, int(l)


def parse2(line):
    _, _, col = line
    col = col[2:-1]
    d = (int(col[-1]) + 1) % 4  # ensuring right down left up maps to up right down left
    l = int(col[:-1], 16)
    return d, l


def shoelace_pick(lines, parser=parse2):
    points = []
    r, c = 0, 0
    b = 0
    for line in lines:
        d, l = parser(line)

        nc = c + DC[d] * l
        nr = r + DR[d] * l
        b += l
        points.append((nr, nc))
        r, c = nr, nc

    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
    i = A - b // 2 + 1

    print(i + b)


def wrong(lines, parser=parse2):
    tot = 1
    width = 1
    for line in lines:
        d, l = parser(line)

        add = 0
        if d == 1:
            width += l
            add = l

        if d == 3:
            add = l + 1
            width -= l - 1

        if d == 2:
            add = width * (l - 1)
        if d == 0:
            add = -width * (l - 2)
        print(tot, add, l, width)
        tot += add

    print(tot)


lines = p.input_as_lines('inputs/test.txt')
lines = [line.split(' ') for line in lines]

# wrong(lines, parse2)

shoelace_pick(lines, parse1)
shoelace_pick(lines, parse2)


def part1(lines):
    holes = set()
    start = (0, 0)
    r, c = start

    for line in lines:
        d, l = parse1(line)
        nc = c + DC[d] * l
        nr = r + DR[d] * l

        for dc in range(min(c, nc), max(c, nc) + 1):
            for dr in range(min(r, nr), max(r, nr) + 1):
                holes.add((dr, dc))

        r, c = nr, nc


    def fill_holes(holes, start, lim=1000):
        rest = set()
        stack = [start]
        i = 0
        while stack and i < lim:
            r, c = stack.pop()
            for i in range(4):
                nr = r + DR[i]
                nc = c + DC[i]
                if not (nr, nc) in holes and not (nr, nc) in rest:
                    rest.add((nr, nc))
                    stack.append((nr, nc))
            i += 1
        return rest

    start = (-1, 1)
    fill = fill_holes(holes, start)

    print(len(holes) + len(fill))

