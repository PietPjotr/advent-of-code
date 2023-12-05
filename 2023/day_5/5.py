import sys
sys.path.append('..')
import my_parser as p


def mapp(seed, maps):
    for m in maps:
        for r in m:
            if seed >= r[1] and seed < r[1] + r[2]:
                seed = r[0] + seed - r[1]
                break

    return seed


def part1():
    lines = p.input_as_lines('inputs/inp.txt')

    maps = []

    seedline = lines[0]
    seeds = [int(x) for x in seedline[seedline.find(':') + 2:].split()]

    i = 2
    while i < len(lines):

        curmap = []
        while i < len(lines) and lines[i] != '':
            if ':' in lines[i]:
                i += 1
                continue
            else:
                curmap.append([int(x) for x in lines[i].split()])
            i += 1

        maps.append(curmap)
        i += 1


    results = []

    # normal loops
    for seed in seeds:
        results.append(mapp(seed, maps))

    print(min(results))


def part2():
    lines = p.input_as_lines('inputs/inp.txt')

    maps = []

    seedline = lines[0]
    seeds = [int(x) for x in seedline[seedline.find(':') + 2:].split()]

    s = []
    for i in range(0, len(seeds), 2):
        s.append([(seeds[i], seeds[i + 1])])

    seeds = s

    # loop to create maps
    i = 2
    while i < len(lines):

        curmap = []
        while i < len(lines) and lines[i] != '':
            if ':' in lines[i]:
                i += 1
                continue
            else:
                curmap.append([int(x) for x in lines[i].split()])
            i += 1

        maps.append(curmap)
        i += 1

    results = []

    # inane loop that checks for every kind of overlap and adds the new mapped
    # overlap range for the next map round.
    # For the remaining range of the seed, it tries again until all map rows
    # have been checked.
    results = [0] * len(seeds)
    for i, seedset in enumerate(seeds):
        for m in maps:
            its = 0
            nextset = []
            while seedset:
                seed = seedset.pop()
                for r in m:
                    skipped = False
                    # complete overlap
                    if seed[0] >= r[1] and seed[0] + seed[1] <= r[1] + r[2]:
                        nex = (r[0] + seed[0] - r[1], seed[1])
                        nextset.append(nex)
                        break
                    # partial left overlap
                    elif seed[0] >= r[1] and seed[0] < r[1] + r[2]:
                        seedset.append((r[1] + r[2], seed[0] + seed[1] - r[1] - r[2]))
                        nex = (r[0] + seed[0] - r[1], r[1] + r[2] - seed[0])
                        nextset.append(nex)
                        break
                    # partial right overlap
                    elif seed[0] + seed[1] > r[1] and seed[0] + seed[1] <= r[1] + r[2]:
                        seedset.append((seed[0], r[1] - seed[0]))
                        nex = (r[0], seed[0] + seed[1] - r[1])
                        nextset.append(nex)
                        break
                    # no overlap
                    else:
                        skipped = True
                        continue
                # no overlap
                if skipped:
                    nextset.append(seed)
            seedset = nextset
        results[i] = seedset

    # find the smallest seed location
    m = float('inf')
    for seedset in results:
        for seed in seedset:
            if seed[0] < m:
                m = seed[0]
    print(m)

part1()
part2()
