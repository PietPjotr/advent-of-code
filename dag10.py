from typing import List
import threading, queue


def input_as_string(filename: str) -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")


def input_as_lines(filename: str) -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")


def input_as_ints(filename: str) -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    def line_as_int(l): return int(l.rstrip('\n'))
    return list(map(line_as_int, lines))


def input_as_grid(lines, row):
    grids = []
    for y in range(0, int(len(lines) / (row + 1) + 1) - 1):
        grid = []
        for x in range((row + 1) * y + 1, (row + 1) * y + row + 1):
            grid.append([int(z) for z in lines[x].split()])
        grids.append(grid)

    return grids


def deel1():

    lines = input_as_lines('dag10_input.txt')
    start = ['(', '[', '{', '<']
    end = [')', ']', '}', '>']
    values = [3,57,1197,25137]

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
                    ill.append(values[end.index(char)])
                    break

    print(sum(ill))


def deel2():
    lines = input_as_lines('dag10_input.txt')

    breaker = False
    ill = []
    line_n = 0
    missing = []
    for line in lines:
        s = []
        line_n += 1
        mis = ''
        for i, char in enumerate(line):
            if char == '(' or char == '{' or char == '[' or char == '<':
                s.append(char)
                if i == len(line) - 1:
                    print(s)
                    length = len(s)
                    for i in range(length):
                        char = s.pop()
                        if char == '(':
                            mis += ')'
                        elif char == '[':
                            mis += ']'
                        elif char == '{':
                            mis += '}'
                        elif char == '<':
                            mis += '>'
                    missing.append(mis)

            elif char == ')' or char == '}' or char ==']' or char =='>':
                top = s.pop()
                if (top == '(' and char == ')') or (top == '[' and char == ']') or (top == '{' and char == '}') or (top == '<' and char == '>'):

                    if i == len(line) - 1:
                        length = len(s)
                        for i in range(length):
                            char = s.pop()
                            if char == '(':
                                mis += ')'
                            elif char == '[':
                                mis += ']'
                            elif char == '{':
                                mis += '}'
                            elif char == '<':
                                mis += '>'
                        missing.append(mis)
                    continue
                else:
                    ill.append(char)
                    break

    answers = []
    for line in missing:
        answer = 0
        for char in line:
            if char == ')':
                answer *= 5
                answer += 1
            elif char == ']':
                answer *= 5
                answer += 2
            elif char == '}':
                answer *= 5
                answer += 3
            elif char == '>':
                answer *= 5
                answer += 4
        answers.append(answer)
    s_answers = sorted(answers, reverse=False)
    print(s_answers[int(len(answers) / 2)])

deel1()