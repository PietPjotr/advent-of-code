def first():
    with open('dag2_input.txt', 'r') as f:
        hor = 0
        depth = 0
        for line in f:
            split_line = line.split(" ")
            if split_line[0] == "forward":
                hor += int(split_line[1])
            elif split_line[0] == "up":
                depth -= int(split_line[1])
            elif split_line[0] == "down":
                depth += int(split_line[1])
            else:
                print("something strange happened")

        print("horizontal: {}, depth: {}".format(hor, depth))
        print(hor * depth)


def second():
    with open('dag2_input.txt', 'r') as f:
        hor = 0
        depth = 0
        aim = 0
        for line in f:
            split_line = line.split(" ")
            if split_line[0] == "forward":
                hor += int(split_line[1])
                depth += aim * int(split_line[1])
            elif split_line[0] == "up":
                aim -= int(split_line[1])
            elif split_line[0] == "down":
                aim += int(split_line[1])
            else:
                print("something strange happened")

        print("horizontal: {}, depth: {}".format(hor, depth))
        print(hor * depth)

second()
