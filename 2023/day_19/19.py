import sys
sys.path.append('..')
import my_parser as p
from itertools import groupby
import re

lines = p.input_split_by_emtpy_newline('inputs/inp.txt')

fs, ps = lines
parts = []
flows = {}


for part in ps:
    els = part[1:-1].split(',')
    part = [int(el.split('=')[1]) for el in els]
    parts.append(part)

for flow in fs:
    name, rest = flow.split('{')
    flows[name] = [str(el) for el in rest[0:-1].split(',')]


def check_part(part, flows):
    stack = [(part, 'in')]
    while stack:
        vals, flow_name = stack.pop()
        els = flows[flow_name]

        final_destination = els[-1]
        for el in els[:-1]:
            cat = el[0]
            cond, destination = el[1:].split(':')
            if eval(str(vals['xmas'.index(cat)]) + cond):
                final_destination = destination
                break

        if final_destination == 'A':
            break
        elif final_destination == 'R':
            vals = []
        else:
            stack.append((vals, final_destination))

    return sum(vals)


def part1():
    res = sum([check_part(part, flows) for part in parts])
    print(res)



def split_range(r, limit, cmd):
    """first range new branch, second range current branch """
    if cmd == '<':
        r1 = (r[0], min(r[1], limit))
        r2 = (max(r[0], limit - 1), r[1])
        return r1, r2
    elif cmd == '>':
        r1 = (r[0], min(r[1], limit + 1))
        r2 = (max(r[0], limit), r[1])
        return r2, r1


def get_score(vals):
    res = 1
    for val in vals:
        delta = val[1] - val[0] - 1
        if delta < 0:
            return 0
        res *= delta
    return res


def part2():
    rs = []
    profiles = [([(0, 4001), (0, 4001), (0, 4001), (0, 4001)], 'in')]
    while profiles:
        vals, cur_name = profiles.pop()
        if cur_name == 'R':
            continue
        if cur_name == 'A':
            rs.append(vals)
            continue
        cur_flow = flows[cur_name]
        final_dest = cur_flow[-1]
        for el in cur_flow[:-1]:
            new_vals = vals.copy()
            dest = el.split(':')[-1]
            cat = el[0]
            cmd = el[1]
            lim = int(re.findall(r'[0-9]+', el)[0])
            i = 'xmas'.index(cat)
            r1, r2 = split_range(vals[i], lim, cmd)
            if r1[0] > r1[1] or r2[0] > r2[1]:
                continue
            new_vals[i] = r1
            vals[i] = r2
            profiles.append((new_vals, dest))
        profiles.append((vals, final_dest))

    ress = [get_score(vals) for vals in rs]
    res = sum(ress)
    print(res)


part1()
part2()
