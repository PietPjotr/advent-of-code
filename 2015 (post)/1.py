import parser

def main():
    # lines = parser.input_as_lines('inputs/1.txt')
    # lines = parser.input_as_ints('inputs/1.txt')
    # lines = parser.input_as_grid('inputs/1.txt')
    lines = parser.input_as_string('inputs/1.txt')
    floor = 0
    for i, char in enumerate(lines):
        if char == '(':
            floor += 1

        elif char == ')':
            floor -= 1
            if floor < 0:
                print(i + 1)
                break
    print(floor)


if __name__ == "__main__":
    main()