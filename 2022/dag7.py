import parser

# My tree datastructure to easily reference the parents as well in case of a cd .. command. That is why i opted for my
# own tree datastructure insead of using a dict of dicts. Slightly more efficient in case the tree got too large.
class Node():
    def __init__(self, name, parent=None, value=0):
        self.name = name
        self.parent = parent
        self.value = value
        self.children = []

    def insert_node(self, node):
        self.children.append(node)

    def print_tree(self):
        print(self.name, self.value)
        for child in self.children:
            child.print_tree()

    def update_values(self):
        sum = 0
        for child in self.children:
            if child.value == 0:
                child.update_values()
            sum += child.value

        self.value = sum

    def get_dirs_under(self, value):
        dirs = []
        if self.value < value and self.children != []:
            dirs.append([self.name, self.value])
        for child in self.children:
            dirs += child.get_dirs_under(value)

        return dirs

    def get_dirs_over(self, value):
        dirs = []
        if self.value >= value and self.children != []:
            dirs.append([self.name, self.value])
        for child in self.children:
            dirs += child.get_dirs_over(value)

        return dirs

    def get_dir_names(self):
        dirs = []
        if self.children != []:
            dirs.append(self.name)
        for child in self.children:
            dirs += child.get_dir_names()

        return dirs


"""add the value of the new dirname to the parent node and returns it as the current directory in the main function"""
def cd(node, path):
    if path == '..':
        return node.parent
    else:
        for child in node.children:
            if child.name == path:
                return child

        new_node = Node(path, node)
        node.insert_node(new_node)
        return new_node

"""Adds all the children nodes to the children list of the parent node."""
def ls(node, files):
    for file in files:
        # node is a directory
        if file[0] == 'dir':
            if file[1] not in node.children:
                new_node = Node(file[1], node)
                node.insert_node(new_node)
            else:
                continue

        # node is a file
        else:
            if file[1] not in node.children:
                # add the value to the node value.
                new_node = Node(file[1], node, int(file[0]))
                node.insert_node(new_node)
            else:
                continue

def deel1(lines):
    lines = ' '.join(lines)
    lines = lines.split('$')

    # Creating a root node
    current_directory = Node('/')
    root = current_directory

    # parse the lines and create a tree
    for line in lines[1:]:
        line = line.strip().split(' ')
        if line[0] == 'cd':
            current_directory = cd(current_directory, line[1])
        elif line[0] == 'ls':
            # converts the elements of the ls command to their respective nodes.
            line = line[1:]
            files = [[line[2 * i], line[2 * i + 1]] for i in range(len(line) // 2)]
            ls(current_directory, files)

    root.update_values()
    n = 100000
    dirs = root.get_dirs_under(n)
    vals = [dir[1] for dir in dirs]
    print(sum(vals))

def deel2(lines):
    lines = ' '.join(lines)
    lines = lines.split('$')

    # Creating a root node
    current_directory = Node('/')
    root = current_directory
    # parse the lines and create a tree
    for line in lines[1:]:
        line = line.strip().split(' ')
        if line[0] == 'cd':
            current_directory = cd(current_directory, line[1])
        elif line[0] == 'ls':
            # converts the elements of the ls command to their respective nodes.
            line = line[1:]
            files = [[line[2 * i], line[2 * i + 1]] for i in range(len(line) // 2)]
            ls(current_directory, files)

    root.update_values()
    n = root.value - 40000000
    dirs = root.get_dirs_over(n)
    dirs.sort(key=lambda x: x[1])
    print(dirs[0][1])

    # dirs = root.get_dir_names()
    # print(len(dirs) == len(set(dirs)), len(dirs), len(set(dirs)))


def main():
    lines = parser.input_as_lines('inputs/dag7.txt')
    # lines = parser.input_as_lines('inputs/dag7_test.txt')
    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()