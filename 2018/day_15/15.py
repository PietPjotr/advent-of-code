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
    def __init__(self, kind, pos, dmg=3):
        self.kind = kind
        self.r = pos[0]
        self.c = pos[1]
        self.hp = 200
        self.dmg = dmg

    def attack(self, target):
        target.hp -= self.dmg

    def move(self, pos):
        nr, nc = pos
        self.r = nr
        self.c = nc

    def get_neighbours(self):
        return [(self.r - dr, self.c - dc) for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]]

    def __str__(self):
        return str((self.kind, (self.r, self.c), self.hp, self.dmg))

    def __repr__(self):
        return str(self)


class Game:
    def __init__(self, grid, attack_power=3):
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
                    elves.append(Unit('E', (r, c), attack_power))
                    self.G[r][c] = '.'

        self.goblins = goblins
        self.elves = elves

    def find_targets(self, unit):
        target_list = self.find_target_list(unit)
        all_positions = self.find_used_positions()
        all_positions.remove((unit.r, unit.c))
        target_positions = []
        for target in target_list:
            if target.hp <= 0:
                continue
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr = target.r + dr
                nc = target.c + dc
                if self.G[nr][nc] == '.' and (nr, nc) not in all_positions:
                    target_positions.append((nr, nc))
        return set(target_positions)

    def find_closest_position(self, unit):
        used_positions = self.find_used_positions()
        queue = deque([(0, unit.r, unit.c)])
        target_positions = self.find_targets(unit)
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

        if positions:
            positions.sort(key=lambda x: (x[0], x[1]))
            distance = min([pos[0] for pos in positions])
            closest_positions = [pos[1] for pos in positions if pos[0] == distance]
            return distance, closest_positions[0]
        return (-1, None)

    # bfs distance matrix from the closest target position
    def find_next_position(self, unit):
        used_positions = self.find_used_positions()
        target_positions = self.find_targets(unit)
        _, closest_position = self.find_closest_position(unit)
        if not closest_position:
            return
        distances = {(closest_position[0], closest_position[1]): 0}
        queue = deque([(0, closest_position[0], closest_position[1])])
        while queue:
            steps, r, c = queue.popleft()
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in distances and self.G[nr][nc] == '.' and (nr, nc) not in used_positions:
                    distances[(nr, nc)] = steps + 1
                    queue.append((steps + 1, nr, nc))

        neighs = unit.get_neighbours()
        neighs = [neigh for neigh in neighs if neigh in distances]
        neighs.sort(key=lambda neigh: (distances[neigh], *neigh))
        return neighs[0]

    def find_used_positions(self):
        goblin_positions = [(goblin.r, goblin.c) for goblin in self.goblins if goblin.hp > 0]
        elf_positions = [(elf.r, elf.c) for elf in self.elves if elf.hp > 0]
        return goblin_positions + elf_positions

    def find_target_list(self, unit):
        neighs = []
        if unit.kind == 'E':
            target_list = self.goblins
        elif unit.kind == 'G':
            target_list = self.elves
        return [un for un in target_list if un.hp > 0]

    def turn(self):
        dps = True
        all_units = self.elves + self.goblins
        all_units.sort(key=lambda x: (x.r, x.c))
        for n, unit in enumerate(all_units):
            if unit.hp <= 0:
                continue

            target_list = self.find_target_list(unit)
            if not target_list:
                self.elves = [elf for elf in self.elves if elf.hp > 0]
                self.goblins = [goblin for goblin in self.goblins if goblin.hp > 0]
                return 'done'

            # check if we can attack
            if any([(enemy.r, enemy.c) in unit.get_neighbours() for enemy in target_list if enemy.hp > 0]):
                neighs = unit.get_neighbours()
                attackable_units = [enemy for enemy in target_list if (enemy.r, enemy.c) in neighs and enemy.hp > 0]
                if not attackable_units:
                    continue
                attackable_units.sort(key=lambda x: (x.hp, x.r, x.c))
                unit.attack(attackable_units[0])
                continue

            next_position = self.find_next_position(unit)
            if not next_position:
                continue
            unit.move(next_position)

            # again find if we can attack
            if any([(enemy.r, enemy.c) in unit.get_neighbours() for enemy in target_list if enemy.hp > 0]):
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
                        print('{}'.format(unit.hp), end=' ')
            print()
        print()


def p1():
    game = Game(deepcopy(G))
    t = 0
    while True:
        completed_turns =  game.turn()
        if completed_turns:
            break
        t += 1

    final_hp = sum([g.hp for g in game.goblins if g.hp] + [e.hp for e in game.elves])
    print(final_hp * t)


def p2():
    attack_power = 4
    while True:
        game = Game(deepcopy(G), attack_power)
        no_elves = len(game.elves)
        t = 0
        while True:
            done = game.turn()
            if done:
                break
            t += 1

        if len(game.elves) == no_elves:
            final_hp = sum([g.hp for g in game.goblins if g.hp] + [e.hp for e in game.elves])
            print(final_hp * t)
            break
        attack_power += 1


def main():
    p1()
    p2()


if __name__ == "__main__":
    main()