import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

weapons = [[8, 4, 0],
           [10, 5, 0],
           [25, 6, 0],
           [40, 7, 0],
           [74, 8, 0]]

armors = [[0, 0, 0],
          [13, 0, 1],
          [31, 0, 2],
          [53, 0, 3],
          [75, 0, 4],
          [102, 0, 5]]

rings = [[0, 0, 0],
         [0, 0, 0],
         [25, 1, 0],
         [50, 2, 0],
         [100, 3, 0],
         [20, 0, 1],
         [40, 0, 2],
         [80, 0, 3]]


def win(player, boss):
    turns = 1
    while True:
        boss[0] -= max(1, player[1] - boss[2])
        if boss[0] <= 0:
            return True
        player[0] -= max(1, boss[1] - player[2])
        if player[0] <= 0:
            return False
        turns += 1


def add_stats(player, weapon, armor, ring1, ring2):
    player[1] += weapon[1] + ring1[1] + ring2[1]
    player[2] += armor[2] + ring1[2] + ring2[2]
    return player


# hp, damage, armor
base_player = [100, 0, 0]
base_boss = [103, 9, 2]
# try all combinations and see if we beat the boss
ma = 0
mi = float('inf')
for weapon in weapons:
    for armor in armors:
        for i, ring1 in enumerate(rings):
            for ring2 in rings[i+1:]:
                cost = weapon[0] + armor[0] + ring1[0] + ring2[0]

                player = add_stats(deepcopy(base_player), weapon, armor, ring1, ring2)
                if win(player, deepcopy(base_boss)) and cost < mi:
                    mi = cost

                player = add_stats(deepcopy(base_player), weapon, armor, ring1, ring2)
                if not win(player, deepcopy(base_boss)) and cost > ma:
                    ma = cost

print(mi)
print(ma)
