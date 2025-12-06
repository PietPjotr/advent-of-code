"""
Part 1; 'regular solution'
part 2; Was originaly brute force but now its a bit smarter and faster making
use of the fact that we can calculate directly using mod and floordiv how many
times the operation would 'cross 0'.

p2 finish: 840 something!! top 1k yay (first try challenge completed lol)
"""

import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')


def p1():
    d = 50
    zeroes = 0
    for l in L:
        n = u.get_all_numbers(l)
        dir = l[0]
        if dir == "L":
            d = (d + n) % 100
        if dir == "R":
            d = (d - n) % 100
        if d == 0:
            zeroes += 1

    print(zeroes)

p1()


def p2():
    d = 50
    zeroes = 0
    for l in L:
        n = u.get_all_numbers(l)
        n0 = n
        dir = l[0]
        if dir == "L":
            d0 = d if d != 0 else 100

            # first crossing
            zeroes += (n >= d0)
            n -= (n >= d0) * d0

            # modulo crossings for big n
            zeroes += max(n // 100, 0)

            d = (d - n0) % 100
        if dir == "R":
            d0 = 100 - d
            zeroes += (n >= d0)
            n -= (n >= d0) * d0
            zeroes += max(n // 100, 0)

            d = (d + n0) % 100

    print(zeroes)

p2()
