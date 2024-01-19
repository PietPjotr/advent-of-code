import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')[0]

pos1 = 0
pos2 = 1
recipes = '37'
while True:
    cur1 = int(recipes[pos1])
    cur2 = int(recipes[pos2])
    new = str(cur1 + cur2)
    recipes += new

    pos1 = (pos1 + cur1 + 1) % len(recipes)
    pos2 = (pos2 + cur2 + 1) % len(recipes)
    if L in recipes[-7:]:
        print(recipes[int(L):int(L)+10])
        print(recipes.index(L))
        break
