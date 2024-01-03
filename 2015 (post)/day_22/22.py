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


def apply(player, boss, active):
    ids = [i for i, timer in active]

    # reset the player shield (this mistake took about 3 hours to find)
    player[2] = 0

    for spell_id, timer in active:
        cost, hp5, mp5, armor, dmg, _ = spells[spell_id]
        player[0] += hp5
        player[1] += mp5
        player[2] += armor

        boss[0] -= dmg

    # update and remove spells
    active = [(spell_id, timer - 1) for spell_id, timer in active]
    active = [(spell_id, timer) for spell_id, timer in active if timer > 0]

    return player, boss, active


def boss_attack(player, boss):
    php, pmp, parmor = player
    bhp, bdmg = boss
    php -= max(1, bdmg - parmor)
    return [php, pmp, parmor], boss


def solve(hardmode=False):
    base_player = [50, 500, 0]
    boss = [71, 10]

    min_mana = float('inf')
    min_casted = []
    player_stack = [(base_player, boss, [], 0)]
    while player_stack:
        boss_stack = []

        # players turn
        for frame in player_stack:
            player, boss, active, mana_spent = frame
            if hardmode:
                player[0] -= 1

            player, boss, active = apply(player, boss, active)

            if mana_spent > min_mana:
                continue

            # boss died
            if boss[0] <= 0:
                if mana_spent < min_mana:
                    min_mana = mana_spent
                continue

            # players turn: cast all possible spells and simulate
            active_spell_ids = [i for i, timer in active]
            for i in [0, 1, 2, 3, 4]:
                if i in active_spell_ids:
                    continue

                cost = spells[i][0]
                if cost > player[1]:
                    continue

                np, na = cast_spell(player, i, active)
                boss_stack.append((np, deepcopy(boss), na, mana_spent + cost))

            # not enough mana, player lost
            if not boss_stack:
                continue

        player_stack = []
        for frame in boss_stack:

            player, boss, active, mana_spent = frame

            player, boss, active = apply(player, boss, active)

            # boss died
            if boss[0] <= 0:
                if mana_spent <= min_mana:
                    min_mana = mana_spent
                continue

            player, boss = boss_attack(player, boss)

            # player died
            if player[0] <= 0:
                continue

            player_stack.append((player, boss, active, mana_spent))

    return min_mana


print(solve())
print(solve(True))
