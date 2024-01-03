import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

# hp, mana, armor
player = [50, 500, 0]
# hp, damage
boss = [71, 10]

#        c, hp5+ mp5+, ar, d, timer
spells = [[53,  0, 0,   0, 4, 1],
          [73,  2, 0,   0, 2, 1],
          [113, 0, 0,   7, 0, 6],
          [173, 0, 0,   0, 3, 6],
          [229, 0, 101, 0, 0, 5],
]


def cast_spell(player, spell_id, active_player, active_boss):
    spell = spells[spell_id]
    player[1] -= spell[0]
    if spell_id == 0:
        active_boss.append([4, 1])
    elif spell_id == 1:
        active_player.append([2, 0, 0, 1])
        active_boss.append([2, 1])
    elif spell_id == 2:
        active_player.append([0, 0, 7, 6])
    elif spell_id == 3:
        active_boss.append([3, 6])
    elif spell_id == 4:
        active_player.append([0, 101, 0, 5])

    return player, active_player, active_boss


def turn(player, boss, active_player, active_boss):
    # spells on player take effect
    for spell in active_player:
        player[0] += spell[0]
        player[1] += spell[1]
        player[2] += spell[2]
        spell[3] -= 1
    active_player = [spell for spell in active_player if spell[-1] > 0]

    # spells on boss take effect
    for spell in active_boss:
        boss[0] -= spell[0]
        spell[1] -= 1
    active_boss = [spell for spell in active_boss if spell[-1] > 0]

    # boss damages player
    player[0] -= max(1, boss[1] - player[2])

    # reset the armor to 0
    player[2] = 0

    print('spells on player: ', active_player, 'spells on boss: ', active_boss)
    return player, boss, active_player, active_boss


def solve():
    # hp, mana, armor
    base_player = [50, 500, 0]
    # hp, damage
    boss = [71, 10]

    min_mana = float('inf')
    stack = []
    for i in range(len(spells)):
        player, active_player, active_boss = cast_spell(deepcopy(base_player), i, [], [])
        stack.append([player, deepcopy(boss), active_player, active_boss, spells[i][0]])

    while stack:
        player, boss, active_player, active_boss, mana_spent = stack.pop(0)
        print('stack: ')
        print(player, boss, mana_spent)
        player, boss, active_player, active_boss = turn(player, boss, active_player, active_boss)
        print(player, boss, mana_spent)
        print()
        # boss died
        if boss[0] <= 0:
            if mana_spent < min_mana:
                min_mana = mana_spent
            continue
        # player died
        elif player[0] <= 0:
            continue

        # cast all possible spells and simulate
        for i in range(len(spells)):
            cost = spells[i][0]
            if cost > player[1]:
                continue
            p = deepcopy(player)
            ap = deepcopy(active_player)
            ab = deepcopy(active_boss)
            nplayer, nactive_player, nactive_boss = cast_spell(p, i, ap, ab)
            stack.append((nplayer, boss, nactive_player, nactive_boss, mana_spent + cost))

    return min_mana


res = solve()
print(res)

