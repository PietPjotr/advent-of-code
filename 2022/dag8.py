import parser


"""
This function creates s list of all the trees that are larger than the tree at the current position. Then it checks 
if the list is empty. If it is, the tree is visible from that side. If the tree is visisble from any side, it is 
visible.
"""
def check_visible(trees, x, y):

    if x == 0 or x == len(trees[0]) - 1:
        return True
    if y == 0 or y == len(trees) - 1:
        return True

    left = [tree for tree in trees[y][: x] if tree >= trees[y][x]]
    if len(left) == 0:
        return True

    right = [tree for tree in trees[y][x + 1:] if tree >= trees[y][x]]
    if len(right) == 0:
        return True

    up = [tree for tree in [trees[i][x] for i in range(y)] if tree >= trees[y][x]]
    if len(up) == 0:
        return True

    down = [tree for tree in [trees[i][x] for i in range(y + 1, len(trees))] if tree >= trees[y][x]]
    if len(down) == 0:
        return True

    return False


"""This function checks from the tree to all sides how many trees are visible than the tree at the given position. 
It stops until it find a tree that is larger or equal to the tree at the given position. The score returned is the
product of the visible trees on all sides."""
def scenic_score(trees, x, y):

    if x == 0 or x == len(trees[0]) - 1:
        return 0
    if y == 0 or y == len(trees) - 1:
        return 0

    score_left = 0
    for tree in trees[y][: x][::-1]:
        if tree < trees[y][x]:
            score_left += 1
        elif tree == trees[y][x]:
            score_left += 1
            break

    score_right = 0
    for tree in trees[y][x + 1:]:
        if tree < trees[y][x]:
            score_right += 1
        elif tree == trees[y][x]:
            score_right += 1
            break

    score_up = 0
    for tree in [trees[i][x] for i in range(y - 1, -1, -1)]:
        if tree < trees[y][x]:
            score_up += 1
        elif tree == trees[y][x]:
            score_up += 1
            break

    score_down = 0
    for tree in [trees[i][x] for i in range(y + 1, len(trees))]:
        if tree < trees[y][x]:
            score_down += 1
        elif tree == trees[y][x]:
            score_down += 1
            break

    return score_left * score_right * score_up * score_down


def deel1(lines):
    visible = 0
    for i, row in enumerate(lines):
        for j, tree in enumerate(row):
            if check_visible(lines, j, i):
                visible += 1
    print(visible)


def deel2(lines):
    highest_score = 0
    for i, row in enumerate(lines):
        for j, tree in enumerate(row):
            if scenic_score(lines, j, i) > highest_score:
                highest_score = scenic_score(lines, j, i)

    print(highest_score)

def main():

    lines = parser.input_as_grid('inputs/dag8.txt')
    # lines = parser.input_as_grid('inputs/dag8_test.txt')
    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()