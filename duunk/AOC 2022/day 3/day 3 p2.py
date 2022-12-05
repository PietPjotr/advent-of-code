f = open('input.txt')

L = f.read().split('\n')
f.close()

def eval(l):
    if ord(l)-ord('a') >= 0:
        return ord(l)-ord('a')+1
    else:
        return ord(l)-ord('A')+27

score = 0
for i in range(len(L)//3):
    S1 = set(L[3*i])
    S2 = set(L[3*i+1])
    S3 = set(L[3*i+2])
    for val in S1.intersection(S2).intersection(S3):
        score += eval(val)
    
print(score)
