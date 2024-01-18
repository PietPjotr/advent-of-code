import sys
import heapq
sys.path.append('..')
import my_parser as p


def build_dps(L):
    dps = {}
    all_names = set()

    for line in L:
        line = line.split()
        a, b = line[1], line[7]
        all_names.update([a, b])
        dps.setdefault(b, []).append(a)

    return dps, all_names


def p1(origin):
    hq = list(origin)
    heapq.heapify(hq)
    completed = []

    while hq:
        name = heapq.heappop(hq)
        completed.append(name)

        for k, v in dps.items():
            if all(el in completed for el in v) and k not in completed and k not in hq:
                heapq.heappush(hq, k)

    print(''.join(completed))


def p2(origin, all_names):
    time, done, working_on, todo = 0, [], [], list(origin)

    while len(done) < len(all_names):
        # add the todo tasks to the working on tasks
        while len(working_on) < 5 and todo:
            new_name = heapq.heappop(todo)
            new_task = (new_name, 60 + ord(new_name) - (ord('A') - 1))
            working_on.append(new_task)

        # update the working on list
        new_working_on = [(name, time_remaining - 1) for name, time_remaining in working_on if time_remaining > 1]
        done.extend([name for name, time_remaining in working_on if time_remaining == 1])
        working_on = new_working_on

        # add the newly available tasks to the todo list
        for k, v in dps.items():
            if all(el in done for el in v) and k not in done and k not in [task[0] for task in working_on] and k not in todo:
                heapq.heappush(todo, k)

        time += 1

    print(time)

L = p.input_as_lines('inputs/inp.txt')
dps, all_names = build_dps(L)

origin = set([el for vals in dps.values() for el in vals]) - set(dps.keys())

p1(set([el for el in origin]))
p2(set([el for el in origin]), all_names)
