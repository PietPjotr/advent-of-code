def deel1():
    with open("dag7_input.txt", "r") as f:
        crabs = [int(x) for x in f.readline().split(',')]

        # calculating the median
        n = len(crabs)
        crabs.sort()
        if n % 2 == 0:
            median1 = crabs[n//2]
            median2 = crabs[n//2 - 1]
            median = (median1 + median2)/2
        else:
            median = crabs[n//2]
        print("Median is: " + str(median))

    tot_fuel = 0
    for crab in crabs:
        tot_fuel += abs(median - crab)
    print("fuel required: ", tot_fuel)


def deel2():
    with open("dag7_input.txt", "r") as f:
        crabs = [int(x) for x in f.readline().split(',')]
        crab_sum = sum(crabs)
        length = len(crabs)
        avg = round(crab_sum / length)
        print(avg)


    # brute force finding the best fuel consumption.
    min_fuel = float('inf')
    for avg in range(1000):
        tot_fuel = 0
        for crab in crabs:
            delta = abs(avg - crab)
            tot_fuel += 0.5 * delta * (delta + 1)
        if (round(tot_fuel) < min_fuel):
            min_fuel = round(tot_fuel)
            data = [round(tot_fuel), avg]
            print(data)




deel2()