import parser

def convert(s):
    if s.islower():
        return ord(s) - 96
    elif s.isupper():
        return ord(s) - 64 + 26

def deel1(lines):
    # lines = parser.input_as_string('inputs/.txt')
    lines = parser.input_as_lines('inputs/dag3.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    # deel1(lines)
    total = 0
    for line in lines:
        first = line[0: int(len(line) / 2)]
        second = line[int(len(line) / 2):]
        match = list(set(first).intersection(second))[0]
        print(convert(match), match)
        total += convert(match)

    print(total)


def deel2(lines):
    pass


def main():
    # lines = parser.input_as_string('inputs/.txt')
    lines = parser.input_as_lines('inputs/dag3.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    # deel1(lines)
    total = 0
    i = 0
    while i < len(lines):
        group = lines[i:i + 3]
        # print(group)

        i += 3
        [first, second, third] = group

        match = list((set(first).intersection(second).intersection(third)))[0]
        print(convert(match), match)
        total += convert(match)

    print(total)





if __name__ == "__main__":
    main()