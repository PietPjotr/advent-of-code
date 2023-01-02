import parser
import itertools
import time

# extra test cases and their corresponding results:
# https://www.reddit.com/r/adventofcode/comments/znklnh/2022_day_16_some_extra_test_cases_for_day_16/


"""Used to represent a stack frame, however this way debugging is a lot easier since no recursion"""
class Frame:
    def __init__(self, i, value, cur, opened, path, remaining_score):
        self.remaining = i
        self.value = value
        self.cur = cur
        self.opened = opened
        self.path = path
        self.remaining_score = remaining_score

    def __repr__(self):
        return f'Frame(i: {self.remaining}, v: {self.value}, c:{self.cur}, o:{self.opened}, p:{self.path}, ' \
               f'r:{self.remaining_score})'

    def __iter__(self):
        return iter((self.remaining, self.value, self.cur, self.opened, self.path, self.remaining_score))


minutes = 30
start_node = 'AA'


"""This function creates the distance matrix using floyd-warshall and deletes the valves with 0 flow."""
def create_distance_matrix(nodes):
    distances = []
    for node1 in nodes:
        distance = []
        for node2 in nodes:
            if node1 == node2:
                distance.append(0)
            elif node2 in nodes[node1][1]:
                distance.append(1)
            else:
                distance.append(float('inf'))
        distances.append(distance)

    # use Floyd-Warshall algorithm to update the shortest distances between all the nodes.
    # https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
    number_of_nodes = len(nodes)
    for k in range(number_of_nodes):
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    # remove all the nodes with valve value 0 since they don't add to the score, and add 1 to all the nodes since we
    # also want to open the nodes we travel to (which costs 1 minute), otherwise we don't want to travel to them.
    global start_node
    names = []
    new_distances = []
    for i, (name1, node1) in enumerate(nodes.items()):
        new_distance = []
        if name1 == start_node or node1[0] != 0:
            for j, (name2, node2) in enumerate(nodes.items()):
                if name2 == start_node or node2[0] != 0:
                    new_distance.append(distances[i][j] + 1)
            new_distances.append(new_distance)
            names.append(name1)
    # print(np.matrix(new_distances))
    return new_distances, names


"""Calculates the upper bound for a certain state of the graph, used to prune the search space for efficiency"""
def upper_bound(current_score, remaining_score, i):
    return (i - 2) * remaining_score + current_score


"""Finds the highest pressure given a stack frame with only a single player/actor."""
def find_highest_pressure_single(nodes, distances, names, stack):
    maximum = 0
    final_path = []
    while stack:
        current_frame = stack.pop()
        i, current_score, cur, opened, path, remaining_score = current_frame

        # these need to be the same size since we already pretend that we opened the start valve
        if len(opened) == len(names):
            if current_score > maximum:
                maximum = current_score
                final_path = path
            continue

        if upper_bound(current_score, remaining_score, i) < maximum:
            continue

        for neigh in names:
            if neigh not in opened:
                j = names.index(cur)
                k = names.index(neigh)
                cost = distances[j][k]
                new_i = i - cost

                if new_i <= 0:
                    if current_score > maximum:
                        maximum = current_score
                        final_path = path
                    continue

                new_score = current_score + new_i * nodes[neigh][0]
                stack.append(Frame(new_i, new_score, neigh, opened | {neigh}, path + [neigh],
                             remaining_score - nodes[neigh][0]))

    return maximum, final_path


# This function is not being used, unfortunately this method of finding the result for part 2 did not work. Instead, I
# ended up finding the values for all the paths and combining the two disjoint paths with the largest value.
def find_highest_pressure_double(nodes, distances, names, minutes):
    global start_node
    remaining_score = sum([nodes[node][0] for node in names])
    start_frame = Frame((minutes, minutes), 0, (start_node, start_node), {start_node},
                        ([start_node], [start_node]), remaining_score)
    stack = [start_frame]
    maximum = 2080  # the score that we got from part 1
    its = 0
    final_path = []
    while stack:
        current_frame = stack.pop()
        (i1, i2), current_score, (cur1, cur2), opened, (path1, path2), remaining_score = current_frame

        if upper_bound(current_score, remaining_score, max(i1, i2)) < maximum:
            continue
        # we always start at a valve with no value, so we just simply add it to the opened set
        if len(opened) == len(names) and current_score > maximum:
            maximum = current_score
            final_path = (path1, path2)
            print("new high score found (opened all valves):", current_score)
            continue

        remaining = [node for node in names if node not in opened]
        next_pairs = itertools.combinations(remaining, 2)
        for pair in next_pairs:
            for i in range(2):
                node1 = pair[i]
                node2 = pair[1 - i]
                if node1 == node2:
                    print("we have found two similar nodes for both players at: ", its, node1, pair)
                if (node1 is None and node2 is None) or (node1 is None or node2 is None):
                    print("something strange has happened")
                    continue
                j1, j2 = names.index(cur1), names.index(cur2)
                k1, k2 = names.index(node1), names.index(node2)
                cost1, cost2 = distances[j1][k1], distances[j2][k2]
                new_i1, new_i2 = i1 - cost1, i2 - cost2

                # simulate player 1 as if it is the only one, since player one is out of time
                if new_i1 > 0 and 0 >= new_i2:
                    start_frame = Frame(i1, 0, cur1, opened.copy(), path1.copy(), remaining_score)
                    dscore1, path1 = find_highest_pressure_single(nodes, distances, names, [start_frame])
                    if current_score + dscore1 > maximum:
                        maximum = current_score + dscore1
                        final_path = (path1, path2)
                        print("new high score found (player 1):", current_score + dscore1)
                    continue

                # simulate player 2 as if it is the only one, since player one is out of time
                if new_i2 > 0 and 0 >= new_i1:
                    start_frame = Frame(i2, 0, cur2, opened.copy(), path2.copy(), remaining_score)
                    dscore2, path2 = find_highest_pressure_single(nodes, distances, names, [start_frame])
                    if current_score + dscore2 > maximum:
                        maximum = current_score + dscore2
                        final_path = (path1, path2)
                        print("new high score found (player 2):", current_score + dscore2)
                    continue

                if new_i1 <= 0 and new_i2 <= 0:
                    if current_score > maximum:
                        maximum = current_score
                        final_path = (path1, path2)
                        print("new high score found (ran out of time):", current_score)
                    continue

                dscore1, dscore2 = new_i1 * nodes[node1][0], new_i2 * nodes[node2][0]
                new_score = current_score + dscore1 + dscore2
                new_remaining = remaining_score - nodes[node1][0] - nodes[node2][0]

                new_frame = Frame((new_i1, new_i2), new_score, (node1, node2), opened | {node1, node2},
                                  (path1 + [node1], path2 + [node2]), new_remaining)
                stack.append(new_frame)
                # print("adding new frame:", new_frame)

        its += 1
        if its % 1000 == 0:
            print('iteration:', its, maximum, len(stack))

    return maximum, final_path


"""Is practically the same function as find_highest_pressure, but without pruning to ensure we find all the paths."""
def find_all_paths(nodes, distances, names, stack):
    its = 0
    paths = {}
    while stack:
        current_frame = stack.pop()
        i, current_score, cur, opened, path, remaining_score = current_frame

        # we always start at a valve with no value, so we just simply add it to the opened set
        if len(opened) == len(names):
            perm = tuple(sorted(path))
            if perm in paths and current_score > paths[perm]:
                paths[perm] = current_score
            elif perm not in paths:
                paths[perm] = current_score
            continue

        for neigh in names:
            if neigh not in opened:
                j = names.index(cur)
                k = names.index(neigh)
                cost = distances[j][k]
                new_i = i - cost

                if new_i <= 0:
                    perm = tuple(sorted(path))
                    if perm in paths and current_score > paths[perm]:
                        paths[perm] = current_score
                    elif perm not in paths:
                        paths[perm] = current_score
                    continue

                new_score = current_score + new_i * nodes[neigh][0]
                stack.append(Frame(new_i, new_score, neigh, opened | {neigh}, path + [neigh],
                                   remaining_score - nodes[neigh][0]))

        its += 1
        # if its % 1000 == 0:
        #     print('iteration:', its, len(stack))
    return paths


"""Find the two best disjoint paths from the given paths dict and returns the total score and both paths."""
def best_two_paths(paths):
    its = 0
    best = 0
    final_paths = []
    list_paths = list(paths.items())
    for i in range(len(paths)):
        for j in range(i, len(paths)):
            path1 = set(list_paths[i][0]) - {"AA"}
            path2 = set(list_paths[j][0]) - {"AA"}
            v1, v2 = list_paths[i][1], list_paths[j][1]
            if len(path1 & path2) == 0:
                if v1 + v2 > best:
                    best = v1 + v2
                    final_paths = (['AA'] + list(path1), ['AA'] + list(path2))
        its += 1
        print(its, best, len(paths))


    return best, final_paths[0], final_paths[1]


def main():
    lines = parser.input_as_lines('inputs/dag16.txt')
    lines = parser.input_as_lines('inputs/dag16_test.txt')
    nodes = {}
    for line in lines:
        line = line.split(' ')
        node = line[1]
        value = int(line[4][5:-1])
        neighss = line[9:]
        neighs = []
        for neigh in neighss:
            if ',' in neigh:
                neigh = neigh[:-1]
            neighs.append(neigh)
        neighs.append(node)
        nodes[node] = [value, neighs]

    # gives the distance matrix for the specific network.
    distances, names = create_distance_matrix(nodes)

    # part 1
    global start_node
    global minutes
    start_frame = Frame(minutes, 0, start_node, {start_node}, [start_node], sum(nodes[node][0] for node in names))
    stack = [start_frame]
    score1, final_path = find_highest_pressure_single(nodes, distances, names, stack)
    print("part1: {} \n    {} {}".format(score1, score1, final_path))

    # part 2
    start_frame = Frame(26, 0, start_node, {start_node}, [start_node], sum(nodes[node][0] for node in names))
    stack = [start_frame]
    paths = find_all_paths(nodes, distances, names, stack)
    score2, path1, path2 = best_two_paths(paths)
    score21 = paths[tuple(sorted(path1))]
    score22 = paths[tuple(sorted(path2))]
    print("part2: {} \n    {} {}\n    {} {}".format(score2, score21, path1, score22, path2))


if __name__ == "__main__":
    main()