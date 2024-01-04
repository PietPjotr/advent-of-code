import sys
sys.path.append('..')
import my_parser as p


def deel1(lines):
    area = 0
    for line in lines:
        [l, w, h] = line
        area += 2*l*w + 2*w*h + 2*h*l
        area += min(l*w, w*h, h*l)
    print(area)


def deel2(lines):
    ribbon = 0
    for line in lines:
        [l, w, h] = line
        ribbon += l*w*h
        line.remove(max(line))
        ribbon += 2*line[0] + 2*line[1]
    print(ribbon)


def main():
    lines = p.input_as_lines('inputs/inp.txt')
    lines = [[int(x) for x in line.split('x')] for line in lines]
    deel1(lines)
    deel2(lines)


if __name__ == "__main__":
    main()
