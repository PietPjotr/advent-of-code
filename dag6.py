import time

def deel1():
    with open("dag6_input.txt", "r") as f:
        line = [int(x) for x in f.readline().split(',')]
        for x in range(110):
            iterate(line)
        print("populatie na {} iteraties:".format(x))
        print(len(line))

def deel2():
    with open("dag6_input.txt", "r") as f:
        line = [int(x) for x in f.readline().split(',')]
        db = []
        for x in range(9):
            number = 0
            for item in line:
                if item == x:
                    number += 1
            db.append(number)

        for i in range(256):
            db = iterate2(db)
        # print("Populatie na {} iteraties:".format(i))
        # print(sum(db))

        pop = sum(db)
        print("done")


def iterate2(db):
    new = []
    first = db[0]
    for i in range(8):
        new.append(db[i + 1])
    new.append(first)
    new[6] += first
    return new



def iterate(inlist):
    length = len(inlist)
    for i in range(length):
        if inlist[i] == 0:
            inlist[i] = 6
            inlist.append(8)
        else:
            inlist[i] -= 1
    return


def main():

    start = time.time()
    deel2()
    end = time.time()
    print(end - start)

if __name__ == "__main__":
    main()
