import parser

def deel1(lines):
    overlap = 0
    for line in lines:
        [one, two] = line.split(',')
        [a, b] = one.split('-')
        [c, d] = two.split('-')

        if (int(a) >= int(c) and int(b) <= int(d)) or (int(c) >= int(a) and int(d) <= int(b)):
            overlap += 1

    print(overlap)

def deel2(lines):
    overlap = 0
    for line in lines:
        [one, two] = line.split(',')
        [a, b] = one.split('-')
        [c, d] = two.split('-')

        range1 = range(int(a), int(b)+1)
        range2 = range(int(c), int(d)+1)

        for i in range1:
            if i in range2:
                overlap += 1
                break

    print(overlap)


def main():
    # lines = parser.input_as_string('inputs/.txt')
    lines = parser.input_as_lines('inputs/dag4.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    deel1(lines)
    deel2(lines)



if __name__ == "__main__":
    main()