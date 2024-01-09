import sys
sys.path.append('..')
import my_parser as p
import hashlib

inp = p.input_as_lines('inputs/inp.txt')[0]


def four(inp):
    result = hashlib.md5(inp.encode()).hexdigest()
    return result[:4]


mapping = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

R = 4
C = 4
start = (0, 0)
end = (3, 3)
openn = set(['b', 'c', 'd', 'e', 'f'])
queue = [[0, '', start]]
paths = []

while queue:
    steps, path, pos = queue.pop(0)
    if pos == end:
        paths.append(path)
        continue
    r, c = pos
    chars = four(inp + path)
    for dir_, char in zip('UDLR', chars):
        if char in openn:
            dr, dc = mapping[dir_]
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C:
                new_path = path + dir_
                queue.append([steps + 1, new_path, (nr, nc)])

print(paths[0])
print(len(paths[-1]))
