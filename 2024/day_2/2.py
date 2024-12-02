import sys
sys.path.append('..')
import my_parser as p


G = p.input_as_grid('inputs/inp.txt')


def is_safe(l):
    diffs = [b - a for a, b in zip(l[:-1], l[1:])]
    return all([1 <= d <= 3 for d in diffs]) or all([-3 <= d <= -1 for d in diffs])


# what I actually did
p1 = 0
p2 = 0
for l in G:
    # p1
    if is_safe(l):
        p1 += 1
    # p2
    if any([is_safe(l[0:i] + l[i+1:]) for i in range(len(l))]):
        p2 += 1


# print(p1)
# print(p2)


# one liners cus I have no life
# p1
print(sum([is_safe(l) for l in G]))

#p2
print(sum([any([is_safe(l[0:i] + l[i+1:]) for i in range(len(l))]) for l in G]))