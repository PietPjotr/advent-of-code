import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

firewall = {}
for l in L:
    depth, size = l.split(': ')
    depth = int(depth)
    size = int(size)
    firewall[depth] = [0, size - 1]


def update(firewall, time):
    for k, wall in firewall.items():
        _, rang = wall
        pos = (time) % (2 * (rang))
        if pos >= rang:
            pos = rang - (pos - rang)
        firewall[k] = [pos, rang]

    return firewall


def update_wall(time, rang):
    pos = (time) % (2 * (rang))
    if pos >= rang:
        pos = rang - (pos - rang)
    return pos


def safe(firewall, time):
    for k, wall in firewall.items():
        pos, rang = wall
        s_pos = update_wall(k + time, rang)
        if s_pos == 0:
            return False
    return True


for time in range(10000000):
    firewall = update(firewall, time)
    if time == 0:
        score = 0
        for i in sorted(firewall.keys()):
            firewall = update(firewall, i)
            pos, rang = firewall[i]
            if pos == 0:
                score += i * (rang + 1)

        print(score)

    if safe(firewall, time):
        print(time)
        break
