import sys
sys.path.append('..')
import my_parser as p

lines = p.input_as_lines('inputs/inp.txt')

str_times = lines[0].split()[1:]
str_distances = lines[1].split()[1:]

times = [int(el) for el in str_times]
distances = [int(el) for el in str_distances]

time2 = [int(''.join(str_times))]
distance2 = [int(''.join(str_distances))]

def calc_score(times, distances):
    wins = []
    for time, distance in zip(times, distances):
        win = 0
        for i in range(0, time + 1):
            speed = i
            if (time - i) * speed > distance:
                win += 1

        wins.append(win)

    res = 1
    for w in wins:
        res *= w

    print(res)


def part1():
    calc_score(times, distances)


def part2():
    calc_score(time2, distance2)


part1()
part2()