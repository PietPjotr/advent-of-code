import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')

inss = [ins.split() for ins in L]
for ins in inss:
    for i in range(len(ins)):
        try:
            ins[i] = int(ins[i])
        except:
            continue

regs = {'a': int(inp, 2), 'b': 0, 'c': 0, 'd': 0}


def solve():
    a = 0
    while True:
        i = 0
        signal = []
        regs['a'] = a
        while 0 <= i < len(L) and len(signal) < 10:
            ins = inss[i]
            if ins[0] == 'cpy':
                regs[ins[2]] = ins[1] if isinstance(ins[1], int) else regs[ins[1]]
            elif ins[0] == 'inc':
                regs[ins[-1]] += 1
            elif ins[0] == 'dec':
                regs[ins[-1]] -= 1
            elif ins[0] == 'jnz':
                val = ins[1] if isinstance(ins[1], int) else regs[ins[1]]
                skip = ins[2] if isinstance(ins[2], int) else regs[ins[2]]
                if val != 0:
                    i += skip - 1
            elif ins[0] == 'out':
                send = ins[1] if isinstance(ins[1], int) else regs[ins[1]]
                signal.append(str(send))
                if signal != ['01'[i % 2] for i in range(len(signal))]:
                    break
            i += 1
        if len(signal) > 0 and signal == ['01'[i % 2] for i in range(len(signal))]:
            print(a)
            return
        a += 1


solve()
