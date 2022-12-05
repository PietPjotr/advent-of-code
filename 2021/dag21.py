import parser


def deel1():
    p1 = 0
    p2 = 0

    pp1 = 0
    pp2 = 5

    rolls = 0

    dice = [i for i in range(1, 101)]
    while True:

        rolls += 1
        pp1 = (pp1 + roll(rolls, dice)) % 10
        p1 += pp1 + 1
        print("player one pos: {}, points {}, total rolls: {}".format(pp1, p1, rolls))
        if p1 >= 1000:
            break

        rolls += 1
        pp2 = (pp2 + roll(rolls, dice)) % 10
        p2 += pp2 + 1
        print("player two pos: {}, points {}, total rolls: {}".format(pp2, p2, rolls))
        print('\n')
        if p2 >= 1000:
            break
        
    if p1 > p2:
        losing_score = p2
    else:
        losing_score = p1

    print(rolls * 3, losing_score, p1, p2)
    print((rolls * 3) * losing_score)


def roll(it, dice):
    index = (it * 3 - 3) % 100
    print(dice[index], dice[(index + 1) % 100], dice[(index + 2) % 100])
    return dice[index] + dice[(index + 1) % 100] + dice[(index + 2) % 100]

def main():
    deel1()


if __name__ == "__main__":
    main()
