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


def upper_bound(minutes, robots, ores, limit=24):
    score = ores[3]
    crackers = robots[3]
    return score + sum([crackers + i for i in range(limit - minutes)])


# at the moment this gives way to low upper bound for the stack frames with no obisian robots and thus very much
# remaining time
def new_upper_bound(costs, blueprint, minutes, robots, ores, limit=24):
    cost = costs[blueprint][3][1]
    production = robots[2] / cost
    i = 1
    dscore = 0
    while production < 1 and minutes + i < limit:
        dscore += production + robots[3]
        production = (robots[2] + i) / cost
        i += 1

    rest = upper_bound(minutes + i, robots, ores, limit)
    score = ores[3] + dscore + rest - ores[3]
    return score


def get_maxs(costs, blueprint):
    max_ore = max([costs[blueprint][1], costs[blueprint][2][0], costs[blueprint][3][0]])
    max_clay = costs[blueprint][2][1]
    max_obsidian = costs[blueprint][3][1]
    return [max_ore, max_clay, max_obsidian, float('inf')]


# possible speed ups from: https://www.reddit.com/r/adventofcode/comments/zpihwi/2022_day_19_solutions/, DrunkHacker
# Prune any branches with fewer geodes at a given time than the best so far
#
# If a geode machine can be built, it must be built
#
# Don't build more robots of a given type than could possibly be necessary given the blueprint
def calc_max_score(costs, blueprint, stack, maxs, limit=24):
    highscore = 0
    final_bots = []
    while stack:
        minutes, robots, ores, to_buy = stack.pop()
        if minutes == limit:
            if ores[3] > highscore:
                highscore = ores[3]
                final_bots = robots
            continue

        if upper_bound(minutes, robots, ores, limit) < highscore:
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
            # if we have a clay robot we no longer want to build ore robots
            if robots[1] >= 1:
                new_to_buy = [1, 2]
                # if we have an obsidian robot we can also start saving up for geode cracking robots
                if robots[2] >= 1:
                    new_to_buy.append(3)
                    # very hacky but 3x speed increase, may not work on all inputs though
                    if robots[2] >= 3:
                        new_to_buy = [2, 3]
                    if robots[3] >= 1:
                        new_to_buy = [2, 3]

            # add all the different possibilities to the stack and also prune on more robots than resources we could
            # spend in a single turn.
            for to_buy in new_to_buy:
                if robots[to_buy] < maxs[to_buy]:
                    new_frame = [minutes, new_robots, ores, to_buy]
                    stack.append(new_frame)
        # we couldn't buy a new robot, so we simply add the current frame with the new resources and new time
        else:
            new_frame = [minutes, robots, ores, to_buy]
            stack.append(new_frame)

    # print("score:", highscore, "final robots:", final_bots, costs[blueprint])
    return highscore


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

    minutes = 0
    robots = [1, 0, 0, 0]
    ores = [0, 0, 0, 0]
    to_buy = [0, 1]
    frame1 = [minutes, robots, ores, to_buy[0]]
    frame2 = [minutes, robots, ores, to_buy[1]]
    stack = [frame1, frame2]

    # part1
    def part1():
        scores_part1 = []
        for blueprint in range(len(costs)):
            maxs = get_maxs(costs, blueprint)
            scores_part1.append(calc_max_score(costs, blueprint, stack.copy(), maxs))

        final_score = sum([(i + 1) * score for i, score in enumerate(scores_part1)])
        print("part1:", final_score)

    # part2
    def part2():
        start = time.time()
        scores_part2 = []
        for blueprint in range(len(costs[:3])):
            maxs = get_maxs(costs, blueprint)
            scores_part2.append(calc_max_score(costs, blueprint, stack.copy(), maxs, 32))

        acc = 1
        [acc := acc * score for score in scores_part2]
        end = time.time()
        spent = end - start
        print("part2:", acc, scores_part2)
        print(f"part2 took {spent} seconds")

    part1()
    part2()


if __name__ == "__main__":
    main()
