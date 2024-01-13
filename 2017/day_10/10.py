import sys
sys.path.append('..')
import my_parser as p

inp = p.input_as_lines('inputs/inp.txt')[0]
inp1 = [int(el) for el in inp.strip().split(',')]
inp2 = [ord(el) for el in inp]
inp2 += [17, 31, 73, 47, 23]

l = [i for i in range(256)]


def reverse(l, i, length):
    size = len(l)
    l = l + l
    to_rev = l[i: i + length]
    rev = to_rev[::-1]
    l = l[0:i] + rev + l[i + length:]
    ret = l[size: size + i] + l[i: size]
    return ret


def rounds(l, inp, rounds):
    skip_size = 0
    i = 0
    for r in range(rounds):
        for num in inp:
            l = reverse(l, i, num)
            i = (i + num + skip_size) % len(l)
            skip_size += 1

    return l


res1 = rounds(l, inp1, 1)
print(res1[0] * res1[1])


def dense(l):
    ret = []
    for i in range(len(l) // 16):
        window = l[16 * i: 16 * i + 16]
        block = window[0]
        for el in window[1:]:
            block ^= el
        ret.append(block)

    return ret


def to_hex(l):
    ret = ''
    for el in l:
        delta = hex(el)
        if len(delta) == 4:
            ret += delta[2:]
        elif len(delta) == 3:
            ret += '0' + delta[2:]
    return ret


sparse = rounds(l, inp2, 64)
dens = dense(sparse)
final = to_hex(dens)
print(final)
