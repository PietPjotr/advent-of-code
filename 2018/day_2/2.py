import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')


def p1():
    two = 0
    three = 0
    for el in L:
        counts = set([el.count(x) for x in el])
        if 3 in counts:
            three += 1
        if 2 in counts:
            two += 1
    return three * two


def p2():
    for i, el1 in enumerate(L):
        for el2 in L[i+1:]:
            same = 0
            for k in range(len(el1)):
                if el1[k] == el2[k]:
                    same += 1

            if same == len(el1) - 1:
                ret = ''
                for i in range(len(el1)):
                    if el1[i] == el2[i]:
                        ret += el1[i]
                return ret


print(p1())
print(p2())
