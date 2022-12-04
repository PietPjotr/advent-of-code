import parser

def iterate(num, n):

    for i in range(n):
        nex = (num * 252533) % 33554393
        num = nex

    return nex




def deel1(lines):
    r = 2947
    c = 3029

    # for some reason the formula i made gets the row of one larger and the
    # column of one lower so this was a good hack to fix it xD
    r = r + 1
    c = c - 1

    nth = int(c / 2 * (1 + c) + (r - 1) / 2 * (c + r - 2 + c))
    nth_number = iterate(20151125, nth)
    print(nth_number)

def deel2(lines):
    pass

def main():
    # lines = parser.input_as_string('inputs/25.txt')
    # lines = parser.input_as_lines('inputs/25.txt')
    # lines = parser.input_as_ints('inputs/25.txt')
    lines = parser.input_as_lines('inputs/25.txt')
    lines_a = [[int(x) for x in line.split()] for line in lines]
    lines = lines_a
    deel1(lines)

if __name__ == "__main__":
    main()