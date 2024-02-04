import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')


def manhattan(p1, p2):
    return sum([abs(p1[i] - p2[i]) for i in range(4)])


points = [tuple([int(el) for el in line.split(',')]) for line in L]

visited = set()
constellations = []
while len(visited) < len(points):
    for p in points:
        if p not in visited:
            stack = [p]
            visited.add(p)
            break
    const = [p]
    while stack:
        point = stack.pop()
        for npoint in points:
            if npoint in visited:
                continue
            if manhattan(point, npoint) <= 3:
                stack.append(npoint)
                visited.add(npoint)
                const.append(npoint)
    constellations.append(const)


print(len(constellations))
