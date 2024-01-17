import sys
sys.path.append('..')
import my_parser as p
from copy import deepcopy

L = p.input_as_lines('inputs/inp.txt')[0]

def reduce(L, char_to_remove=''):
    L = L.replace(char_to_remove.upper(), '')
    L = L.replace(char_to_remove.lower(), '')
    while True:
        j = 0
        start_length = len(L)
        while j < len(L) - 1:
            window = L[j: j + 2]
            if window[0] != window[1] and window[0].lower() == window[1].lower():
                L = L[:j] + L[j + 2:]
                j -= 2
            j = max(0, j + 1)  # ensures we don't accidentally go back to the end
        if len(L) == start_length:
            break

    return len(L)


print(reduce(deepcopy(L)))

p2 = float('inf')
for char in 'abcdefghijklmnopqrstuvwxyz':
    p2 = min(p2, reduce(deepcopy(L), char))

print(p2)
