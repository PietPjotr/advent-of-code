import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')


def p1():
    two = 0
    three = 0
    for el in L:
        el = [(char, el.count(char)) for char in el]
        Two = True
        Three = True
        for char, c in el:
            if c == 3 and Three:
                three += 1
                Three = False
            if c == 2 and Two:
                two += 1
                Two = False

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
