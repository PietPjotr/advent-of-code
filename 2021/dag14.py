import parser
import copy


def deel1(header, translations):
    iterations = 10
    for x in range(iterations):
        new = ''
        new += header[0]
        for i in range(len(header) - 1):
            new += translations[header[i] + header[i + 1]]
            new += header[i + 1]

        header = new

    counts = []
    for key, value in translations.items():
        counts.append(header.count(value))

    s = sorted(counts, reverse=False)
    print(s)
    print(s[-1] - s[0])


def deel2(header, translations):
    # creating a pairs dict containing all the pairs and initialising it with
    # the letters/pairs in the header.
    pairs = translations.copy()
    for key, value in pairs.items():
        pairs[key] = 0
    reset = pairs.copy()

    for i in range(len(header) - 1):
        pairs[header[i] + header[i + 1]] += 1

    # initialise the letters with the letter of the header.
    letters = {}
    for key, _ in translations.items():
        if key[0] not in letters:
            letters[key[0]] = 0
        if key[1] not in letters:
            letters[key[1]] = 0
    for letter in header:
        letters[letter] += 1


    iterations = 40
    for x in range(iterations):
        # used to copy over all the new pairs in the current iteration.
        init = reset.copy()
        for key, value in pairs.items():
            # a new iteration creates 2 new pairs of amount 'value' of previous
            # iteration.
            init[key[0] + translations[key]] += value
            init[translations[key] + key[1]] += value

            # keeps track of all the new letters.
            letters[translations[key]] += value

        pairs = init.copy()

    print(letters)
    
    counts = [value for _, value in letters.items()]
    s = sorted(counts, reverse=False)
    print(s[-1] - s[0])


def main():
    # lines = parser.input_as_string('inputs/dag14.txt')
    lines = parser.input_as_lines('inputs/dag14.txt')
    # lines = parser.input_as_ints('inputs/ag14.txt')
    # lines = parser.input_as_grid('inputs/dag14.txt')
    header = lines[0]
    translations = {}
    for line in lines[2:]:
        split = line.split(' -> ')
        translations[split[0]] = split[1]

    deel2(header, translations)


if __name__ == "__main__":
    main()
