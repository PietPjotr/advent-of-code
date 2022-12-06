import parser

def deel1(lines):
    line = lines[0]
    i = 4
    four = list(line[0:i])

    if len(set(four)) == len(four):
        print(i)

    for el in line[i:]:
        four.pop(0)
        four.append(el)
        i += 1
        if len(set(four)) == len(four):
            break

    print(i)

def deel2(lines):
    line = lines[0]
    i = 14
    four = list(line[0:i])

    if len(set(four)) == len(four):
        print(i)

    for el in line[i:]:
        four.pop(0)
        four.append(el)
        i += 1
        if len(set(four)) == len(four):
            break

    print(i)

def main():
    lines = parser.input_as_lines('inputs/dag6.txt')
    # lines = parser.input_as_lines('inputs/dag6_test.txt')

    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()