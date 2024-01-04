import sys
sys.path.append('..')
import my_parser as p
import math

L = p.input_as_lines('inputs/test.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])


def get_divisors(num):
    divs = []
    end = int(math.sqrt(num) + 1)
    for i in range(1, end):
        if num % i == 0:
            divs.append(i)
            divs.append(num // i)
    return divs


inp = 29000000
def delivered(divs, part):
    deliver = 10
    if part == 2:
        deliver = 11
    return sum([div * deliver for div in divs])


def filter_divs(divs):
    return [el for el in divs if el > (max(divs) // 51)]


def solve(start, part):
    m = 0
    for house in range(start, inp // 10, 10):
        divs = get_divisors(house)
        if part == 2:
            divs = filter_divs(divs)
        gifts = delivered(divs, part)
        if gifts / inp > m:
            m = gifts / inp
        if gifts >= inp:
            print(house)
            return house


ret = solve(10, 1)
solve(ret, 2)
