import sys
sys.path.append('..')
import my_parser as p

lines = p.input_as_lines('inputs/inp.txt')
lines = [((eval(one)), (eval(two))) for line in lines for one, two in [line.split('~')]]

lines.sort(key=lambda x: min(x[0][2], x[1][2]))

def get_range(xs, ys, zs, xe, ye, ze):
    xs = range(xs, xe + 1)
    ys = range(ys, ye + 1)
    zs = range(zs, ze + 1)
    return [(x, y, z) for x in xs for y in ys for z in zs]


def get_dependencies(i, volsi, lines, minz=0):
    dependencies = []
    for j in range(0, i):
        startj, endj = lines[j]
        if startj[2] < minz and endj[2] < minz:
            continue
        volsj = get_range(*startj, *endj)
        for vol in volsi:
            if vol in volsj:
                dependencies.append(j)
                break
    return dependencies


# dependency list for every line as index and dependencies[index] is the list
# of lines where line index rests on
all_dependencies = [[] for _ in range(len(lines))]
for i in range(len(lines)):
    start, end = lines[i]
    zs, ze = start[2], end[2]
    dependencies = []
    while not dependencies:
        zs -= 1
        ze -= 1
        if zs == 0 or ze == 0:
            break
        start = (start[0], start[1], zs)
        end = (end[0], end[1], ze)
        new_vols = get_range(*start, *end)
        dependencies = get_dependencies(i, new_vols, lines, min(ze, zs))

    lines[i] = ((start[0], start[1], zs + 1), (end[0], end[1], ze + 1))
    all_dependencies[i] = dependencies

not_desintegrate = set()
to_desintegrate = set()
not_supporting = set([i for i in range(len(lines))])

cp = sorted(all_dependencies, key=lambda x: len(x))
for i, deps in enumerate(cp):
    for dep in deps:
        not_supporting.discard(dep)
    if len(deps) == 1:
        not_desintegrate.add(deps[0])
    elif len(deps) > 1:
        for dep in deps:
            if dep not in not_desintegrate:
                to_desintegrate.add(dep)


print(len(to_desintegrate) + len(not_supporting))

res = 0
for i, depsi in enumerate(all_dependencies):
    fallen = set([i])
    for j, depsj in enumerate(all_dependencies):
        if not depsj:
            continue
        if all([dep in fallen for dep in depsj]):
            fallen.add(j)
    res += len(fallen) - 1

print(res)







