import parser


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

    for line in lines:
        line = line.strip()
        double = 0
        double_string = 0

        for j in range(len(line) - 1):
            string = line[j] + line[j+1]
            string2 = line[j+1] + line[j]
            # print(string, line, line[0:j] + line[j+2:])
            if string in (line[0:j] + line[j+2:]):
                double_string += 1
                break

        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                double += 1
                break

        # print(double, double_string)
        if double > 0 and double_string > 0:
            nice_lines += 1

    print(nice_lines)


def main():
    # lines = parser.input_as_string('inputs/.txt')
    lines = parser.input_as_lines('inputs/5.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    # lines = ['qjhvhtzxzqqjkmpb']
    # lines = ['aaaa']
    # deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()
