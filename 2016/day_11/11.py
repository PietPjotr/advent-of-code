import sys
sys.path.append('..')
import my_parser as p
from itertools import combinations
from copy import deepcopy


def valid(items):
    generators = [el[0] for el in items if el[-1] == 'g']
    chips = [el[0] for el in items if el[-1] == 'm']
    if len(generators) == 0 or len(chips) == 0:
        return True

    for chip in chips:
        if chip not in generators:
            return False

    return True


def get_state(cur_floor, floors):
    """I don't quite understand why but apparently we can collapse all states
    into the same states dependent only on the amount of pairs, the amount of
    chips and the amount of generators per floor. I would expect that it also
    matters where the other generator and chips are, but apparently not."""
    state = []
    for floor in floors:
        generators = set([el[0] for el in floor if el[-1] == 'g'])
        chips = set([el[0] for el in floor if el[-1] == 'm'])
        pairs = chips & generators
        rest_chips = chips - pairs
        rest_gens = generators - pairs
        state.append((len(pairs), len(rest_chips), len(rest_gens)))

    state = tuple(state)
    state = (cur_floor, state)

    return state


def bfs(floors):
    """Finds the solution in a few seconds"""
    n_items = 0
    for floor in floors:
        for _ in floor:
            n_items += 1

    DP = set()
    start = (0, 0, floors)
    stack = [start]
    while stack:
        steps, cur_floor, floors = stack.pop(0)

        if len(floors[-1]) == n_items:
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

        iis = [i for i in range(cur_floor - 1, cur_floor + 2) if lowest <= i <= 3 and i != cur_floor]

        # Moving up 2 items
        if cur_floor + 1 in iis:
            for to_carry in items2:
                next_floors = deepcopy(floors)
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor + 1].append(el)
                if valid(next_floors[cur_floor]) and valid(next_floors[cur_floor + 1]):
                    stack.append((steps + 1, cur_floor + 1, next_floors))

        # Moving up 1 item
        if cur_floor + 1 in iis:
            for to_carry in items1:
                next_floors = deepcopy(floors)
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor + 1].append(el)
                if valid(next_floors[cur_floor]) and valid(next_floors[cur_floor + 1]):
                    stack.append((steps + 1, cur_floor + 1, next_floors))

        # Moving down 1 item
        if cur_floor - 1 in iis:
            for to_carry in items1:
                next_floors = deepcopy(floors)
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor - 1].append(el)
                if valid(next_floors[cur_floor]) and valid(next_floors[cur_floor - 1]):
                    stack.append((steps + 1, cur_floor - 1, next_floors))

        # Moving down 2 items
        if cur_floor - 1 in iis and cur_floor - 2 in iis:
            for to_carry in items2:
                next_floors = deepcopy(floors)
                for el in to_carry:
                    next_floors[cur_floor].remove(el)
                    next_floors[cur_floor - 1].append(el)
                if valid(next_floors[cur_floor]) and valid(next_floors[cur_floor - 1]):
                    stack.append((steps + 1, cur_floor - 1, next_floors))

    return None


def main():
    L = p.input_as_lines('inputs/inp.txt')

    floors = [[] for i in range(4)]
    for i, line in enumerate(L):
        line = line.replace('.', '')
        line = line.replace('-compatible', '')
        line = [[el for el in l.split(' ')] for l in line.split(', ')]
        for el in line:
            if el[-1] == 'relevant':
                continue
            floors[i].append((el[-2][0], el[-1][0]))

    floors2 = deepcopy(floors)
    floors2[0].append(('e', 'g'))
    floors2[0].append(('e', 'm'))
    floors2[0].append(('d', 'g'))
    floors2[0].append(('d', 'm'))

    # also time this function
    print(bfs(floors))

    print(bfs(floors2))


if __name__ == '__main__':
    main()