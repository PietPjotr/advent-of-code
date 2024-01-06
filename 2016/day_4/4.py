import sys
sys.path.append('..')
import my_parser as p
import re


def decrypt(name, ID):
    res = ''
    name = name.split('-')
    lb = ord('a')
    for word in name:
        for el in word:
            offset = ID % 26
            new = chr(lb + (ord(el) - lb + offset) % 26)
            res += new
        res += ' '
    return res

L = p.input_as_lines('inputs/inp.txt')


def solve():
    p1 = 0
    p2 = 0
    for room in L:
        freq = {}
        name, check = re.findall(r'[a-z-]+', room)
        ID = int(re.findall(r'[0-9]+', room)[0])
        og_name = name[:-1]
        name = name.replace('-', '')
        for el in name:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1

        s = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        test = ''.join([el[0] for el in s][:5])

        if test == check:
            p1 += ID
            room_name = decrypt(og_name, ID)
            if 'northpole' in room_name:
                p2 = ID

    print(p1)
    print(p2)

solve()
