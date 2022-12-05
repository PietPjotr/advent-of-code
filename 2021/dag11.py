# import pandas as pd
import numpy as np


def update(lines, flashed, i, j):
    i_range = len(lines)
    j_range = len(lines[0])
    # updatet = [[False for i in range(i_range)]for j in range(j_range)]

    if i > 0:
        lines[i-1][j] += 1
        if lines[i-1][j] > 9 and flashed[i-1][j] == False:
            flashed[i-1][j] = True
            lines, flashed = update(lines, flashed, i-1, j)

        if j > 0:
            lines[i-1][j-1] += 1
            if lines[i-1][j-1] > 9 and flashed[i-1][j-1] == False:
                flashed[i-1][j-1] = True
                lines, flashed = update(lines, flashed, i-1, j-1)

        if j < j_range - 1:
            lines[i-1][j+1] += 1
            if lines[i-1][j+1] > 9 and flashed[i-1][j+1] == False:
                flashed[i-1][j+1] = True
                lines, flashed = update(lines, flashed, i-1, j+1)

    if i < i_range - 1:
        lines[i+1][j] += 1
        if lines[i+1][j] > 9 and flashed[i+1][j] == False:
            flashed[i+1][j] = True
            lines, flashed = update(lines, flashed, i+1, j)
        if j > 0:
            lines[i+1][j-1] += 1
            if lines[i+1][j-1] > 9 and flashed[i+1][j-1] == False:
                flashed[i+1][j-1] = True
                lines, flashed = update(lines, flashed, i+1, j-1)

        if j < j_range - 1:
            lines[i+1][j+1] += 1
            if lines[i+1][j+1] > 9 and flashed[i+1][j+1] == False:
                flashed[i+1][j+1] = True
                lines, flashed = update(lines, flashed, i+1, j+1)

    if j > 0:
        lines[i][j-1] += 1
        if lines[i][j-1] > 9 and flashed[i][j-1] == False:
            flashed[i][j-1] = True
            lines, flashed = update(lines, flashed, i, j-1)

    if j < j_range - 1:
        lines[i][j+1] += 1
        if lines[i][j+1] > 9 and flashed[i][j+1] == False:
            flashed[i][j+1] = True
            lines, flashed = update(lines, flashed, i, j+1)

    return lines, flashed


def iterate(lines):
    i_range = len(lines)
    j_range = len(lines[0])
    flashed = [[False for i in range(i_range)]for j in range(j_range)]

    # print("start: ")
    # print(np.matrix(lines))
    # print('\n')

    for i in range(i_range):
        for j in range(j_range):
            lines[i][j] += 1
    # print("plus one: ")
    # print(np.matrix(lines))
    # print('\n')

    for twice in range(1):
        for i in range(i_range):
            for j in range(j_range):
                el = lines[i][j]
                if el > 9 and flashed[i][j] == False:
                    flashed[i][j] = True
                    lines, flashed = update(lines, flashed, i, j)
    # print("updated: ")
    # print(np.matrix(lines))
    # print('\n')

    # sets all the values of the flashed opctopuses to 0:
    for i in range(i_range):
        for j in range(j_range):
            if flashed[i][j] == True:
                lines[i][j] = 0
    # print("set to zero: ")
    # print(np.matrix(lines))
    # print('\n')

    return lines, flashed


def main():
    lines = []
    with open('inputs/dag11.txt', 'r') as f:
        for line in f.readlines():
            line_a = []
            line = line.strip()
            for char in line:
                line_a.append(int(char))
            lines.append(line_a)

    i_range = len(lines)
    j_range = len(lines[0])

    STEPS = 210
    flash = 0
    for i in range(STEPS):
        lines, flashed = iterate(lines)
        for line in flashed:
            for char in line:
                if char == True:
                    flash += 1
        for line in lines:
            if line.count(0) != len(lines[0]):
                break
            else:
                print(i)
                # print(np.matrix(lines))



    print(np.matrix(lines))
    print(flash)


if __name__ == "__main__":
    main()
