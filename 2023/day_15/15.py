import sys
sys.path.append('..')
import my_parser as p

line = p.input_as_string('inputs/inp.txt')

lines = line.split(',')
box = [[] for _ in range(256)]

def hash_score(string):
    score = 0
    for char in string:
        score += ord(char)
        score *= 17
        score %= 256
    return score

res = 0
for line in lines:
    res += hash_score(line)

    label = ''
    if '-' in line:
        label, _ = line.split('-')
        score = hash_score(label)
        for lens in box[score]:
            if lens.startswith(label):
                box[score].remove(lens)

    if '=' in line:
        label, strength = line.split('=')
        score = hash_score(label)
        strength = int(strength)
        present = False
        for i, lens in enumerate(box[score]):
            if lens.startswith(label):
                box[score][i] = line
                present = True
                break
        if not present:
            box[score].append(line)

print(res)

res = 0
for i, lenses in enumerate(box):
    for j, lens in enumerate(lenses):
        strength = int(lens.split('=')[1])
        res += (i+1) * (j+1) * strength

print(res)
