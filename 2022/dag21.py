import parser

class Tree:
    def __init__(self, name, left=None, right=None, operator=None, val=float('inf')):
        self.name = name
        self.val = val
        self.left = left
        self.right = right
        self.operator = operator

    def __repr__(self):
        return str(self.val)

    def update_vals(self):
        if self.val != float('inf'):
            return
        else:
            self.left.update_vals()
            self.right.update_vals()
            self.val = op[self.operator](self.left.val, self.right.val)


    def find(self, name):
        if self.name == name:
            return self
        if self.left:
            return self.left.find(name)
        if self.right:
            return self.right.find(name)

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node

    def print_node(self):
        print(self.name, self.val)

    def print(self):
        if self.left:
            self.left.print()
        self.print_node()
        if self.right:
            self.right.print()



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
        print("parent of humn is", cur)
        return True
    else:
        return find_humn(monkeys, monkeys[left]) or find_humn(monkeys, monkeys[right])

def main():
    # lines = parser.input_as_string('inputs/.txt')
    lines = parser.input_as_lines('inputs/dag21.txt')
    # lines = parser.input_as_lines('inputs/dag21_test.txt')
    # lines = parser.input_as_ints('inputs/.txt')
    # lines = parser.input_as_grid('inputs/.txt')
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

    # deprecated, still uses the old dict instead of the tree
    root = update_vals(monkeys, 'root')
    print(int(root))

    left_monkey = monkeys[monkeys['root'][0]]
    right_monkey = monkeys[monkeys['root'][1]]
    left = find_humn(monkeys, left_monkey)
    right = find_humn(monkeys, right_monkey)
    print(left, right)

    right_val = update_vals(monkeys, monkeys['root'][1])
    print(int(right_val))


    # I decided to make a tree instead of a dict since it has more freedom to work with
    root = Tree('root', monkeys['root'][0])
    keys = set(monkeys.keys())
    keys.remove('root')
    while keys:
        left = monkeys[root.name]
        right = monkeys[root.name]
        if isinstance(left, int):
            root.insert_left(Tree(root.left, val=left))
            root.insert_right(Tree(root.right, val=right))
            keys.remove(root.left)
            keys.remove(root.right)
        else:
            root.insert_left(Tree(root.left, left[0], left[1], left[2]))
            root.insert_right(Tree(root.right, right[0], right[1], right[2]))
            keys.remove(root.left)
            keys.remove(root.right)

    root.update_vals()
    print(root.val)





if __name__ == "__main__":
    main()