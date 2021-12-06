with open('dag1_input.txt', 'r') as f:

    increased = 0
    trio = []
    trio.append(int(f.readline()))
    trio.append(int(f.readline()))
    trio.append(int(f.readline()))
    first_sum = sum(trio)
    for line in f.readlines():
        trio.append(int(line))
        trio.pop(0)
        if sum(trio) > first_sum:
            increased += 1
        first_sum = sum(trio)

    print(increased)
