import sys
sys.path.append('..')
import my_parser as p
import hashlib


L = p.input_as_lines('inputs/inp.txt')

inp = L[0]


def gen_hashes(hash_func):
    hashes = []
    for salt in range(24000):
        hashes.append(hash_func(inp + str(salt)))

    return hashes


def single_hash(string):
    return hashlib.md5(string.encode()).hexdigest()


def much_hash(string):
    for i in range(2017):
        string = hashlib.md5(string.encode()).hexdigest()
    return string


def in_next(hashes, start, end, char):
    for h in range(start, end):
        result = hashes[h]
        for i in range(len(result) - 4):
            window = result[i:i+5]
            if all([el == char for el in window]):
                return True
    return False


def solve(hash_func):
    keys = []
    salt = 0
    hashes = gen_hashes(hash_func, inp)
    while len(keys) < 64:
        to_hash = inp + str(salt)
        result = hash_func(to_hash)
        for i in range(len(result) - 2):
            window = result[i:i+3]
            if window[0] == window[1] == window[2]:
                char = window[0]
                b = in_next(hashes, salt + 1, salt + 1001, char)
                # print(salt, b)
                if b:
                    keys.append(salt)
                    # print(salt)
                break
        salt += 1

    print(keys[-1])


# takes fucking ages around 1,5 min for both parts
solve(single_hash)
solve(much_hash)
