from copy import deepcopy

#        c, hp5+ mp5+, ar, d, timer
spells = [[53,  0, 0,   0, 4, 1],
          [73,  2, 0,   0, 2, 1],
          [113, 0, 0,   7, 0, 6],
          [173, 0, 0,   0, 3, 6],
          [229, 0, 101, 0, 0, 5],
]

spell_names = ['Magic Missile', 'Drain', 'Shield', 'Poison', 'Recharge']


def cast_spell(player, spell_id, active):
    spell = spells[spell_id]

    ret_active = deepcopy(active)
    ret_player = deepcopy(player)

    ret_active.append((spell_id, spell[-1]))
    ret_player[1] -= spell[0]

    return ret_player, ret_active


def apply(player, boss, active, turn=''):
    for spell_id, timer in active:
        stats = spells[spell_id]
        player[0] += stats[1]
        player[1] += stats[2]
        if player[2] == 0:
            player[2] += stats[3]

        boss[0] -= stats[4]
        timer -= 1

    active = [(spell_id, timer - 1) for spell_id, timer in active]
    active = [spell for spell in active if spell[-1] > 0]

    return player, boss, active


def boss_attack(player, boss):
    player[0] -= max(1, boss[1] - player[2])
    return player, boss


def solve():
    base_player = [50, 500, 0]
    boss = [71, 10]

    base_player = [10, 250, 0]
    boss = [13, 8]

    min_mana = float('inf')
    min_casted = []
    player_stack = [(base_player, boss, [], 0, [])]
    while player_stack:
        boss_stack = []

        # players turn
        for i, frame in enumerate(player_stack):
            player, boss, active, mana_spent, casted = frame

            player, boss, active = apply(player, boss, active)

            if mana_spent > min_mana:
                continue

            # boss died
            if boss[0] <= 0:
                if mana_spent < min_mana:
                    min_mana = mana_spent
                    min_casted = deepcopy(casted)
                    print(min_mana)
                continue

            # players turn: cast all possible spells and simulate
            ids = [i for i, timer in active]
            for i in range(len(spells)):
                if i in ids:
                    continue
                cost = spells[i][0]
                if cost > player[1]:
                    continue

                np, na = cast_spell(player, i, active)
                boss_stack.append((np, deepcopy(boss), na, mana_spent + cost, casted + [i]))

            # not enough mana, player lost
            if not boss_stack:
                continue

        player_stack = []
        for i, frame in enumerate(boss_stack):

            player, boss, active, mana_spent, casted = frame

            player, boss, active = apply(player, boss, active)

            # boss died
            if boss[0] <= 0:
                if mana_spent < min_mana:
                    min_mana = mana_spent
                    min_casted = deepcopy(casted)
                    print(min_mana)
                continue

            player, boss = boss_attack(player, boss)

            # player died
            if player[0] <= 0:
                continue

            player_stack.append((player, boss, active, mana_spent, casted))

    return min_mana, casted

res, casted = solve()
print([spell_names[i] for i in casted])
spells_names = [spell_names[i] for i in casted]
print(sum([spells[spell][0] for spell in casted]))

casted_small = ['Poison', 'Magic Missile']
print(sum([spells[spell_names.index(spell)][0] for spell in casted_small]))
