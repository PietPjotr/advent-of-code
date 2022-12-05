
# TODO: figure out how the fuck i can calculate the amount of operands that an
# a message with 0 as length_id has (so only the amount of bits in the load
# are known.)

import parser
import numpy as np
from collections import deque

def hex_to_bin(string):
    table = {'0' : '0000',
            '1' : '0001',
            '2' : '0010',
            '3' : '0011',
            '4' : '0100',
            '5' : '0101',
            '6' : '0110',
            '7' : '0111',
            '8' : '1000',
            '9' : '1001',
            'A' : '1010',
            'B' : '1011',
            'C' : '1100',
            'D' : '1101',
            'E' : '1110',
            'F' : '1111', }
    s_bin = ''
    for s in string:
        s_bin += str(table[s]).strip()

    return s_bin


def parse_version4(load):
    num = load[1:5]
    n = 5
    keep_reading = load[0]
    while keep_reading == '1':
        keep_reading = load[n]
        num += load[n+1:n+5]
        n += 5

    num = int(num, 2)

    if len(load) - n < 6:

        return '', num
    else:
        return load[n:], num



def parse_other(load, versions):
    version = load[0:3]
    type_id = load[3:6]

    load = load[6:]

    length = -1
    if type_id == '100':
        next_packet, num = parse_version4(load)
        versions.append(num)
        load, versions = parse_other(next_packet, versions)

    elif len(load) > 18 and type_id != '100':
        # print("adding op: ", (version, type_id))
        length_bit = load[0]
        if length_bit == '1':
            nop = int(load[1:12], 2)
            versions.append((type_id, nop))
            next_packet = load[12:]
            # size = int(len(next_packet) / nop)
            load, versions = parse_other(next_packet, versions)

        elif length_bit == '0':
            versions.append((type_id, "howww"))
            nob = int(load[1:16], 2)
            next_packet = load[16:]
            load, versions = parse_other(next_packet, versions)


    return load, versions


def version_to_ints(versions):
    ints = []
    for version in versions:
        ints.append(int(version, 2))

    return ints


def isdigit(ch):
    if(ord(ch) >= 48 and ord(ch) <= 57):
        return True
    return False


def mult(l):
    res = 1
    for el in l:
        res *= el
    return res


def evaluate(expr):
    table = {'000': '+',
            '001' : '*' ,
            '010' : 'min',
            '011' : 'max',
            '101' : '>',
            '110' : '<',
            '111' :'=='}

    s = []
    for x in expr[::-1]:
        if type(x) == int:
            s.append(x)

        elif table[x] in set(['+', '*', 'min', 'max']):
            nums = []
            # print(s, on, x)
            while s:
                on = s.pop()
                nums.append(on) # maybe append in case certain values are popped of the stack in revers order.

            print(nums)

            op = table[x]
            if op == '+':
                s.append(sum(nums))
                print("after sum: ", s)
            elif op == '*':
                s.append(mult(nums))
                print("after mult: ", s)
            elif op == 'min':
                s.append(min(nums))
            elif op == 'max':
                s.append(max(nums))
        else:
            op = table[x]
            num1 = s.pop()
            num2 = s.pop()
            if op == '>':
                s.append(int(num1 > num2))
            elif op == '<':
                s.append(int(num1 < num2))
            elif op == '==':
                s.append(int(num1 == num2))
            else:
                print('wtf is going on.')

    return s


def main():
    lines = parser.input_as_string('inputs/dag16.txt')
    # lines : parser.input_as_lines('inputs/16_test.txt')
    # lines : parser.input_as_ints('inputs/16_test.txt')
    # lines : parser.input_as_grid('inputs/16_test.txt')
    binary_string = hex_to_bin(lines)
    _, versions = parse_other(binary_string, [])
    print(versions)
    # ints = version_to_ints(versions)
    # print(ints)
    # print(sum(ints))

    # 2:
    # _, structure = parse_other(binary_string, [])
    exprsn = ['001','000', 9, 9,'000', 9, 9]
    print(evaluate(exprsn))




if __name__ == "__main__":
    main()