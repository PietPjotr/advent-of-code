import parser

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}


def update_vals(monkeys, name):
    monkey = monkeys[name]
    if isinstance(monkey, int):
        return monkey
    else:
        return op[monkey[2]](update_vals(monkeys, monkey[0]), update_vals(monkeys, monkey[1]))


def find_humn(monkeys, cur):
    if isinstance(cur, int):
        return False
    left = cur[0]
    right = cur[1]
    if left == 'humn' or right == 'humn':
        return True
    else:
        return find_humn(monkeys, monkeys[left]) or find_humn(monkeys, monkeys[right])


def main():
    lines = parser.input_as_lines('inputs/dag21.txt')
    # lines = parser.input_as_lines('inputs/dag21_test.txt')

    monkeys = {}

    for line in lines:
        line = line.split(': ')
        cur = line[0]
        rest = line[1]
        if rest.isnumeric():
            monkeys[cur] = int(rest)
        else:
            rest = rest.split(' ')
            neigh1, neigh2 = rest[0], rest[2]
            operator = rest[1]
            monkeys[cur] = (neigh1, neigh2, operator)

    root = update_vals(monkeys, 'root')
    print(int(root))

    # this was used to find in which subtree the human was.
    left_monkey = monkeys[monkeys['root'][0]]
    right_monkey = monkeys[monkeys['root'][1]]
    left = find_humn(monkeys, left_monkey)
    right = find_humn(monkeys, right_monkey)

    right_val = update_vals(monkeys, monkeys['root'][1])

    # these values were experimentally found, these bounds are specific to my input, used for the binary search
    start = 10**13
    end = -10**13

    # binary search until right_val and left_val are close enough (the same to be exact
    while start - end > 1:
        mid = (start + end) // 2
        monkeys['humn'] = mid
        left_val = update_vals(monkeys, monkeys['root'][0])
        if right_val - left_val > 0:
            start = mid
        else:
            end = mid
    print(mid)


if __name__ == "__main__":
    main()