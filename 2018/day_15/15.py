import sys
sys.path.append('..')
import my_parser as p
from collections import deque
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])


class Unit:
    def __init__(self, kind, pos):
        self.kind = kind
        self.r = pos[0]
        self.c = pos[1]
        self.hp = 200
        self.dmg = 3

    def attack(self, target):
        target.hp -= self.dmg

    def move(self, path):
        nr, nc = path[0]
        self.r = nr
        self.c = nc

    def get_neighbours(self):
        return [(self.r - dr, self.c - dc) for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]]

    def __str__(self):
        return str((self.kind, (self.r, self.c), self.hp, self.dmg))

    def __repr__(self):
        return str(self)


def sort_paths_by_coordinates(paths):
    # Sort the paths based on the coordinates in reading order
    return sorted(paths, key=lambda path: [(coord[0], coord[1]) for coord in path])


class Game:
    def __init__(self, grid):
        self.R = len(grid)
        self.C = len(grid[0])
        self.G = grid
        self.time = 0

        goblins = []
        elves = []
        for r in range(self.R):
            for c in range(self.C):
                el = self.G[r][c]
                if el == 'G':
                    goblins.append(Unit('G', (r, c)))
                    self.G[r][c] = '.'
                elif el == 'E':
                    elves.append(Unit('E', (r, c)))
                    self.G[r][c] = '.'

        self.goblins = goblins
        self.elves = elves

    def find_targets(self, unit):
        target_list = self.find_target_list(unit)
        all_positions = self.find_used_positions()
        all_positions.remove((unit.r, unit.c))
        target_positions = []
        for target in target_list:
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr = target.r + dr
                nc = target.c + dc
                if self.G[nr][nc] == '.' and (nr, nc) not in all_positions:
                    target_positions.append((nr, nc))
        return target_positions

    def find_closest_position(self, unit):
        used_positions = self.find_used_positions()
        queue = deque([(0, unit.r, unit.c)])
        target_positions = self.find_targets(unit)
        # self.show(target_positions, '?')
        visited = set()
        positions = []
        while queue:
            steps, r, c = queue.popleft()
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visited and self.G[nr][nc] == '.' and (nr, nc) not in used_positions:
                    if (nr, nc) in target_positions:
                        positions.append((steps + 1, (nr, nc)))
                    queue.append((steps + 1, nr, nc))
                    visited.add((nr, nc))

        # not sure if specifiying the key like this is actually necessary
        if positions:
            positions.sort(key=lambda x: (x[0], x[1]))
            distance = min([pos[0] for pos in positions])
            closest_positions = [pos[1] for pos in positions if pos[0] == distance]
            # self.show(closest_positions, '!')
            # self.show([closest_positions[0]], '+')
            return distance, closest_positions[0]
        return (-1, None)

    def find_shortest_path_efficient(self, unit):
        used_positions = self.find_used_positions()
        queue = deque([(unit.r, unit.c, [])])
        target_positions = self.find_targets(unit)
        while queue:
            r, c, path = queue.popleft()
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in path and self.G[nr][nc] == '.' and (nr, nc) not in used_positions:
                    if (nr, nc) in target_positions:
                        return path + [(nr, nc)]
                    queue.append((nr, nc, path + [(nr, nc)]))
        return []

    def find_used_positions(self):
        goblin_positions = [(goblin.r, goblin.c) for goblin in self.goblins if goblin.hp > 0]
        elf_positions = [(elf.r, elf.c) for elf in self.elves if elf.hp > 0]
        return goblin_positions + elf_positions

    def find_shortest_path_dfs(self, unit, max_steps, target):
        all_positions = self.find_used_positions()
        stack = [[0, unit.r, unit.c, []]]
        paths = []
        while stack:
            steps, r, c, path = stack.pop()
            if steps > max_steps:
                continue
            if (r, c) == target:
                paths.append(path)
                continue
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in path and self.G[nr][nc] == '.' and (nr, nc) not in all_positions:
                    stack.append((steps + 1, nr, nc, path + [(nr, nc)]))

        if paths:
            return sort_paths_by_coordinates(paths)[0]

        assert False

    def find_target_list(self, unit):
        neighs = []
        if unit.kind == 'E':
            target_list = self.goblins
        elif unit.kind == 'G':
            target_list = self.elves
        return target_list

    def turn(self):
        all_units = self.elves + self.goblins
        all_units.sort(key=lambda x: (x.r, x.c))
        for n, unit in enumerate(all_units):
            # print(n, unit)
            if unit.hp <= 0:
                continue

            target_list = self.find_target_list(unit)

            # check if we can attack
            if any([(enemy.r, enemy.c) in unit.get_neighbours() for enemy in target_list]):
                neighs = unit.get_neighbours()
                attackable_units = [enemy for enemy in target_list if (enemy.r, enemy.c) in neighs and enemy.hp > 0]
                if not attackable_units:
                    continue
                attackable_units.sort(key=lambda x: (x.hp, x.r, x.c))
                unit.attack(attackable_units[0])
                continue

            # we cannot attack, see if we can move instead
            steps, closest_position = self.find_closest_position(unit)
            # code for no reachable positions so we continue
            if steps == -1:
                continue
            path = self.find_shortest_path_dfs(unit, steps, closest_position)

            # move to the closest target
            unit.move(path)

            # again find if we can attack
            if any([(enemy.r, enemy.c) in unit.get_neighbours() for enemy in target_list]):
                neighs = unit.get_neighbours()
                attackable_units = [enemy for enemy in target_list if (enemy.r, enemy.c) in neighs and enemy.hp > 0]
                if not attackable_units:
                    continue
                attackable_units.sort(key=lambda x: (x.hp, x.r, x.c))
                unit.attack(attackable_units[0])
                continue

        self.elves = [elf for elf in self.elves if elf.hp > 0]
        self.goblins = [goblin for goblin in self.goblins if goblin.hp > 0]

    def show(self, positions=[], char='@', hp=True):
        goblin_positions = [(goblin.r, goblin.c) for goblin in self.goblins]
        elf_positions = [(elf.r, elf.c) for elf in self.elves]
        all_units = self.elves + self.goblins
        all_units.sort(key=lambda x: (x.r, x.c))
        for r in range(self.R):
            for c in range(self.C):
                if (r, c) in positions:
                    print(char, end='')
                elif (r, c) in goblin_positions:
                    print('G', end='')
                elif (r, c) in elf_positions:
                    print('E', end='')
                else:
                    print(self.G[r][c], end='')
            if hp:
                print('   ', end='')
                for unit in all_units:
                    if unit.r == r:
                        print('{}({})'.format(unit.kind, unit.hp), end=', ')
            print()
        print()

    def show_hp(self):
        all_units = self.elves + self.goblins
        all_units.sort(key=lambda x: (x.r, x.c))
        for r in range(R):
            for unit in all_units:
                if unit.r == r:
                    print('{}({})'.format(unit.kind, unit.hp), end=', ')
            print()

def main():
    game = Game(G)
    print('Initially')
    game.show()
    t = 0
    # for t in range(1):
    while len(game.elves) > 0 and len(game.goblins) > 0:
        game.turn()
        t += 1
        game.time = t
        print(t)
        # if t % 1 == 0:
        #     print('After round: {}'.format(t))
        #     game.show()
    print('final')
    game.show()
    ft = t - 1
    print(ft)
    fhp = sum([g.hp for g in game.goblins] + [e.hp for e in game.elves])
    print('Outcome: {} * {} = {}'.format(ft, fhp, ft * fhp))


if __name__ == "__main__":
    main()