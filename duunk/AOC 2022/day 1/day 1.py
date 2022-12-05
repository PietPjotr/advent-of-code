f = open('input.txt')

L = f.read().split('\n\n')
f.close()

for (i, elm) in enumerate(L):
    L[i] = elm.split('\n')
    for (j, e) in enumerate(L[i]):
        L[i][j] = int(e)

sums = [sum(elm) for elm in L]
sums.sort()

print(sums[-1]+sums[-2]+sums[-3])
