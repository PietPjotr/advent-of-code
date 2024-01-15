import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')

ports = [[int(el) for el in l.split('/')] for l in L]


def p1():
    starting_ports = [port for port in ports if 0 in port]
    max_steps = 0
    p1 = 0
    p2 = 0
    for port in starting_ports:
        used = set()
        used.add(tuple(port))
        stack = [(0, sum(port), 0, port, used)]
        while stack:
            steps, strength, prev, port, used = stack.pop()
            over = [el for el in port]
            over.remove(prev)
            over = over[0]
            available_ports = [p for p in ports if over in p and tuple(p) not in used]
            if not available_ports:
                if strength > p1:
                    p1 = strength
                if steps >= max_steps:
                    max_steps = steps
                    if strength > p2:
                        p2 = strength
                continue

            for new_port in available_ports:
                new_used = deepcopy(used)
                new_used.add(tuple(new_port))
                stack.append((steps + 1, strength + sum(new_port), over, new_port, new_used))

    print(p1)
    print(p2)


p1()
