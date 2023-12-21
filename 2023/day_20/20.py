import sys
sys.path.append('..')
import my_parser as p
import collections
import math

lines = p.input_as_lines('inputs/inp.txt')

states = {}
for line in lines:
    src, dest = line.split(' -> ')
    kind, name = src[0], src[1:]
    dest = dest.split(', ')
    states[name] = (kind, 0, dest)

# get the list of nodes before the node before the rx node
ns = []
tar = ''
for k, v in states.items():
    _, _, dests = v
    if 'rx' in dests:
        tar = k
        break
for k, v in states.items():
    _, _, dests = v
    if tar in dests:
        ns.append(k)

# update all the previous remembered signals of the & nodes to 0
for k, v in states.items():
    name = k
    kind, _, dests = v
    if kind == '&':
        states[name] = (kind, {}, dests)
        kind, d, _ = states[name]
        for k, v in states.items():
            kind, val, dests = v
            if name in dests:
                d[k] = 0

cycles = []
stack = collections.deque()
signals = [0, 0]
part2 = False
i = 1
while not part2:
    stack.append(('btn', 0, 'roadcaster'))
    signals[0] += 1
    while stack:
        src, rec, name = stack.popleft()
        if name not in states:
            continue
        if name in ns and rec == 0 and len(cycles) < 4:
            cycles.append(i)
            if len(cycles) == 4:
                part2 = True

        kind, val, dests = states[name]
        if kind == 'b':
            for dest in dests:
                signals[val] += 1
                stack.append((name, val, dest))
        if kind == '%':
            if rec == 1:
                continue
            if rec == 0:
                val = [0, 1][val-1]
                states[name] = (kind, val, dests)
                for dest in dests:
                    signals[val] += 1
                    stack.append((name, val, dest))
        if kind == '&':
            val[src] = rec
            send = 1
            if all([v == 1 for v in val.values()]):
                send = 0
            for dest in dests:
                signals[send] += 1
                stack.append((name, send, dest))

    if i == 1000:
        print(signals[0] * signals[1])
    i += 1

print(math.lcm(*cycles))
