f = open('input.txt')
L = f.read().split('\n')
f.close()

scores = {'r': 1, 'p': 2, 's': 3}
scores2 = {'X': 0, 'Y': 3, 'Z': 6}
transform = {'A': 'r', 'B': 'p', 'C': 's'}
cycle = {'A': 'B', 'B': 'C', 'C': 'A'}

def play(you, strat):
    if strat == 'X':
        return transform[cycle[cycle[you]]]
    elif strat == 'Y':
        return transform[you]
    elif strat == 'Z':
        return transform[cycle[you]]

s = 0
for e in L:
    s += scores2[e[2]] + scores[play(e[0], e[2])]
print(s)
