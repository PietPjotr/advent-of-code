import parser

def deel1():

    lines = parser.input_as_lines('dag10_input.txt')

    start = ['(', '[', '{', '<']
    end = [')', ']', '}', '>']

    ill = []
    for line in lines:
        s = []

        for char in line:
            if char in start:
                s.append(char)
            else:
                top = s.pop()
                if start.index(top) == end.index(char):
                    continue
                else:
                    ill.append(char)
                    break
    answer = 0
    for char in ill:
        if char == end[0]:
            answer += 3
        elif char == end[1]:
            answer += 57
        elif char == end[2]:
            answer += 1197
        elif char == end[3]:
            answer += 25137
    print(answer)

deel1()