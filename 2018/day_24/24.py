import sys
sys.path.append('..')
import my_parser as p
import re
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')
IS = L[1:11]
I = L[13:]

# IS = L[1:3]
# I = L[5:7]

class Group:
    def __init__(self, no_units, hp, weaknesses, immunities, dmg, attack_type, initiative):
        self.no_units = no_units
        self.hp = hp
        self.dmg = dmg
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.attack_type = attack_type
        self.initiative = initiative

    def __str__(self):
        return str(self.no_units) + ', ' + \
               str(self.hp) + ', ' + \
               str(self.weaknesses) + ', ' + \
               str(self.immunities) + ', ' + \
               str(self.dmg) + ', ' + \
               str(self.attack_type) + ', ' + \
               str(self.initiative)

    def __repr__(self):
        return str(self)


def parse(l, lines):
    for line in lines:
        no_units = int(re.findall(r'(\w+) units', line)[0])
        hp = int(re.findall(r'(\w+) hit points', line)[0])
        weaknesses = re.findall(r'weak to ([^;)]+)', line)
        immunities = re.findall(r'immune to ([^;)]+)', line)
        if weaknesses:
            weaknesses = weaknesses[0].split(', ')
        if immunities:
            immunities = immunities[0].split(', ')
        attack = re.findall(r'that does (\d+) (\w+) damage', line)[0]
        dmg = int(attack[0])
        attack_type = attack[1]
        initiative = int(re.findall(r'initiative (\d+)', line)[0])
        group = Group(no_units, hp, weaknesses, immunities, dmg, attack_type, initiative)
        l.append(group)


# create the different groups
immune_system = []
infection = []
parse(immune_system, IS)
parse(infection, I)

# give every group a separate id
og_immune_system = [(i, i_s) for i, i_s in enumerate(immune_system)]
og_infection = [(len(immune_system) + i, inf) for i, inf in enumerate(infection)]


def selection_func(source, target):
    id_source, source = source
    id_target, target = target
    effective_power = source.dmg * source.no_units
    deals = effective_power
    if source.attack_type in target.immunities:
        deals = 0
    elif source.attack_type in target.weaknesses:
        deals = 2 * effective_power
    # print('group {} would deal group {} {} damage'.format(id_source, id_target, deals))
    return (deals, target.no_units * target.dmg, target.initiative)


# could also be arranges differently: per army, but shouldn't really matter
def selection(immune_system, infection):
    selection_dict = {}
    all_units = immune_system + infection
    all_units.sort(key=lambda x: (x[1].dmg * x[1].no_units, x[1].initiative), reverse=True)
    for id_, unit in all_units:
        if unit.no_units <= 0:
            continue
        if (id_, unit) in immune_system:
            targets = infection
        else:
            targets = immune_system
        sorted_targets = sorted(targets, key=lambda x: selection_func((id_, unit), x), reverse=True)
        # remove already selected or dead targets or targets that are immune
        sorted_targets = [st for st in sorted_targets if st[0] not in set(selection_dict.values()) and st[1].no_units > 0]
        sorted_targets = [st for st in sorted_targets if unit.attack_type not in st[1].immunities]
        # no targets so we continue
        if not sorted_targets:
            continue
        selection_dict[id_] = sorted_targets[0][0]

    return selection_dict


def attack(immune_system, infection, selection_dict):
    all_units = immune_system + infection

    # remove the units that are dead
    all_units = [u for u in all_units if u[1].no_units > 0]
    # sort by initiative
    all_units.sort(key=lambda x: x[1].initiative, reverse=True)

    for id1, unit1 in all_units:
        if unit1.no_units <= 0:
            continue
        # no target so we continue
        if id1 not in selection_dict:
            continue
        target_id = selection_dict[id1]
        for id2, unit2 in all_units:
            # deal damage to the target
            if id2 == target_id:
                effective_power = unit1.no_units * unit1.dmg
                deals = effective_power
                if unit1.attack_type in unit2.weaknesses:
                    deals = 2 * effective_power
                unit2.no_units -= deals // unit2.hp


def turn(immune_system, infection):
    selection_dict = selection(immune_system, infection)
    attack(immune_system, infection, selection_dict)


for boost in range(0, 10000):
    immune_system = []
    for id_, el in og_immune_system:
        new_el = deepcopy(el)
        new_el.dmg += boost
        immune_system.append((id_, new_el))

    infection = deepcopy(og_infection)

    alive_imsy = [el for el in immune_system if el[1].no_units > 0]
    alive_inf = [el for el in infection if el[1].no_units > 0]

    no_all_units = sum([el[1].no_units for el in alive_imsy + alive_inf])
    skip = False

    while alive_imsy and alive_inf:
        turn(immune_system, infection)
        alive_imsy = [el for el in immune_system if el[1].no_units > 0]
        alive_inf = [el for el in infection if el[1].no_units > 0]
        if no_all_units == sum([el[1].no_units for el in alive_imsy + alive_inf]):
            skip = True
            break
        no_all_units = sum([el[1].no_units for el in alive_imsy + alive_inf])

    if skip:
        continue

    if boost == 0:
        print(no_all_units)

    if alive_imsy:
        print(sum([el[1].no_units for el in alive_imsy]))
        break

