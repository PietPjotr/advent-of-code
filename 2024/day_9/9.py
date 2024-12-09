import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict

L = p.input_as_lines('inputs/inp.txt')
L = L[0]
L = [str(el) for el in L]

def get_data():
    data = []
    for i, el in enumerate(L):
        data += int(el) * [[str(i // 2)], ['.']][i % 2]
    data = list(data)
    return data


def part1():
    data = get_data()
    empty_i = 0
    digit_i = len(data) - 1
    while digit_i > empty_i:

        if data[empty_i] != '.':
            empty_i += 1
            continue

        if not data[digit_i].isdigit():
            digit_i -= 1
            continue

        data[empty_i], data[digit_i] = data[digit_i], '.'

    print(score(data))


def score(data):
    s = 0
    for i, el in enumerate(data):
        if el != '.':
            s += i * int(el)
    return s


def find_empty_block(data, left_bound, right_bound, size):
    a = left_bound

    while a < right_bound:
        # Find the start of an empty space
        while a < right_bound and data[a] != '.':
            a += 1

        # Check the length of the empty block
        b = a
        while b < right_bound and data[b] == '.':
            b += 1

        # empty block that fits the data block
        if b - a >= size:
            return a, b

        # go next empty block
        a = b

    return None, None


def find_data_block(data, right_bound):
    # Find 'end' of the block
    b = right_bound
    while data[b] == '.':
        b -= 1

    # Find start of the block
    a = b
    while data[a] == data[b]:
        a -= 1

    # correct a
    a += 1

    return a, b


def insert(data, dia, dib, eia, R, L):
    si = eia
    # insert
    for j in range(0, dib - dia + 1):
        data[si + j] = data[dia]

    # empty inserted cells
    for k in range(dia, dib + 1):
        data[k] = '.'

    R = dia - 1

    # update valid window
    while data[L].isdigit():
        L += 1

    return R, L


def part2():
    data = get_data()

    # get bounds
    L = ''.join(data).index('.')
    R = len(data) - 1

    while L < R:

        dia, dib = find_data_block(data, R)
        eia, eib = find_empty_block(data, L, R, dib - dia + 1)

        # if data block fits nowhere, go next data block
        if eia is None:
            R = dia - 1
            continue

        # insert
        R, L = insert(data, dia, dib, eia, R, L)

    print(score(data))


part1()
part2()