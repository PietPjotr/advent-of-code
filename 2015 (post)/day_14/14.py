import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

deers = []

for line in L:
    line = line.split(' ')
    v = line[3]
    duration = line[6]
    rest = line[13]
    deers.append([int(el) for el in [v, duration, rest]])


def get_score(deer, time):
    score = 0
    while time > deer[2] + deer[1]:
        time -= deer[2]
        time -= deer[1]

        score += deer[0] * deer[1]

    travel_time = deer[1]
    while time > 0 and travel_time > 0:
        score += deer[0]
        travel_time -= 1
        time -= 1

    return score

time = 2503
print(max(get_score(deer, time) for deer in deers))

scores = [0 for _ in range(len(deers))]
for i in range(1, time + 1):
    distances = [get_score(deer, i) for deer in deers]
    m = max(distances)
    iis = []
    for j, d in enumerate(distances):
        if d == m:
            iis.append(j)
    for j in iis:
        scores[j] += 1

print(max(scores))
