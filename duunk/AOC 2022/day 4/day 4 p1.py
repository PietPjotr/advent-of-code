f = open('input.txt')
L = f.read().split('\n')
f.close()

for i in range(len(L)):
    L[i] = L[i].split(',')
    for j in range(2):
        L[i][j] = L[i][j].split('-')
        for k in range(2):
            L[i][j][k] = int(L[i][j][k])

s = 0
for elm in L:
    if (elm[0][0] <= elm[1][0] and elm[0][1] >= elm[1][1]) or\
       (elm[0][0] >= elm[1][0] and elm[0][1] <= elm[1][1]):
        s += 1

print(s)
