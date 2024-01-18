import sys
sys.path.append('..')
import my_parser as p

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

L = p.input_as_lines('inputs/inp.txt')[0]
L = L.split()
players, worth = int(L[0]), int(L[-2])


def solve(players, worth):
    current = Node(0)
    current.next = current.prev = current

    marbles = current
    scores = [0 for _ in range(players)]

    for marble in range(1, worth + 1):
        if marble % 23 != 0:
            new_marble = Node(marble)

            # Insert the new marble between the next and next-next nodes
            new_marble.next = current.next.next
            new_marble.prev = current.next
            current.next.next.prev = new_marble
            current.next.next = new_marble

            current = new_marble
        else:
            scores[(marble - 1) % players] += marble

            # Move back 7 steps in the linked list
            for _ in range(7):
                current = current.prev

            extra = current.value
            scores[(marble - 1) % players] += extra

            current.prev.next = current.next
            current.next.prev = current.prev

            current = current.next

    print(max(scores))


solve(players, worth)
solve(players, worth * 100)
