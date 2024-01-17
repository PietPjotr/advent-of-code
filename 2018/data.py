import matplotlib.pyplot as plt

# data from all the aoc years, the first tuple represents the people that
# completed both parts of day 1 and the second value represents the people that
# only completed part 1 of day 1.
# the second value of the tuple represents all the people that completed all
# the days of the year. Wanted to see how that fraction changed over the years
data = {2015: ((88019, 17916), 6710),
        2016: ((25054, 7096), 4231),
        2017: ((53620, 10333), 6812),
        2018: ((76527, 21148), 4007),
        2019: ((110175, 15432), 4155),
        2020: ((180055, 14806), 14246),
        2021: ((223587, 29458), 12004),
        2022: ((280886, 15051), 13195),
        2023: ((231116, 74133), 10614),
}

xs = []
ys_all = []
ys_completed = []
for i, (k, v) in enumerate(data.items()):
    all_1 = sum(v[0])
    completed_1 = v[0][0]
    completed = v[1]
    xs.append(k)
    ys_all.append(completed / all_1)
    ys_completed.append(completed / completed_1)

# plt.show()
plt.plot(xs, ys_all)
plt.plot(xs, ys_completed)
plt.show()

