f = open('input.txt')

L = f.read().split('\n')
f.close()

scores = {'X': 1, 'Y': 2, 'Z': 3}
transform = {'A': 'X', 'B': 'Y', 'C': 'Z'}
cycle = {'A': 'B', 'B': 'C', 'C': 'A'}

def outcome(me, you):
    if me == transform[you]:
        return 3
    elif me == transform[cycle[you]]:
        return 6
    else:
        return 0


s = 0
for e in L:
    s += scores[e[2]] + outcome(e[2], e[0])
print(s)
