import parser
import time

def buy_robot(costs, blueprint, old_ores, to_buy):
    ores = old_ores.copy()
    new_robot = -1
    if to_buy == 0:
        if ores[0] >= costs[blueprint][to_buy]:
            new_robot = to_buy
            ores[0] -= costs[blueprint][to_buy]
    elif to_buy == 1:
        if ores[0] >= costs[blueprint][to_buy]:
            new_robot = to_buy
            ores[0] -= costs[blueprint][to_buy]
    elif to_buy == 2:
        if ores[0] >= costs[blueprint][to_buy][0] and ores[1] >= costs[blueprint][to_buy][1]:
            new_robot = to_buy
            ores[0] -= costs[blueprint][to_buy][0]
            ores[1] -= costs[blueprint][to_buy][1]
    elif to_buy == 3:
        if ores[0] >= costs[blueprint][to_buy][0] and ores[2] >= costs[blueprint][to_buy][1]:
            new_robot = to_buy
            ores[0] -= costs[blueprint][to_buy][0]
            ores[2] -= costs[blueprint][to_buy][1]

    return ores, new_robot


def upper_bound(costs, blueprint, minutes, robots, ores):
    production = sum(robots)
    score = ores[3]
    resources = ores[0] + ores[2]
    # highest = 0
    # for i, bots in enumerate(robots):
    #     if bots > 0:
    #         highest = i

    # if highest == 3:
    cost = sum(list(costs[blueprint][3]))
    crackers = robots[3] + resources / cost
    while minutes <= 32:
        score += crackers
        crackers += production / cost
        production = production + production / cost
        minutes += 1
    # elif highest == 2:

    return int(score)
# else:
#     return float('inf')



def main():
    lines = parser.input_as_lines('inputs/dag19.txt')
    # lines = parser.input_as_lines('inputs/dag19_test.txt')
    costs = []
    for line in lines:
        line = line.split(' ')
        r1 = int(line[6])
        r2 = int(line[12])
        r3 = (int(line[18]), int(line[21]))
        r4 = (int(line[27]), int(line[30]))
        costs.append([r1, r2, r3, r4])

    scores = []
    # for blueprint in range(len(costs[0:3])):
    for blueprint in range(2,3):
        start = time.time()

        stack = []
        minutes = 0
        robots = [1, 0, 0, 0]
        ores = [0, 0, 0, 0]
        to_buy = 0
        frame1 = [minutes, robots, ores, to_buy]

        to_buy = 1
        frame2 = [minutes, robots, ores, to_buy]
        stack.append(frame1)
        stack.append(frame2)
        max_ore = max([costs[blueprint][0], costs[blueprint][1], costs[blueprint][2][0], costs[blueprint][3][0]])
        max_clay = costs[blueprint][2][1]
        max_obsidian = costs[blueprint][3][1]
        maxs = [max_ore, max_clay, max_obsidian, float('inf')]
        its = 0
        highscore = 26

        while stack:
            current_frame = stack.pop()
            minutes, robots, ores, to_buy = current_frame
            if minutes == 32:
                if ores[3] > highscore:
                    highscore = ores[3]
                    end = time.time()
                    print("new highscore:", highscore, end - start)
                continue

            if upper_bound(costs, blueprint, minutes, robots, ores) < highscore:
                continue

            ores, new_robot = buy_robot(costs, blueprint, ores, to_buy)

            # update the ores based on the amount of robots we have not yet counting the robot we just made
            for i in range(4):
                ores[i] += robots[i]

            # if we can build a new robot we build the new robot and add a new frame with all other possible to_buy robots
            minutes += 1
            new_to_buy = [0, 1]  # we can always get the resources for the first two robots, so we always add those
            if new_robot >= 0:
                new_robots = robots.copy()
                new_robots[new_robot] += 1
                # if we have a clay robot we can also save up for an obsidian robot
                if robots[1] >= 1:
                    new_to_buy.append(2)
                    # if we have an obsidian robot we can save up for a geode robot
                    if robots[2] >= 1:
                        new_to_buy.append(3)
                for to_buy in new_to_buy:
                    if robots[to_buy] < maxs[to_buy]:
                        # throw away all the excess resources
                        # for j, ore in enumerate(ores):
                        #     if ore > maxs[j] * 2:
                        #         ores[j] = maxs[j]
                        new_frame = [minutes, new_robots, ores, to_buy]
                        stack.append(new_frame)
                    # print("adding new frames:", new_frame)
            # we couldn't buy a new robot, so we simply add the current frame with the new recourses and the updated time
            else:
                # throw away all the excess resources
                # for j, ore in enumerate(ores):
                #     if ore > maxs[j] * 2:
                #         ores[j] = maxs[j]
                new_frame = [minutes, robots, ores, to_buy]
                stack.append(new_frame)
                # print("adding one new frame:", new_frame)

            its += 1
            # if its % 1000 == 0:
            #     print(its, highscore, len(stack))
        print("highscore found:", highscore, blueprint)
        scores.append(highscore)

    print(scores)
    final_score = sum([(i + 1) * score for i, score in enumerate(scores)])
    print(final_score)
    final_score = scores[0] * scores[1] * scores[2]
    print(final_score)


if __name__ == "__main__":
    main()

# guesses part2: 2816: too low so probably something like 8, 16, >22
#              : 3200: still too low -------------------->8, 16, >25
#              : 3840: still too low -------------------->8, 16, >30
#              : 4480: not the right answer :( 35
# 34           : 4352: nor right
