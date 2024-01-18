import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')[0]
L = [int(el) for el in L.split()]


def p1(nodes):
    # base case
    if nodes[0] == 0:
        return sum([nodes[i + 2] for i in range(nodes[1])]), 2 + nodes[1]

    # determine the values of the
    sum_children = 0
    md_start = 0
    for child in range(nodes[0]):
        sum_child, end = p1(nodes[2 + md_start:])
        sum_children += sum_child
        md_start += end

    # return the sum of the children + the sum of the metadata of the current
    # node and the end of the current node
    return sum_children + sum([nodes[md_start + 2 + i] for i in range(nodes[1])]), 2 + md_start + nodes[1]


print(p1(L)[0])


def p2(nodes):
    # base case
    if nodes[0] == 0:
        return sum([nodes[i + 2] for i in range(nodes[1])]), 2 + nodes[1]

    # Find the values of the child nodes
    md_start = 0
    children = []
    for child in range(nodes[0]):
        sum_child, end = p2(nodes[2 + md_start:])
        children.append(sum_child)
        md_start += end

    # Determine the chosen children based on the metadata of the current node
    chosen_children = []
    for child in nodes[md_start + 2: md_start + 2 + nodes[1]]:
        if child <= len(children):
            chosen_children.append(children[child - 1])

    # return the value of the current node and the end of the current node
    return sum(chosen_children), 2 + md_start + nodes[1]


print(p2(L)[0])
