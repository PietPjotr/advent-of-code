import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict


# recursive reduce that recursively checks only the valid possibilites from
# right to left and continues on the currently valid possible operations
def reduce(res, numbers, part=2):
    if len(numbers) == 1:
        return res == numbers[0]

    last = numbers[-1]
    possible_results = []

    # Check addition
    if res > last:
        possible_results.append((res - last, numbers[:-1]))
    # Check multiplication
    if res % last == 0:
        possible_results.append((res // last, numbers[:-1]))
    # Check concatenation only for part 2
    if part == 2:
        last_str = str(last)
        res_str = str(res)
        if res_str.endswith(last_str):
            new_res_str = res_str[:len(res_str) - len(last_str)]
            if new_res_str:
                possible_results.append((int(new_res_str), numbers[:-1]))

    return any(reduce(new_res, new_numbers, part) for new_res, new_numbers in possible_results)


L = p.input_as_lines('inputs/inp.txt')

p1 = 0
p2 = 0
for i, line in enumerate(L):
    res, nums = line.split(': ')
    nums = tuple([int(el) for el in nums.split()])
    res = int(res)
    if reduce(res, nums, 2):  # 2 for part 2 version
        p2 += res
    if reduce(res, nums, 1):  # not 2 for part 1 version
        p1 += res

print(p1)
print(p2)
