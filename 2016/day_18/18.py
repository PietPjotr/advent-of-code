import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

unsafe = set(['^^.', '.^^', '^..', '..^'])

def solve(rows):
    for i in range(rows - 1):
        prev = L[-1]
        new = ''
        padded = '.' + prev + '.'
        for i in range(len(prev)):
            window = padded[i:i+3]
            if window in unsafe:
                new += '^'
            else:
                new += '.'

        L.append(new)

    p1 = 0
    for row in L:
        for el in row:
            if el == '.':
                p1 += 1

    print(p1)


solve(40)
solve(400000)
