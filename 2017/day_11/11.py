import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
L = L[0].split(',')

mapp = {'n':(0, 2),
        's':(0, -2),
        'ne':(1, 1),
        'se':(1, -1),
        'nw':(-1, 1),
        'sw':(-1, -1),
        }


def get_distance(x, y):
    # for x distance use 1 unit per distance, for diag-y use 1 unit
    # and for vertical y use 2 units per distance, then calc by using the fact
    # that we can travel 1 y disance per x distance, and the remaining y's
    # can be traveled directly vertically so we divide by 2
    return abs(x) + max(0, (abs(y) - abs(x)) // 2)


def solve(lines):
    p2 = 0
    x, y = 0, 0
    for ins in lines:
        dx, dy = mapp[ins]
        x += dx
        y += dy
        p2 = max(p2, get_distance(x, y))

    return get_distance(x, y), p2


p1, p2 = solve(L)
print(p1)
print(p2)