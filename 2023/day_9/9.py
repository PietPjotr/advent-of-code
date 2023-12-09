import sys
sys.path.append('..')
import my_parser as p

lines = p.input_as_lines('inputs/inp.txt')

l = []

for line in lines:
    line = [int(x) for x in line.split()]

    l.append(line)

lines = l


def predict(diffs):
    """ff flex momentje: ik had deze functie gewoon in eenkeer goed:
    geen errors en werkend zoals bedoeld. Gebeurt echt letterlijk nooit"""
    diffs[-1].append(0)
    for i in range(len(diffs) - 2, -1, -1):
        line = diffs[i]
        line.append(line[-1] + diffs[i + 1][-1])

    return diffs[0][-1]


def predict_backwards(diffs):
    diffs[-1].insert(0, 0)
    for i in range(len(diffs) - 2, -1, -1):
        line = diffs[i]
        line.insert(0, line[0] - diffs[i + 1][0])

    return diffs[0][0]


nxt = []
prev = []

for line in lines:
    all_diffs = [line]
    while True:
        check = all_diffs[-1]
        diffs = []
        for i in range(len(check) - 1):
            diff = check[i + 1] - check[i]
            diffs.append(diff)
        if all(dif == 0 for dif in diffs):
            all_diffs.append(diffs)
            break
        all_diffs.append(diffs)

    extrapolated = predict(all_diffs)
    nxt.append(extrapolated)

    extrapolated = predict_backwards(all_diffs)
    prev.append(extrapolated)


print(sum(nxt))
print(sum(prev))










