import parser
import hashlib

import math


def toBinary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


def deel1(lines):
    check = '000000'
    answer = 0
    for i in range(4000000):
        encode = lines + str(i).strip()
        result = hashlib.md5(encode.encode('ascii'))
        # print(result)
        # print(result.hexdigest()[:5])
        if result.hexdigest()[:6] == check:

            answer = i
            break
    print(answer)


def deel2(lines):
    pass


def main():
    lines = 'bgvyzdsv'
    # lines = 'abcdef'
    # lines = parser.input_as_string('inputs/.txt')
    # lines = parser.input_as_lines('inputs/.txt'
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    deel1(lines)


if __name__ == "__main__":
    main()
