import sys
sys.path.append('..')
import my_parser as p
from functools import cmp_to_key


def create_counts(hand):
    return [hand.count(char) for char in hand]


def create_handset(hands, f):
    ranks = [[] for _ in range(7)]

    for i, hand in enumerate(hands):

        counts = f(hand)

        # 5 of a kind
        if 5 in counts:
            ranks[0].append(i)
            continue
        # 4 of a kind
        if 4 in counts:
            ranks[1].append(i)
            continue
        # Full house
        if 3 in counts and 2 in counts:
            ranks[2].append(i)
            continue
        # Three of a kind
        if 3 in counts:
            ranks[3].append(i)
            continue
        # Two pairs
        if counts.count(2) == 4:
            ranks[4].append(i)
            continue
        # One pair
        if 2 in counts:
            ranks[5].append(i)
            continue
        # High card
        ranks[6].append(i)

    return ranks


def compare_strings(string1, string2, kinds):
    for char1, char2 in zip(string1, string2):
        index1 = kinds.index(char1)
        index2 = kinds.index(char2)
        if index1 > index2:
            return 1  # string1 is greater
        elif index1 < index2:
            return -1  # string2 is greater
    return 0  # strings are equal


def calculate_score(ranks, hands, bids, kinds):
    sorted_ranks = []
    for rank in ranks:
        sorted_rank = sorted(rank, key=cmp_to_key(lambda x, y: compare_strings(hands[x], hands[y], kinds)))
        for i in sorted_rank:
            sorted_ranks.append(i)

    score = 0
    for i, rank in enumerate(sorted_ranks[::-1]):
        score += (i + 1) * bids[rank]

    print(score)


def part1():
    kinds = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    lines = p.input_as_lines('inputs/inp.txt')

    hands = [line.split()[0] for line in lines]
    bids = [int(line.split()[1]) for line in lines]

    handset = create_handset(hands, create_counts)
    calculate_score(handset, hands, bids, kinds)


def joker(hand):
    if hand == 'JJJJJ':
        return [5]
    jokers = hand.count('J')
    rest = [char for char in hand if char != 'J']
    counts = [rest.count(char) for char in rest]
    most_frequent_char = rest[counts.index(max(counts))]
    for _ in range(jokers):
        rest.append(most_frequent_char)

    counts = [rest.count(char) for char in rest]
    return counts


def part2():
    kinds = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    lines = p.input_as_lines('inputs/inp.txt')

    hands = [line.split()[0] for line in lines]
    bids = [int(line.split()[1]) for line in lines]

    handset = create_handset(hands, joker)
    calculate_score(handset, hands, bids, kinds)

part1()
part2()








