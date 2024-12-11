import sys
sys.path.append('..')
import my_parser as p
from collections import Counter


S = p.input_as_string('inputs/inp.txt')
stones = [int(el) for el in S.strip().split()]
memo = {}

# recursively implements the iterative method to impement memoization
def simulate(stone, iterations):
    if (stone, iterations) in memo:
        return memo[(stone, iterations)]

    if iterations == 0:
        return 1

    if stone == 0:
        result = simulate(1, iterations - 1)
    elif len(str(stone)) % 2 == 0:
        el1 = int(str(stone)[:len(str(stone)) // 2])
        el2 = int(str(stone)[len(str(stone)) // 2:])
        result = simulate(el1, iterations - 1) + simulate(el2, iterations - 1)
    else:
        result = simulate(stone * 2024, iterations - 1)

    memo[(stone, iterations)] = result
    return result


print(sum(simulate(stone, 25) for stone in stones))
print(sum(simulate(stone, 75) for stone in stones))
