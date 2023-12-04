import sys
sys.path.append('..')
import my_parser as p
import re


def part1():
    lines = p.input_as_lines('inputs/inp.txt')

    scores = []

    for line in lines:
        # filter out only the numbers
        first = line[line.find(':') + 2: line.find('|')]
        second = line[line.find('|') + 2:]

        # extact the numbers as ints
        winning = [int(num) for num in (re.findall(r'\d+', first))]
        our = [int(num) for num in (re.findall(r'\d+', second))]

        score = 0

        # calculate the score of every card
        for num in our:
            if num in winning:
                if score == 0:
                    score = 1
                else:
                    score = score * 2

        scores.append(score)

    print(sum(scores))


def part2():
    lines = p.input_as_lines('inputs/inp.txt')

    cards = [1] * len(lines)

    for i, line in enumerate(lines):
        # filter out only the numbers
        first = line[line.find(':') + 2: line.find('|')]
        second = line[line.find('|') + 2:]

        # extact the numbers as ints
        winning = [int(num) for num in (re.findall(r'\d+', first))]
        our = [int(num) for num in (re.findall(r'\d+', second))]

        current_cards = cards[i]

        # calculate the score of every card
        wins = 0
        for num in our:
            if num in winning:
                wins += 1

        # add the consecutive cards that we won for every card
        for j in range(i + 1, i + wins + 1):
            if j < len(cards):
                cards[j] += current_cards

    print(sum(cards))

part1()
part2()




