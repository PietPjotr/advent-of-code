import sys
import multiprocessing
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')


def p1(regs):
    sound = 0
    i = 0
    while 0 <= i < len(L):
        ins = L[i].split()
        cmd = ins[0]
        reg = ins[1]
        if cmd == 'snd':
            sound = regs[reg]
        elif cmd == 'set':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] = val
        elif cmd == 'add':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] += val
        elif cmd == 'mul':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] *= val
        elif cmd == 'mod':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] %= val
        elif cmd == 'rcv':
            val = regs[ins[1]] if ins[1] in regs else int(ins[1])
            if val == 0:
                i += 1
                continue
            else:
                print(sound)
                break
        elif cmd == 'jgz':
            offset = regs[ins[2]] if ins[2] in regs else int(ins[2])
            val = regs[ins[1]] if ins[1] in regs else int(ins[1])
            if val > 0:
                i += offset
                continue
        i += 1


def initialize_registers():
    regs = {}
    for ins in L:
        ins = ins.split()
        reg = ins[1]
        try:
            reg = int(ins[1])
        except ValueError:
            if reg not in regs:
                regs[reg] = 0
    return regs


def program(pid, snd_queue, rcv_queue):
    regs = initialize_registers()
    regs['p'] = pid
    i = 0
    send_count = 0
    times_waiting = 0

    while 0 <= i < len(L):
        ins = L[i].split()
        cmd = ins[0]
        reg = ins[1]

        if cmd == 'snd':
            val = regs[reg]
            snd_queue.put(val)
            send_count += 1

        elif cmd == 'set':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] = val

        elif cmd == 'add':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] += val

        elif cmd == 'mul':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] *= val

        elif cmd == 'mod':
            val = regs[ins[2]] if ins[2] in regs else int(ins[2])
            regs[reg] %= val

        elif cmd == 'rcv':
            if rcv_queue.empty():
                times_waiting += 1
                # we have waited too long so there is probably a deadlock
                if times_waiting > 100000 and pid == 1:
                    print(send_count)
                    snd_queue.put('end')
                    return
                continue

            else:
                val = rcv_queue.get()
                if val == 'end':
                    return
                regs[reg] = val

        elif cmd == 'jgz':
            offset = regs[ins[2]] if ins[2] in regs else int(ins[2])
            val = regs[ins[1]] if ins[1] in regs else int(ins[1])
            if val > 0:
                i += offset
                continue

        i += 1

    return send_count


if __name__ == '__main__':
    # part 1
    regs1 = initialize_registers()
    p1(regs1)

    # part 2 using multiprocessing
    # Create queues for communication between programs
    queue_01 = multiprocessing.Queue()
    queue_10 = multiprocessing.Queue()

    # Create processes for both programs
    process_0 = multiprocessing.Process(target=program, args=(0, queue_01, queue_10))
    process_1 = multiprocessing.Process(target=program, args=(1, queue_10, queue_01))

    # Start the processes
    process_0.start()
    process_1.start()

    # Wait for both processes to finish
    process_0.join()
    process_1.join()
