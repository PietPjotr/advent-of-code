import sys
sys.path.append('..')
import my_parser as p
from itertools import combinations
from copy import deepcopy
sys.setrecursionlimit(5000)

L = p.input_as_lines('inputs/test.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

floors = [[] for i in range(4)]
for i, line in enumerate(L):
    line = line.replace('.', '')
    line = line.replace('-compatible', '')
    line = [[el for el in l.split(' ')] for l in line.split(', ')]
    for el in line:
        if el[-1] == 'relevant':
            continue
        floors[i].append((el[-2][0], el[-1][0]))


def valid(items):
    generators = [el[0] for el in items if el[-1] == 'g']
    chips = [el[0] for el in items if el[-1] == 'm']
    if len(generators) == 0 or len(chips) == 0:
        return True

    for chip in chips:
        if chip not in generators:
            return False

    return True


def show(cur_floor, floors):
    all_items = []
    for floor in floors:
        for item in floor:
            all_items.append(item)
    all_items.sort()
    tot_len = len(all_items)
    for i, floor in enumerate(floors[::-1]):
        print('F' + str(4 - i), end='  ')
        if 3 - i == cur_floor:
            print('E  ', end='')
        else:
            print('.  ', end='')
        for item in all_items:
            if item in floor:
                print((item[0][0] + item[1][0]).upper() + '  ', end='')
            else:
                print('.   ', end='')
        print()
    print()


def get_state(cur_floor, floors):
    dp = []
    tot_over = set()
    for floor in floors:
        generators = set([el[0] for el in floor if el[-1] == 'g'])
        chips = set([el[0] for el in floor if el[-1] == 'm'])
        pairs = chips & generators
        rest_chips = chips - pairs
        rest_gens = generators - pairs
        over = generators ^ chips
        tot_over |= over
        dp.append([len(pairs), rest_chips, rest_gens])

    mapp = sorted(list(tot_over))

    state = []
    for pair_len, chips, generators in dp:
        chips = tuple([mapp.index(el) for el in chips])
        generators = tuple([mapp.index(el) for el in generators])
        state.append((pair_len, chips, generators))

    state = tuple(state)
    state = (cur_floor, state)

    return state

# test = [[   [('r', 'g')],
#             [('h', 'm'), ('h', 'g'), ('b', 'm')],
#             [('l', 'm'), ('l', 'g')],
#         ],
#         [   [('r', 'g')],
#             [('l', 'm'), ('l', 'g'), ('b', 'm')],
#             [('h', 'm'), ('h', 'g')],
#         ],
# ]

# s1, s2 = get_state(0, test[0]), get_state(0, test[1])
# print(s1 == s2)



def rec_solve(stack):
    while stack:
        res = None
        steps, cur_floor, floors = stack.pop(0)
        # print(steps)

        if len(floors[-1]) == n_items:
            print('solution found: {}'.format(steps))
            return steps

        dp = get_state(cur_floor, floors)
        if dp in DP:
            continue
        DP.add(dp)

        floor = floors[cur_floor]
        items1 = [comb for comb in combinations(floor, 1)]
        items2 = [comb for comb in combinations(floor, 2)]

        for lowest in range(len(floor)):
            if floors[lowest]:
                break
        items2.extend(items1)

        iis = []
        for i in range(cur_floor - 1, cur_floor + 2):
            if i < lowest or i > 3 or i == cur_floor:
                continue
            else:
                iis.append(i)

        next_stack = []
        if cur_floor + 1 in iis:
            for to_carry in items2:
                next_floors = deepcopy(floors)
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor + 1].append(el)

                if not (valid(next_floors[cur_floor]) and valid(next_floors[cur_floor + 1])):
                    continue

                next_stack.append((steps + 1, cur_floor + 1, next_floors))
        res = rec_solve(next_stack)
        if res:
            return res
        next_stack = []
        if cur_floor + 1 in iis:
            for to_carry in items1:
                next_floors = deepcopy(floors)
                next_stack = []
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor + 1].append(el)

                if not (valid(next_floors[cur_floor]) and valid(next_floors[cur_floor + 1])):
                    continue

                next_stack.append((steps + 1, cur_floor + 1, next_floors))
        res = rec_solve(next_stack)
        if res:
            return res

        # lower floor
        next_stack = []
        if cur_floor - 1 in iis:
            for to_carry in items1:
                next_floors = deepcopy(floors)
                next_stack = []
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor - 1].append(el)

                if not (valid(next_floors[cur_floor]) and valid(next_floors[cur_floor - 1])):
                    continue

                next_stack.append((steps + 1, cur_floor - 1, next_floors))
        res = rec_solve(next_stack)
        if res:
            return res
        next_stack = []
        if cur_floor - 1 in iis:
            for to_carry in items2:
                next_floors = deepcopy(floors)
                next_stack = []
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor - 1].append(el)
                if not (valid(next_floors[cur_floor]) and valid(next_floors[cur_floor - 1])):
                    continue

                next_stack.append((steps + 1, cur_floor - 1, next_floors))
        res = rec_solve(next_stack)
        if res:
            return res

    return


n_items = 0
for floor in floors:
    for _ in floor:
        n_items += 1

DP = set()
start = (0, 0, floors)
stack = [start]
res = float('inf')
print(rec_solve(stack))


def solve(floors):
    all_items = []
    for floor in floors:
        for item in floor:
            all_items.append(item)

    final_length = len(all_items)
    start = (0, 0, floors)
    stack = [start]
    DP = set()
    its = 0
    while stack:
        steps, cur_floor, floors = stack.pop(0)
        if its % 1000 == 0:
            print(steps)

        if len(floors[-1]) == final_length:
            break

        dp = get_state(cur_floor, floors)
        if dp in DP:
            continue
        DP.add(dp)

        floor = floors[cur_floor]
        items1 = [comb for comb in combinations(floor, 1)]
        items2 = [comb for comb in combinations(floor, 2)]
        for lowest in range(len(floor)):
            if floors[lowest]:
                break
        lowest = 0
        items2.extend(items1)
        for to_carry in items2:
            for i in range(cur_floor - 1, cur_floor + 2):
                next_floors = deepcopy(floors)

                if i < lowest or i > 3 or i == cur_floor:
                    continue

                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[i].append(el)

                if not (valid(next_floors[cur_floor]) and valid(next_floors[i])):
                    continue
                stack.append((steps + 1, i, next_floors))

        its += 1

    print(steps)


# import time

# s = time.time()
# solve(floors)
# e = time.time()
# print("it took {} seconds to complete the calculations".format(e - s))
