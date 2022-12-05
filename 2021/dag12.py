import parser
import numpy as np
import copy


def rec_search(graph, cur, visited, visitedList):
    visited.append(cur)
    for edge in graph[cur]:
        if edge == 'end':
            visited.append('end')
            visitedList.append(visited)
        elif not edge.isupper() and edge not in visited:
            rec_search(graph, edge, copy.deepcopy(visited), visitedList)
        elif edge.isupper():
            rec_search(graph, edge, copy.deepcopy(visited), visitedList)


def rec_search2(graph, cur, visited, visitedList, twice):
    visited.append(cur)
    for edge in graph[cur]:
        if edge == 'end':
            visited.append('end')
            visitedList.append(visited)

        # if 'end' not in visited:
        if not edge.isupper():
            if edge not in visited:
                rec_search2(graph, edge, copy.copy(visited), visitedList, twice)
            elif edge in visited and not twice and edge != 'end' and edge != 'start':
                rec_search2(graph, edge, copy.copy(visited), visitedList, True)

        elif edge.isupper():
            rec_search2(graph, edge, copy.copy(visited), visitedList, twice)


def main():
    # lines = parser.input_as_string('inputs/dag12.txt')
    lines = parser.input_as_lines('inputs/dag12.txt')
    # lines = parser.input_as_ints('inputs/dag12.txt')
    # lines = parser.input_as_grid('inputs/dag11.txt')
    lines_n = []
    lines_n = [[char for char in line.split('-')] for line in lines]
    lines = lines_n

    nodes = []
    for edges in lines:
        for node in edges:
            if node not in nodes:
                nodes.append(node)

    connected = []
    for j in range(len(nodes)):
        neighs = []
        for edge in lines:
            if edge[0] == nodes[j]:
                neighs.append(edge[1])
            if edge[1] == nodes[j]:
                neighs.append(edge[0])
        connected.append(neighs)

    zip_iterator = zip(nodes, connected)
    graph = dict(zip_iterator)

    visitedList = []
    # print(graph)
    # rec_search(graph, 'start', [], visitedList)
    rec_search2(graph, 'start', [], visitedList, False)
    print(len(visitedList))

    # for testing the paths:
    # con = []
    # for path in visitedList:
    #     con.append(' '.join(map(str, path)))
    # s = sorted(con)
    # for line in s:
    #     print(line)


if __name__ == "__main__":
    main()
