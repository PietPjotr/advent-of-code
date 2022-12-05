f = open('input.txt')
L = f.read().split('\n\n')
f.close()

# manipulation of the input

instructions = L[1].split('\n')
for (i, e) in enumerate(instructions):
    E = e.split(' ')
    instructions[i] = [int(E[1]), int(E[3]), int(E[5])]

splitcrates = L[0].split('\n')
height = L[0].count('\n')
stacks = [None for _ in range(9)]
indices = [1+4*i for i in range(9)]

for i in range(9):
    stacks[i] = [splitcrates[height-1-j][indices[i]] for j in range(height)]
    stacks[i] = list(filter(lambda x: x != ' ', stacks[i]))

# solution

for I in instructions:
    move = []
    for _ in range(I[0]):
        move.append(stacks[I[1]-1].pop())
    move.reverse()
    for m in move:
        stacks[I[2]-1].append(m)

top = [stacks[i][-1] for i in range(9)]
s = ''
for t in top:
    s += t
print(s)
