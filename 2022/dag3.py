import parser

def convert(s):
    if s.islower():
        return ord(s) - 96
    elif s.isupper():
        return ord(s) - 64 + 26

def deel1(lines):
    total = 0
    for line in lines:
        first = line[0: int(len(line) / 2)]
        second = line[int(len(line) / 2):]
        match = list(set(first).intersection(second))[0]
        total += convert(match)

    print(total)

def deel2(lines):
    total = 0
    i = 0
    while i < len(lines):
        group = lines[i:i + 3]

        i += 3
        [first, second, third] = group
        match = list((set(first).intersection(second).intersection(third)))[0]
        total += convert(match)

    print(total)


def main():
    lines = parser.input_as_lines('inputs/dag3.txt')
    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()