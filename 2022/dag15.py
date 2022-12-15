import parser

def deel1(lines):
    pass

def deel2(lines):
    pass

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def beacon(x, y, sensors):
    for sensor, value in sensors:
        if manhattan_distance(x, y, sensor[0], sensor[1]) <= value:
            return False
    return True

def beacon_efficient(y, beacons, x_min, x_max):
    ranges = []
    for i, beacon in enumerate(beacons):
        value = beacons[beacon]
        range_ = x_range(y, beacon, value)
        # print(range_, beacon, value, i, y)
        if range_ is not None:
            ranges.append(range_)
    s = x_min
    e = x_max
    ranges.sort()
    for range_ in ranges:
        if range_[1] < s:
            continue
        if range_[0] > s:
            return s + 1, range_[0] - 1
        s = range_[1]
    if s < e:
        return s + 1, range_[0] - 1

    return None


def x_range(y, beacon, value):
    if y in range(beacon[1] - value, beacon[1] + value + 1):
        dy = abs(beacon[1] - y)
        a = beacon[0] - (value - dy)
        b = beacon[0] + value - dy
        return a, b
    else:
        return None

def main():
    lines = parser.input_as_lines('inputs/dag15.txt')
    # lines = parser.input_as_lines('inputs/dag15_test.txt')

    sensors = {}
    beacons = set()
    x_max = 0
    x_min = 0
    y_max = 0
    y_min = 0
    for line in lines:
        line = line.split(' ')
        x_sensor = int(line[2][2:-1])
        y_sensor = int(line[3][2:-1])

        x_beacon = int(line[8][2:-1])
        y_beacon = int(line[9][2:])

        value = manhattan_distance(x_sensor, y_sensor, x_beacon, y_beacon)
        sensors[(x_sensor, y_sensor)] = value

        x_max = max(x_max, x_sensor + value)
        x_min = min(x_min, x_sensor - value)

        y_max = max(y_max, y_sensor + value)
        y_min = min(y_min, y_sensor - value)

        beacons.add((x_beacon, y_beacon))

    not_beacons = []
    amount = 0
    y = 2000000
    # print(x_min, x_max, y_min, y_max)
    # for x in range(x_min, x_max + 1):
    #     if not beacon(x, y, sensors.items()) and (x, y) not in beacons:
    #         not_beacons.append((x, y))
    #         amount += 1

    lim = 4000000
    y_max = lim
    x_max = lim
    x_min = 0
    for y in range(y_max):
        print(y)
        range_ = beacon_efficient(y, sensors, x_min, x_max)
        if range_ is not None:
            print(range_, y)
            break

    # print(not_beacons)
    print(range_[0])
    tune = range_[0] * lim + y
    print(tune)




if __name__ == "__main__":
    main()