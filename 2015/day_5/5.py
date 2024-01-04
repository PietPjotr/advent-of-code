import sys
sys.path.append('..')
import my_parser as p


def deel1(lines):
    evil = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'

    nice_lines = 0
    for line in lines:
        n_vowels = 0
        n_evil = 0
        double = 0
        for char in line:
            if char in vowels:
                n_vowels += 1

        for n in evil:
            if n in line:
                n_evil += 1
                break

        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                double += 1
                break

        if n_vowels >= 3 and n_evil == 0 and double > 0:
            nice_lines += 1

    print(nice_lines)


def deel2(lines):
    nice_lines = 0

    nice = []
    for line in lines:

        # check for the first condition: pair of letters that appears twice without overlapping
        n_grams = []
        n = 2
        cond1 = False
        cond2 = False

        # create all bi-grams
        for i in range(len(line) - n + 1):
            n_grams.append(line[i: i + n])

        for i, gram in enumerate(n_grams):
            if gram in n_grams[i + 2:]:
                cond1 = True
                break

        # checking for condition 2
        for i in range(1, len(n_grams) - 1):
            gram = n_grams[i]
            if gram[::-1] == n_grams[i + 1] or gram[::-1] == n_grams[i - 1]:
                cond2 = True
                break

        # if both conditions are true then the line is nice
        if cond1 and cond2:
            nice_lines += 1

    print(nice_lines)


def main():

    lines = p.input_as_lines('inputs/inp.txt')

    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()
