import parser
from itertools import chain
import ast
import math
import copy


class node:
    """
    This class contains nodes that represent nodes in a binary tree. Every
    node has at most 2 children. All the nodes also have heights. A tree can be
    initiated by vreating a node with the list with two elements and then
    expanding that node using the expand function.
    """
    l = None
    r = None

    def __init__(self, lis):
        self.key = lis
        self.height = 0

    def expand(self):
        """ This function creates all the nodes for the proper elements in the
        list. """
        if isinstance(self.key, list):
            self.l = node(self.key[0])
            self.r = node(self.key[1])
            self.l.expand()
            self.r.expand()
            if self.r.height >= self.l.height:
                self.height = self.r.height + 1
            else:
                self.height = self.l.height + 1
        else:
            self.height = 0
            return

    def inorder(self):
        """ This function prints the keys of all the (leaf) nodes inorder. """
        if isinstance(self.key, list):
            self.l.inorder()
            # print(self.key, self.height)
            self.r.inorder()
        else:
            print(self.key, self.height)

    def find_order(self, nodes=[]):
        """ Returns a list of all the leaf nodes in a given tree. """
        if isinstance(self.key, list):
            self.l.find_order(nodes)
            self.r.find_order(nodes)
        else:
            nodes.append(self)
        return nodes

    def find_left(self, Node):
        """ Finds the leaf left of Node, returns the right node or None. """
        nodes = self.find_order([])

        for n in nodes:
            if n == Node:
                index = nodes.index(Node)
                if index > 0:
                    return nodes[index - 1]
        return None

    def find_right(self, Node):
        """ Finds the leaf right of Node, returns the right node or None. """
        nodes = self.find_order([])

        for n in nodes:
            if n == Node:
                index = nodes.index(Node)
                if index < len(nodes) - 1:
                    return nodes[index + 1]
        return None

    def explode(self):
        """ This function checks whether there is a list that's nested within 4
        other lists and explodes the list according to the AoC rules. """
        path = []
        cur = self
        prev = None
        if cur.height > 4:

            while cur.height > 0:
                path.append(cur)

                # decide which node leads to the deepest node.
                if cur.r and cur.l:
                    if cur.r.height > cur.l.height:
                        next_n = cur.r
                    else:
                        next_n = cur.l
                else:
                    if cur.r:
                        next_n = cur.r
                    if cur.l:
                        next_n = cur.l

                prev = cur
                cur = next_n

            # Adds the value of the left number of the current pair to it's
            # left neighbouring leaf and the same for the right value.
            left = self.find_left(prev.l)
            right = self.find_right(prev.r)
            if left:
                left.key += prev.l.key
            if right:
                right.key += prev.r.key

            # resets the exploded pair.
            prev.key = 0
            prev.height = 0
            prev.l = None
            prev.r = None

            # updates the heights of all the nodes along the path to the deleted
            # node
            for n in path[::-1]:
                if n.r and n.l:
                    n.height = max(n.l.height, n.r.height) + 1
                else:
                    if n.r:
                        n.height = n.r.height + 1
                    elif n.l:
                        n.height = n.l.height + 1
                    else:
                        n.height = 0
            return

        else:
            return

    def syncheight(self):
        self.height = max(
            -1 if self.l is None else self.l.syncheight(),
            -1 if self.r is None else self.r.syncheight()
        ) + 1
        return self.height

    def split(self):
        """ This function splits a pair containing a number greater than 9. """
        nodes = self.find_order([])
        for n in nodes:
            if n.key > 9:
                n.key = [math.floor(n.key/2), math.ceil(n.key/2)]
                n.l = node(n.key[0])
                n.r = node(n.key[1])
                self.syncheight()
                return
        return

    def magnitude(self):
        if self.height < 1:
            return self.key
        else:
            return 3*self.l.magnitude() + 2*self.r.magnitude()

    def add(self, Node):
        root = node([self.key, Node.key])
        root.l = self
        root.r = Node
        root.height = max(root.l.height, root.r.height) + 1
        return root


def deel1(lists):
    cur = lists.pop(0)
    cur = node(cur)
    cur.expand()

    its = 0
    for el in lists:
        its += 1
        new = node(el)
        new.expand()

        cur = cur.add(new)

        nodes = cur.find_order([])
        split = [False if el.key <= 9 else True for el in nodes]
        while any(split) or cur.height > 4:
            if cur.height > 4:
                cur.explode()
            elif any(split):
                cur.split()

            nodes = cur.find_order([])
            split = [False if el.key <= 9 else True for el in nodes]

    print(cur.magnitude())
    cur.inorder()


def deel2(lists):
    m = 0
    for i, el1 in enumerate(lists):
        n1 = node(el1)
        n1.expand()
        for j, el2 in enumerate(lists):
            n2 = node(el2)
            n2.expand()
            if n1.key == n2.key:
                continue

            cur = n2.add(copy.deepcopy(n1))
            # print('', n1.key,'\n', n2.key,'\n', cur.key)


            nodes = cur.find_order([])
            split = [False if el.key <= 9 else True for el in nodes]
            while any(split) or cur.height > 4:
                if cur.height > 4:
                    cur.explode()
                elif any(split):
                    cur.split()

                nodes = cur.find_order([])
                split = [False if el.key <= 9 else True for el in nodes]

            if cur.magnitude() > m:
                print(m, cur.magnitude(), i, j)
                m = cur.magnitude()

    print(m)


def test(lists, i, j):
    l1 = lists[i]
    n1 = node(l1)
    n1.expand()

    l2 = lists[j]
    n2 = node(l2)
    n2.expand()

    cur = n2.add(n1)
    # print('', n1.key,'\n', n2.key,'\n', cur.key)


    nodes = cur.find_order([])
    split = [False if el.key <= 9 else True for el in nodes]
    while any(split) or cur.height > 4:
        if cur.height > 4:
            cur.explode()
        elif any(split):
            cur.split()

        nodes = cur.find_order([])
        split = [False if el.key <= 9 else True for el in nodes]

    print(cur.magnitude())


def main():
    lines = parser.input_as_lines('inputs/dag18.txt')
    lists = []
    for line in lines:
        lists.append(ast.literal_eval(line))

    deel2(lists)
    # print("\ntests: ")
    # test(lists, 0, 1)
    # test(lists, 0, 3)
    # test(lists, 0, 5)
    # test(lists, 0, 8)






if __name__ == "__main__":
    main()
