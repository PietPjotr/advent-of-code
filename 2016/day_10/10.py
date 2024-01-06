import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

bots = [[] for _ in range(len(L))]
outputs = [[] for _ in range(len(L))]
inss = [[] for _ in range(len(L))]
for i in range(len(L)):
    line = L[i % len(L)]
    line = line.split()

    if line[0] == 'bot':
        bot = int(line[1])
        inss[bot] = line

    if line[0] == 'value':
        value = int(line[1])
        bot = int(line[-1])
        bots[bot].append(value)


def solve(low, high):
    i = 0
    while True:
        change = False
        for bot, chips in enumerate(bots):
            ins = inss[bot]
            if len(chips) == 2:
                change = True
                check = sorted(chips)
                if check[0] == low and check[1] == high:
                    print(bot)

                if ins[5] == 'bot':
                    bots[int(ins[6])].append(min(chips))
                elif ins[5] == 'output':
                    outputs[int(ins[6])].append(min(chips))

                if ins[-2] == 'bot':
                    bots[int(ins[-1])].append(max(chips))
                elif ins[-2] == 'output':
                    outputs[int(ins[-1])].append(max(chips))
                bots[bot] = []

        if not change:
            break
        i += 1


solve(17, 61)
print(outputs[0][0] * outputs[1][0] * outputs[2][0])
