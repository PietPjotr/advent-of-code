# import parser
import copy


def deel1(monkeys):
    n = 20
    for i in range(n):
        for key, monkey in monkeys.items():
            for j, item in enumerate(monkey["items"]):

                operation = monkey["operation"]
                item = perform_operation(operation, item)
                item = item // 3

                if item % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)

                monkey["business"] += 1

            monkey["items"] = []

    # find the largest two monkey business levels and print their product
    business_sorted = sorted([monkey["business"] for monkey in monkeys.values()])
    print(business_sorted[-1] * business_sorted[-2])

def deel2(monkeys):
    div = 1
    for monkey in monkeys.values():
        div *= monkey["test"]

    n = 10000
    for i in range(n):
        for key, monkey in monkeys.items():
            for j, item in enumerate(monkey["items"]):

                operation = monkey["operation"]
                item = perform_operation(operation, item)
                item = item % div

                if item % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)

                monkey["business"] += 1

            monkey["items"] = []

    # find the largest two monkey business levels and print their product
    business_sorted = sorted([monkey["business"] for monkey in monkeys.values()])
    print(business_sorted[-1] * business_sorted[-2])


def perform_operation(operation, item):
    if operation[0] == "+":
        if operation[1] == "old":
            item *= 2
        else:
            item += int(operation[1])
    elif operation[0] == "*":
        if operation[1] == "old":
            item = item ** 2
        else:
            item *= int(operation[1])

    return item

def main():
    # split the lines based on two newlines
    f = open("inputs/dag11.txt", "r")
    lines = f.read().split("\n\n")
    f.close()

    # f = open("inputs/dag11_test.txt", "r")
    # lines = f.read().split("\n\n")
    # f.close()

    monkeys = {}
    for i, line in enumerate(lines):
        monkey = {}
        line = line.strip().split("\n")

        monkey["items"] = list(map(int, line[1][line[1].index(":") + 2:].split(", ")))
        monkey["operation"] = line[2][line[2].index("=") + 6:].split(" ")
        monkey["test"] = int(line[3][line[3].index("y") + 2:])
        monkey["true"] = str(line[4][line[4].index("y") + 2:])
        monkey["false"] = str(line[5][line[5].index("y") + 2:])
        monkey["business"] = 0
        monkeys[str(i)] = monkey

    deel1(copy.deepcopy(monkeys))
    deel2(copy.deepcopy(monkeys))



if __name__ == "__main__":
    main()