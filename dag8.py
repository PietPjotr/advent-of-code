import re
from itertools import chain

def deel1():
    with open("dag8_input.txt", "r") as f:
        lines = []
        for line in f.readlines():
            add_temp = line.split(' | ')[1].strip()
            add = add_temp.split(' ')
            lines.append(add)
    print(lines)

    freq = 0
    for line in lines:
        for number in line:
            if len(number) == 2 or len(number) == 4 or len(number) == 3 or len(number) == 7:
                freq += 1
                print(number)
            if len(number) == 5:
                print(number)

    print(freq)


def compare(one, two):
    """ This function checks whether both string one and two all contain the
    same characters. Raturns True if one and two are combinations of eachoter.
    """
    if len(one) != len(two):
        return False
    for letter in one:
        if letter not in two:
            return False
    return True

def subtract(one, two):
    """ This function removes all the characters from one that are contained in
    two. and returns the result. """
    minus = ''
    for element in two:
        minus += element

    res = ''
    for number in one:
        if number not in minus:
            res += number
    return res

def containsAll(one, two):
    """ Check whether one contains all of the items in two. """
    return all([c in one for c in two])

def translate(entry):
    """ This function takes an entry in the shape of a 2d array with two
    elements: input and output respectively. And returns an array with the
    string that belongs to the corresponding index in de array."""
    t = ''
    tr = ''
    tl = ''
    m = ''
    br = ''
    bl = ''
    b = ''

    zero = ''
    one = ''
    four = ''
    six = ''
    seven = ''
    eight = ''
    nine = ''

    entry = list(chain.from_iterable(entry))
    for number in entry:
        if len(number) == 2:
            one = number
        if len(number) == 3:
            seven = number
        if len(number) == 4:
            four = number
        if len(number) == 7:
            eight = number

    t = subtract(seven, one)
    tr = br = one
    tl = m = subtract(four, [one])
    bl = b = subtract(eight, [four, t])

    six_found = False
    nine_found = False
    zero_found = False
    end = False
    for number in entry:
        if len(number) == 6:
            if not containsAll(number, m) and not zero_found:
                zero = number
                zero_found = True
                m = subtract(m, [zero])
                tl = subtract(tl, m)

            elif containsAll(number, bl) and not six_found:
                six = number
                six_found = True
                tr = subtract(tr, [six])
                br = subtract(br, tr)

            elif containsAll(number, tr) and not nine_found:
                nine = number
                nine_found = True
                bl = subtract(bl, [nine])
                b = subtract(b, [bl])

    two = t + tr + m + bl + b
    three = t + tr + m + br + b
    five = t + tl + m + br + b

    return [zero, one, two, three, four, five, six, seven, eight, nine]


def deel2():
    with open("dag8_input.txt", "r") as f:
        lines = []
        for line in f.readlines():
            add_temp = line.split(' | ')
            lines.append([add_temp[0].split(' '), add_temp[1].strip().split(' ')])

    freq = 0
    results = []

    for line in lines:
        result = ''
        signals = translate(line)
        for number in line[1]:
            for i, signal in enumerate(signals):
                if compare(number, signal):
                    result += str(i).strip()

        results.append(int(result))

    # print(results)
    print(sum(results))




deel2()