import parser

def deel1(lines):
    total = 0
    # print(lines)
    for line in lines:
        total += eval1(line[0], line[-1])

    print(total)


def deel2(lines):
    total = 0
    # print(lines)
    for line in lines:
        total += eval2(line[0], line[-1])

    print(total)

"""
Evaluates the amount of points based on the given inputs a and b. A being the
expected play and x being the response according to the guide.
"""
def eval1(a, x):
    # start
    s = ['A', 'B', 'C']

    # response according to guide
    r = ['X', 'Y', 'Z']

    score = r.index(x) + 1

    # check beat or not
    for i in range(len(s)):
        if a == s[i]:
            # draw
            if x == r[i]:
                score += 3
            # beat
            elif x == r[(i + 1) % 3]:
                score += 6
            # lost
            else:
                score += 0

    return score


def eval2(a, x):
    # start
    s = ['A', 'B', 'C']

    # response according to guide
    r = ['X', 'Y', 'Z']

    score = r.index(x) * 3

    # check rock paper or scissors
    for i in range(len(s)):
        if x == r[i]:
            step = i - 1
            # calc the score of our pick
            i_s = (s.index(a) + step) % 3 + 1
            score += i_s

    return score


def main():
    # lines = parser.input_as_string('inputs/.txt')
    lines = parser.input_as_lines('inputs/dag2.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
    deel1(lines)
    deel2(lines)



if __name__ == "__main__":
    main()