import sys
sys.path.append('..')
import my_parser as p
import re


lines = p.input_as_lines('inputs/inp.txt')


def p1(lines):
    chars = []
    our_chars = []
    for line in lines:
        chars.append(len(line))
        inner = line[1:-1]
        res = re.findall(r'(\\{2}|\\\"|\\x[0-9a-f]{2}|[a-z])', inner)

        our_chars.append(len(res))

    res = sum(chars) - sum(our_chars)
    print(res)


def p2(lines):
    special_seqs = [r'\\', r'\"']
    new_strings = []
    for line in lines:
        new_string = ''
        for i in range(len(line)):
            cur = line[i:min(i+4, len(line))]
            matched = False
            for j, seq in enumerate(special_seqs):
                matchh = re.match(seq, cur)
                if matchh:
                    matched = True
                    if j == 0:
                        new_string += r'\\'
                    elif j == 1:
                        new_string += r'\"'
                    elif j == 2:
                        new_string += r'{}'.format(cur[1:])
            if not matched:
                new_string += line[i]

        new_strings.append('"{}"'.format(new_string))

    len_big = [len(st) for st in new_strings]
    len_small = [len(st) for st in lines]
    print(sum(len_big) - sum(len_small))


p1(lines)
p2(lines)
