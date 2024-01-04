import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/test.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

inp = '1113122113'

def print_length(inp, steps):
    for i in range(steps):
        new = ''
        cur = inp[0]
        for el in inp[1:]:
            if el != cur[0]:
                new += str(len(cur)) + cur[0]
                cur = el
            else:
                cur += el

        new += str(len(cur)) + cur[0]
        inp = new
    print(len(inp))


print_length(inp, 40)
print_length(inp, 50)