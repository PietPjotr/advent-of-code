import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict
from functools import cache

L = p.input_as_lines('inputs/inp.txt')

links = {}
for line in L:
    nodes = line.split(' ')
    f = nodes[0][:-1]
    t = nodes[1:]
    links[f] = set(t)



def p1(s, e):
    res = 0
    st = list(links[s])
    while st:
        n = st.pop()
        if n == e:
            res += 1
            continue
        for nn in links[n]:
            st.append(nn)

    print(res)


p1('you', 'out')


@cache
def p2(node, seen_dac, seen_fft):
    if node == 'out':
        return 1 if seen_dac and seen_fft else 0
    res = 0
    for nxt in links[node]:
        seen_dac_next = seen_dac or nxt == 'dac'
        seen_fft_next = seen_fft or nxt == 'fft'
        res += p2(nxt, seen_dac_next, seen_fft_next)
    return res


print(p2('svr', False, False))
