import sys
sys.path.append('..')
import my_parser as p
import re

L = p.input_as_lines('inputs/inp.txt')
G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

# sort the values on the times by getting all the numbers and comparing
# from year to second (the guard number will also be considered if times would
# be equal but we know that no times will ever be equal so that won't be a
# problem)
sort = sorted(L, key=lambda x: tuple(map(int, re.findall(r'\d+', x))))

guards = {}
cur_guard = 0
sleep = 0
for line in sort:
    times, rest = line.split('] ')
    time = int(times[-2:])
    guard = re.findall(r'\d+', rest)
    if guard:
        cur_guard = int(guard[0])
        if cur_guard not in guards:
            guards[cur_guard] = [0 for _ in range(60)]
    else:
        if 'wakes up' in rest:
            for minute in range(sleep, time):
                guards[cur_guard][minute] += 1
        elif 'falls asleep' in rest:
            sleep = time

# calc score
p1 = 0
p2 = 0
m1 = 0
m2 = 0
for guard, minutes in guards.items():
    if sum(minutes) > m1:
        m1 = sum(minutes)
        p1 = (guard, minutes.index(max(minutes)))
    if max(minutes) > m2:
        m2 = max(minutes)
        p2 = (guard, minutes.index(max(minutes)))

print(p1[0] * p1[1])
print(p2[0] * p1[1])
