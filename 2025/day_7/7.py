import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

G = p.input_as_grid('inputs/inp.txt')
G = u.Grid(G)

spos = G.findall('S')[0]
first_beam_pos = spos.south()


def f(r, visited):
    #idea: keep a set of the current 'layer'. keep track of the visited and
    # propagate the visited according to the beam splitting rules. The final
    # score for p2 is then simply the sum of all the visited amounts of the
    # final layer and this is thus the amount of paths that can reach all of
    # these final positions and thus the amount of 'timelines'.
    p1 = 0
    while True:
        nr = set()
        for pos in r:
            npos = pos.south()

            if npos not in G:
                print("p1 =", p1)
                p2 = sum([visited[p] for p in r])
                print("p2 =", p2)
                return
            if npos in visited:
                visited[npos] += visited[pos]
                continue
            if G[npos] == '.':
                nr.add(npos)
                visited[npos] += visited[pos]
            elif G[npos] == '^':
                l = npos.west()
                r = npos.east()
                nr.add(l)
                nr.add(r)
                visited[l] += visited[pos]
                visited[r] += visited[pos]
                p1 += 1
        r = nr


r = {first_beam_pos}
visited = defaultdict(int)
visited[first_beam_pos] = 1

f(r, visited)
