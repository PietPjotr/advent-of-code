import copy


def deel1():
    with open('dag4_input.txt', 'r') as f:
        bingo = []
        order = f.readline()
        order = list(order.split(','))

        empty = f.readline()
        max_tries = float('inf')
        data = []
        line_num = 0
        lines = []
        all_data = []
        times_bingo = 0
        for line in f.readlines():
            lines.append(line)

        for line in lines:
            checked = False
            if line.strip():
                bingo.append(line.split())
            else:
                # check for bingo:
                tries = 0
                for number in order:
                    tries += 1
                    for i in range(5):
                        for j in range(5):
                            if bingo[i][j] == number:
                                bingo[i][j] = True

                    # checking if a row, column or diagonal contains only True:
                    # checking rows:
                    rows = 0
                    r_sum = 0
                    for row in bingo:
                        if row.count(True) == len(row):
                            if tries < max_tries:
                                max_tries = tries
                            for k in range(5):
                                for l in range(5):
                                    if bingo[k][l] != True:
                                        r_sum += int(bingo[k][l])
                                        times_bingo += 1
                                        print(times_bingo)
                                data = [tries, r_sum, number, line_num, 'row']
                                all_data.append(data)
                            checked = True
                            break

                        rows += 1
                    if checked == True:
                        break

                    # checking columns:
                    cols = 0
                    c_sum = 0
                    transposed = list(zip(*bingo))
                    for column in transposed:
                        if column.count(True) == len(column):
                            if tries < max_tries:
                                max_tries = tries
                            for k in range(5):
                                for l in range(5):
                                    if bingo[k][l] != True:
                                        c_sum += int(bingo[k][l])
                                        times_bingo += 1
                                        print(times_bingo)
                            data = [tries, c_sum, number, line_num, 'col']
                            all_data.append(data)
                            checked = True
                            break
                        cols += 1
                    if checked == True:
                        bingo = []
                        break
                bingo = []

            line_num += 1

        print(data)
        print(all_data)
        print(sorted(all_data, key=lambda x: x[0]))
        # print(data[1] * int(data[2]))


def check_tries(bingo, order, h):
    tries = 0
    for number in order:
        tries += 1
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == number:
                    bingo[i][j] = True

        # checking if a row, column or diagonal contains only True:
        # checking rows:
        rows = 0
        r_sum = 0
        for row in bingo:
            if row.count(True) == len(row):
                for k in range(5):
                    for l in range(5):
                        if bingo[k][l] != True:
                            r_sum += int(bingo[k][l])

                if r_sum == 0:
                    print("0 gevonden in row. It: {}Board: {}".format(h, bingo))
                data = [tries, r_sum, number, 'row']
                return data
            rows += 1

        # checking columns:
        cols = 0
        c_sum = 0
        transposed = [[bingo[a][b]
                       for a in range(len(bingo))] for b in range(len(bingo[0]))]
        for column in transposed:
            if column.count(True) == len(column):
                for m in range(5):
                    for n in range(5):
                        if bingo[m][n] != True:
                            c_sum += int(bingo[m][n])

                if c_sum == 0:
                    print("0 gevonden in col. It: {} Board: {}".format(h, bingo))
                data = [tries, c_sum, number, 'col']
                return data
            cols += 1


def deel2():
    with open('dag4_input.txt', 'r') as f:
        bingo = []
        order = f.readline()
        order = list(order.split(','))

        empty = f.readline()
        data = []
        lines = []
        all_data = []
        boards = []

        for line in f.readlines():
            lines.append(line)

        for line in lines:
            if line.strip():
                bingo.append(line.split())
            else:
                boards.append(bingo)
                bingo = []
        # print(boards)
        h = 0
        while h < len(boards):
            bingo = boards[h]
            data = check_tries(bingo, order, h)
            data.append(h)
            data.append(int(data[1]) * int(data[2]))
            all_data.append(data)
            h += 1

        # print(data)
        print(sorted(all_data, key=lambda x: x[0]))
        print(len(all_data))
        print(223 * 81)


deel2()
