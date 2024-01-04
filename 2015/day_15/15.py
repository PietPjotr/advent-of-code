import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
ingredients = []

for line in L:
    scores = []
    line = line.split(' ')
    for i, el in enumerate(line):
        if i == 0:
            continue
        if i % 2 == 0:
            el = el.replace(',', ' ')
            scores.append(int(el))

    ingredients.append(scores)


def calc_score(freqs, part):
    score = 1
    if part == 2:
        calories = sum([ingredients[j][-1] * freqs[j] for j in range(len(ingredients))])
        if calories != 500:
            return 0
    for i in range(len(ingredients[0]) - 1):
        cur = sum([ingredients[j][i] * freqs[j] for j in range(len(ingredients))])
        if cur < 0:
            cur = 0
        score *= cur
    return score


def solve(part):
    pool = 101
    highest = 0
    for i in range(1, pool):
        for j in range(pool - i):
            for k in range(pool - i - j):
                for l in range(pool - i - j - k):
                    freqs = [i, j, k, l]
                    if sum(freqs) == 100:
                        score = calc_score(freqs, part)
                        if score > highest:
                            highest = score

    print(highest)

solve(1)
solve(2)