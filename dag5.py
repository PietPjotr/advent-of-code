import math

with open("dag5_input.txt", "r") as f:
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for line in f.readlines():
        [one, two] = line.split(" -> ")
        # print(one, two)
        coord1 = [int(one.split(",")[0]), int(one.split(",")[1])]
        coord2 = [int(two.split(",")[0]), int(two.split(",")[1])]

        if coord1[0] == coord2[0]:
            if coord1[1] > coord2[1]:
                for i in range(coord2[1], coord1[1] + 1):
                    grid[coord1[0]][i] += 1

            else:
                for i in range(coord1[1], coord2[1] + 1):
                    grid[coord1[0]][i] += 1

        elif coord1[1] == coord2[1]:
            if coord1[0] > coord2[0]:
                for i in range(coord2[0], coord1[0] + 1):
                    grid[i][coord1[1]] += 1

            else:
                for i in range(coord1[0], coord2[0] + 1):
                    grid[i][coord1[1]] += 1


        ## diagonal pipes:
        elif abs(coord1[0] - coord2[0]):
            # 4 cases:
            if coord1[0] > coord2[0]:
                if coord1[1] > coord2[1]:
                    for i in range(abs(coord1[0] - coord2[0]) + 1):
                        grid[coord2[0] + i][coord2[1] + i] += 1

                else:
                    for i in range(abs(coord1[0] - coord2[0]) + 1):
                        grid[coord2[0] + i][coord2[1] - i] += 1

            else:
                if coord1[1] > coord2[1]:
                    for i in range(abs(coord1[0] - coord2[0]) + 1):
                        grid[coord2[0] - i][coord2[1] + i] += 1

                else:
                    for i in range(abs(coord1[0] - coord2[0]) + 1):
                        grid[coord2[0] - i][coord2[1] - i] += 1



    count = 0
    for i in range(1000):
        for j in range(1000):
            if (grid[i][j]) >= 2:
                count += 1

    print(count)

