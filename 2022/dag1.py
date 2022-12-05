import parser

def deel1(lines):
    cur = 0
    most = 0
    for i in range(len(lines)):
        if lines[i] != '':
            cur += int(lines[i])
        elif cur > most:
            most = cur
            cur = 0
        else:
            cur = 0
    print(most)

def deel2(lines):
    cur = 0
    most3 = [0, 0, 0]
    for i in range(len(lines)):
        if lines[i] != '':
            cur += int(lines[i])
        elif cur > min(most3):
            most3[most3.index(min(most3))] = cur
            cur = 0
        else:
            cur = 0

    print(sum(most3))


def main():
    lines = parser.input_as_lines('inputs/dag1.txt')
    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()