import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')[0]
l = [i for i in range(256)]


def reverse(l, i, length):
    size = len(l)
    # double the list to ensure wrap around goes right
    l = l + l
    to_rev = l[i: i + length]
    rev = to_rev[::-1]
    l = l[0:i] + rev + l[i + length:]

    # take the relevant slice of the doubled input list
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


def to_bin(hex_string):
    return "{0:0128b}".format(int(hex_string, 16))


p1 = 0
inp = L
key = 'flqrgnkx'
key = inp
grid = []
for i in range(128):
    rkey_string = key + '-' + str(i)
    rkey_bytes = [ord(el) for el in rkey_string] + [17, 31, 73, 47, 23]
    sparse = rounds(l, rkey_bytes, 64)
    dens = dense(sparse)
    hex_string = to_hex(dens)
    final = to_bin(hex_string)
    grid.append(final)
    p1 += final.count('1')

print(p1)


# flood fill over all possible 1 positions and count the distinct number
# of connected groups
groups = set()
ones = []
for r in range(128):
    for c in range(128):
        if grid[r][c] == '1':
            ones.append((r, c))

for one in ones:
    visited = set()
    stack = [one]
    while stack:
        r, c = stack.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 128 and 0 <= nc < 128 and grid[nr][nc] == '1':
                stack.append((nr, nc))

    groups.add(tuple(sorted(visited)))

print(len(groups))
