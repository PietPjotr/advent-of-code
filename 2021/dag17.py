import parser

# return all the positions the probe reaches.
def simulate(vx, vy, max_x, min_y):
    x = 0
    y = 0
    pos = []
    highest = y
    while x <= max_x and y >= min_y:
        lastx = x
        lasty = y
        x += vx
        y += vy
        if y > highest:
            highest = y
        vy -= 1
        if vx > 0:
            vx -= 1

    return lastx, lasty, highest


def deel2(lines):
    pass

def main():
    x_min = 175
    x_max = 227
    y_min = -79
    y_max = -134


    last_pos = []
    for i in range(1000):
        for j in range(-1000, 1000):
            lastx, lasty, highest = simulate(i, j, x_max, y_max)
            if lastx >= x_min and lasty <= y_min:
                last_pos.append((i, j, highest))

    # print(last_pos)
    print(len(last_pos))
    s = sorted(last_pos, key=lambda x: x[2])
    # print(s)

if __name__ == "__main__":
    main()