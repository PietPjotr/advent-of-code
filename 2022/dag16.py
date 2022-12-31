import parser
import copy
import numpy as np
import itertools

def deel1(lines):
    pass

def deel2(lines):
    pass

class Frame:
    def __init__(self, i, value, cur, opened, path):
        self.remaining = i
        self.value = value
        self.cur = cur
        self.opened = opened
        self.path = path

    def __repr__(self):
        return f'Frame(i: {self.remaining}, v: {self.value}, c:{self.cur}, o:{self.opened}, p:{self.path})'

    def __iter__(self):
        return iter((self.remaining, self.value, self.cur, self.opened, self.path))


minutes = 30
start_node = 'AA'

def confirm_path_score(nodes, distances, names, path, minutes=30):
    score = 0
    print(minutes)
    for i in range(0, len(path) - 1):
        fro = path[i]
        to = path[i + 1]
        j = names.index(fro)
        k = names.index(to)
        minutes -= distances[j][k]
        delta = nodes[to][0] * minutes
        score += delta
        print("opening:", to, "adding:", delta, "new score:", score, "minutes:", minutes, "score:", nodes[to][0])
    # print('final score:', score)
    return score


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


def find_highest_pressure_single(nodes, distances, names, stack):
    its = 0
    maximum = 0
    final_path = []
    while stack:
        # for i in range(0):
        current_frame = stack.pop()
        i, current_score, cur, opened, path = current_frame
        # we always start at a valve with no value, so we just simply add it to the opened set
        if len(opened) == len(names) and current_score > maximum:
            maximum = current_score
            final_path = path
            # print(opened,
            continue

        for neigh in names:
            if neigh not in opened:
                j = names.index(cur)
                k = names.index(neigh)
                cost = distances[j][k]
                new_i = i - cost

                if new_i < -1:
                    if current_score > maximum:
                        maximum = current_score
                        final_path = path
                    continue

                new_score = current_score + new_i * nodes[neigh][0]
                new_opened = opened.copy()
                new_opened.add(neigh)

                new_path = path.copy()
                new_path.append(neigh)
                new_frame = Frame(new_i, new_score, neigh, new_opened, new_path)
                stack.append(new_frame)

        its += 1
        # if its % 1000 == 0:
        #     print('iteration:', its, maximum, len(stack))

    return maximum, final_path


# TODO: change the initial variables to decide stack variables myself instead of always starting at 'AA', to use
# TODO: recursively in case either player has already used up all their time.
def find_highest_pressure_double(nodes, distances, names, minutes):
    global start_node
    start_frame = Frame((minutes, minutes), 0, (start_node, start_node), set([start_node]),
                        ([start_node], [start_node]))
    stack = [start_frame]
    maximum = 0
    its = 0
    final_path = []
    # while stack:
    for _ in range(4):
        current_frame = stack.pop()
        (i1, i2), current_score, (cur1, cur2), opened, (path1, path2) = current_frame
        # we always start at a valve with no value, so we just simply add it to the opened set
        if len(opened) == len(names) and current_score > maximum:
            maximum = current_score
            final_path = (path1, path2)
            print("new high score found (opened all valves):", current_score)
            continue

        remaining = [node for node in names if node not in opened]
        next_pairs = itertools.combinations(remaining, 2)
        for pair in next_pairs:
            # TODO check if giving the getting the higher outcome is worth the effort
            # if pair[0] != fro1 and pair[0] != fro2 and pair[1] != fro1 and pair[1] != fro2:

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
                # simulate player 2 as if it is the only one, since player one is out of time
                if new_i1 <= 0 and new_i2 > 0:
                    print("Player 1 is done, values:", new_i1, new_i2, i1, i2)
                    score = new_i2 * nodes[node2][0]
                    start_frame = Frame(i2, score, cur2, node2, opened.copy(), path2.copy())
                    stack = [start_frame]
                    dscore2, extra_path = find_highest_pressure_single(nodes, distances, names, stack)
                    if current_score + dscore2 > maximum:
                        maximum = current_score + dscore2
                        final_path = (path1, path2 + extra_path)
                        print("new high score found (player 2):", current_score + dscore2)
                        continue

                # simulate player 1 as if it is the only one, since player one is out of time
                if new_i2 <= 0 and new_i1 > 0:
                    start_frame = Frame(i1, 0, cur1, opened.copy(), path1.copy())
                    stack = [start_frame]
                    dscore1, extra_path = find_highest_pressure_single(nodes, distances, names, stack)
                    if current_score + dscore1 > maximum:
                        maximum = current_score + dscore1
                        final_path = (path1 + extra_path, path2)
                        print("new high score found (player 1):", current_score + dscore1)
                        continue

                if new_i1 <= 0 and new_i2 <= 0 and current_score > maximum:
                    maximum = current_score
                    final_path = (path1, path2)
                    print("new high score found (ran out of time):", current_score)
                    continue

                dscore1, dscore2 = new_i1 * nodes[node1][0], new_i2 * nodes[node2][0]
                new_score = current_score + dscore1 + dscore2

                new_opened = opened.copy()
                new_opened.add(node1)
                new_opened.add(node2)

                new_path1, new_path2 = path1.copy(), path2.copy()
                new_path1.append(node1)
                new_path2.append(node2)

                new_frame = Frame((new_i1, new_i2), new_score, (cur1, cur2), (node1, node2), new_opened, (new_path1, new_path2))
                stack.append(new_frame)
                # print("adding new frame:", new_frame)


        its += 1
        if its % 1 == 0:
            print('iteration:', its, maximum, len(stack))

    return maximum, final_path


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

    global start_node
    global minutes
    start_frame = Frame(minutes, 0, start_node, {'AA'}, [start_node])
    stack = [start_frame]

    max_, final_path = find_highest_pressure_single(nodes, distances, names, stack)
    print("score1:", max_, "\nfinal path:", final_path)
    # score = confirm_path_score(nodes, distances, names, final_path)

    # max_, final_path = find_highest_pressure_double(nodes, distances, names, 26)
    # print("score2:", max_, "\nfinal paths:", final_path)
    # score1 = confirm_path_score(nodes, distances, names, final_path[0], minutes=26)
    # score2 = confirm_path_score(nodes, distances, names, final_path[1], minutes=26)
    # print(score1, final_path[0])
    # print(score2, final_path[1])





if __name__ == "__main__":
    main()