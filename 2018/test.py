from collections import deque
import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')[0]
L = L.split()
players, worth = int(L[0]), int(L[-2])


def solve(players, worth):
    scores = [0 for _ in range(players)]
    circle = deque([0])

    for marble in range(1, worth + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[(marble - 1) % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores)


print(solve(players, worth))
print(solve(players, worth * 100))
