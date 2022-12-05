f = open('input.txt')
L = f.read().split('\n')
f.close()

def eval(l):
    if ord(l)-ord('a') >= 0:
        return ord(l)-ord('a')+1
    else:
        return ord(l)-ord('A')+27

score = 0
for line in L:
    cut = len(line)//2
    S1 = set(line[0:cut])
    S2 = set(line[cut:])
    for val in S1.intersection(S2):
        score += eval(val)

print(score)
