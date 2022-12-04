import parser

def deel1(lines):
    pass

def deel2(lines):
    pass


def main():
    # lines = parser.input_as_string('inputs/dag1_input.txt')

    lines = parser.input_as_lines('inputs/dag1_input.txt')
    # lines = parser.input_as_ints('inputs/dag1_input.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt', split_on='')
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




if __name__ == "__main__":
    main()