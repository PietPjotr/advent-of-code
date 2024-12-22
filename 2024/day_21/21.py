import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict
from collections import deque
from itertools import product
from functools import cache
from itertools import product
from collections import Counter

codes = p.input_as_lines('inputs/inp.txt')

G1 = """789
456
123
#0A"""

G2 = """#^A
<v>"""

G1 = [[el for el in line] for line in G1.split('\n')]
G2 = [[el for el in line] for line in G2.split('\n')]

G1 = Grid(G1)
G2 = Grid(G2)
G1.remove('#')
G2.remove('#')


def get_all_shortest_paths(G, s, e):
    queue = deque([(s, [s], set(), 0)]) # pos, path, visited, dist
    paths = []
    shortest_dist = float('inf')

    while queue:
        current, path, visited, dist = queue.popleft()

        if current == e:
            if dist < shortest_dist:
                shortest_dist = dist
                paths = [path]
            elif dist == shortest_dist:
                paths.append(path)

        for neighbour in current.nbs():
            if neighbour in G and neighbour not in visited:
                if dist + 1 <= shortest_dist:
                    queue.append((neighbour, path + [neighbour], visited | {neighbour}, dist + 1))

    return paths


# changes a path to a string of inputs to perform to get the path
# independent of the grid
def extract_dirs(path):
    res = ''
    for a, b in zip(path[:-1], path[1:]):
        d = b - a
        dirs = d.dirs()
        res += ['^', '>', 'v', '<'][dirs.index(d)]
    return res + 'A'


# take a single start and end position and return one of the 'best' next paths:
# this is based off of the distance from the string in the path to A in G2
# directional pad, and off the idea that if we have '>>^A' or '>^>A', we can
# guarantee that for next generation, the first one is better since we can
# go to '>' press it twice and move to the next rather than having to move
# twice to get both '>' presses.
def get_strings_single_push(G, start_char, end_char):
    startpos = G.find(start_char)
    endpos = G.find(end_char)
    shortest_paths = get_all_shortest_paths(G, startpos, endpos)
    shortest_strings = [extract_dirs(path) for path in shortest_paths]

    # sort on the above mentioned idea
    sorting_key = lambda x: sum(Pos.dist(G2.find(a), G2.find(b)) for a, b in zip(x[:-1], x[1:]))
    shortest_strings = sorted(shortest_strings, key=sorting_key)

    return sorted(shortest_strings, key=sorting_key)[0]  # return the 'shortest'


def get_transitions(G):
    transitions = {}
    distinc_chars = list(set([v for v in G.values()]))
    for p in product(distinc_chars, repeat=2):
        possible_strings = get_strings_single_push(G, *p)
        transitions[p] = possible_strings

    return transitions


def get_next_string_parts(G, code, transitions):
    parts = []
    code = 'A' + code  # start at 'A'
    for start_char, dest_char in zip(code[:-1], code[1:]):
        sub_string = transitions[(start_char, dest_char)]
        parts.append(sub_string)

    return parts


def string_to_counter(string):
    string = string.replace('A', 'A ')
    string = string.split()
    return Counter(string)


def solve(iterations):
    score = 0
    for code in codes[:]:
        # get all possible transitions for both grids
        transitions1 = get_transitions(G1)
        transitions2 = get_transitions(G2)

        # do the one string transition for the numerical pad
        string = ''.join(get_next_string_parts(G1, code, transitions1))

        counter = string_to_counter(string)

        for i in range(iterations):
            next_counter = defaultdict(int)

            for el, count in counter.items():
                next_string_parts = get_next_string_parts(G2, el, transitions2)
                for s in next_string_parts:
                    next_counter[s] += count
            counter = next_counter

        length = sum([len(k) * v for k, v in counter.items()])
        num = get_all_nums(code)[0]

        score += length * num

    return score


print(solve(2))
print(solve(25))
