import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

layers = [int(line.split(': ')[0]) for line in L]
firewall = [[] for _ in range(max(layers) + 1)]
for l in L:
    depth, size = l.split(': ')
    depth = int(depth)
    size = int(size)
    firewall[depth] = [0, size - 1]


def update(firewall, time):
    for i in range(len(firewall)):
        wall = firewall[i]
        if not wall:
            continue
        _, rang = wall
        pos = (time) % (2 * (rang))
        if pos >= rang:
            pos = rang - (pos - rang)
        firewall[i] = [pos, rang]

    return firewall


def update_wall(time, rang):
    pos = (time) % (2 * (rang))
    if pos >= rang:
        pos = rang - (pos - rang)
    return pos


def safe(firewall, time):
    for i in range(len(firewall)):
        if firewall[i]:
            pos, rang = firewall[i]
            s_pos = update_wall(i + time, rang)
            if s_pos == 0:
                return False
    return True


for time in range(10000000):
    firewall = update(firewall, time)
    if time == 0:
        score = 0
        for pos in range(len(firewall)):

            if firewall[pos] and firewall[pos][0] == 0:
                score += pos * (firewall[pos][1] + 1)

            time += 1
            firewall = update(firewall, time)
        print(score)

    if safe(firewall, time):
        print(time)
        break
