

def deel1():
    gamma = ''
    for i in range(0, 12):
        ones = 0
        zeros = 0
        with open('dag3_input.txt', 'r') as f:
            for line in f.readlines():
                if line[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            if ones > zeros:
                gamma += '1'
            else:
                gamma += '0'

    epsilon = ''
    for i in range(0, len(gamma)):
        if gamma[i] == "1":
            epsilon += "0"
        else:
            epsilon += "1"

    print(epsilon, gamma)

    # gamma_bin = bin(int(binascii.hexlify(gamma), 16))
    # epsilon_bin = gamma = bin(int(binascii.hexlify(epsilon), 16))

    gamma_int = 1575 #converted online :P
    epsilon_int = 2520 #converted online :P

    print(gamma_int * epsilon_int)


def deel2():
    lines = []
    with open('dag3_input.txt', 'r') as f:
        for line in f.readlines():
            lines.append(line)

    check = ""
    i = 0
    while len(lines) > 1:
        ones = 0
        zeros = 0
        for line in lines:
            if line[i] == '1':
                ones += 1
            else:
                zeros += 1
        # use '>=' for oxygen and '<' for co2 scrubber.
        if ones < zeros:
            check += "1"
        else:
            check += "0"

        lines_new = []
        for line in lines:
            if line[i] == check[i]:
                lines_new.append(line)

        lines = lines_new
        i += 1


    print(lines)
    print(check)

    oxygen = 2509 #converted online :P
    co2 = 1701 #converted online :P

    print(co2 * oxygen)

deel2()





