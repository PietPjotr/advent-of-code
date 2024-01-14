import sys
sys.path.append('..')
import my_parser as p

inp = int(p.input_as_lines('inputs/inp.txt')[0])

buff = [0]
pos = 0
for i in range(1, 2018):
    pos = (pos + inp) % len(buff)
    buff.insert(pos + 1, i)
    pos += 1

print(buff[buff.index(2017) + 1])

pos = 0
buff = [-1 for _ in range(50000001)]
buff[0] = 0
length = 1
for i in range(1, 50000001):
    pos = (pos + inp) % length
    buff[pos + 1] = i
    pos += 1
    length += 1
    if i % 5000000 == 0:
        print(str(i / 50000000 * 100) + '%')

print(buff[buff.index(0) + 1])