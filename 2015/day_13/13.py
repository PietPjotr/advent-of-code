import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

graph = {}
for line in L:
    line = line.split(' ')
    k = line[0]
    k2 = line[-1][:-1]
    sign = line[2]
    v = int(line[3]) if sign == 'gain' else -int(line[3])
    if k in graph:
        graph[k][k2] = v
    else:
        graph[k] = {k2: v}


def get_score(table):
    score = 0
    for i in range(len(table)):
        cur = table[i]
        l = table[i - 1]
        r = table[(i + 1) % len(table)]
        score_left = graph[cur][l]
        score_right = graph[cur][r]
        score += score_left + score_right
    return score


def solve(graph):
    names = set(graph.keys())
    highest = 0
    for name in names:
        stack = [[name]]
        while stack:
            table = stack.pop()
            if len(table) == len(names):
                score = get_score(table)
                if score > highest:
                    highest = score

            for name in names:
                if name not in table:
                    new = table + [name]
                    stack.append(new)

    print(highest)


solve(graph)

# add 'you' to the graph
names = set(graph.keys())
for name in names:
    graph[name]['you'] = 0
graph['you'] = {name: 0 for name in names}

solve(graph)
