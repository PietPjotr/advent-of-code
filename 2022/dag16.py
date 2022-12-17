import parser
import copy
from collections import deque
import heapq
import numpy as np

def deel1(lines):
    pass

def deel2(lines):
    pass

class Frame:
    def __init__(self, i, value, fro, cur, opened, path):
        self.remaining = i
        self.value = value
        self.fro = fro
        self.cur = cur
        self.opened = opened
        self.path = path

    def __repr__(self):
        return f'Frame(i: {self.remaining}, v: {self.value}, f:{self.fro}, c:{self.cur}, o:{self.opened}, p:{self.path})'

    def __iter__(self):
        return iter((self.remaining, self.value, self.fro, self.cur, self.opened, self.path))


def recursive(nodes, minutes, value, fro, cur, opened, path, maximum):
    # print('iteration')
    # print all the values
    print(minutes, value, fro, cur, opened, path, maximum)
    if minutes == 0:
        print('used all the minutes')
        return value, path

    # we make sure that we do not go back to where we came from without doing anything. This will not result in a
    # higher value
    neighs = nodes[cur][1]
    if fro in neighs:
        neighs.remove(fro)

    # we add the opening of the current node as a neighbor
    if cur not in opened:
        neighs.append(cur)

    # we try all the neighbours, which always costs 1 minute (either walking or opening)
    new_opened = copy.deepcopy(opened)
    for neigh in neighs:
        # if the neighbor is the current node, we will open the valve and add the score for the next stack frame
        if neigh == cur:
            delta_score = int(nodes[cur][0]) * minutes
            new_opened.add(cur)
        else:
            delta_score = 0

        new_path = copy.deepcopy(path)
        new_path.append(neigh)
        total_score = value + delta_score
        maximum = max(total_score, maximum)

        # we add the new node to the stack
        recursive(nodes, minutes - 1, total_score, cur, neigh, new_opened, new_path, maximum)

    return value, path

def main():
    lines = parser.input_as_lines('inputs/dag16.txt')
    lines = parser.input_as_lines('inputs/dag16_test.txt')
    nodes = {}
    for line in lines:
        line = line.split(' ')
        node = line[1]
        value = int(line[4][5:-1])
        neighss = line[9:]
        neighs = []
        for neigh in neighss:
            if ',' in neigh:
                neigh = neigh[:-1]
            neighs.append(neigh)
        neighs.append(node)

        nodes[node] = [value, neighs]

    minutes = 30
    start_node = list(nodes.keys())[0]  # 'AA'
    start_frame = Frame(minutes, 0, None, start_node, set(), [])
    stack = [start_frame]
    maximum = 0
    its = 0
    while stack:
    # for i in range(30):
        current_frame = stack.pop()
        i, current_score, fro, cur, opened, path = current_frame
        neighss = nodes[cur][1]
        # print('current frame, neighs', current_frame, neighss)
        # print(nodes, cur)

        new_path = copy.deepcopy(path)
        new_path.append(cur)

        if i == 0:
            if current_score > maximum:
                maximum = current_score
                final_path = path
                print(maximum)
            continue

        neighs = copy.deepcopy(nodes[cur][1])
        if fro in neighs:
            neighs.remove(fro)

        # we try all the neighbours, which always costs 1 minute (either walking or opening)
        new_opened = copy.deepcopy(opened)
        i -= 1
        for neigh in neighs:
            # if the neighbor is the current node, we will open the valve and calculate the resulting score
            if neigh == cur and neigh not in opened:
                delta_score = nodes[neigh][0] * i
                new_opened.add(neigh)
            else:
                delta_score = 0

            new_score = current_score + delta_score

            # we add the new node to the stack
            new_frame = Frame(i, new_score, cur, neigh, new_opened, new_path)
            stack.append(new_frame)
            def key(x):
                return x.value + x.remaining * 140
            stack.sort(key=key)
            while len(stack) > 700:
                stack.pop(0)

        its += 1
        if its % 100 == 0:
            print(its, maximum)

    print(maximum)
    print(final_path)
    print(len(final_path))



if __name__ == "__main__":
    main()