import parser

def deel1(lines):
    area = 0
    for line in lines:
        line = [int(x) for x in line.strip().split('x')]
        # print(line)
        [l, w, h] = line
        area += 2*l*w + 2*w*h + 2*h*l
        line.remove(max(line))
        area += line[0] * line[1]
    print(area)

def deel2(lines):
    ribbon = 0
    for line in lines:
        line = [int(x) for x in line.strip().split('x')]
        [l, w, h] = line
        ribbon += l*w*h
        line.remove(max(line))
        ribbon += 2*line[0] +  2*line[1]
    print(ribbon)


def main():
    # lines = parser.input_as_lines('inputs/1.txt')
    # lines = parser.input_as_ints('inputs/1.txt')
    # lines = parser.input_as_grid('inputs/1.txt')
    lines = parser.input_as_lines('inputs/2.txt')
    deel2(lines)

if __name__ == "__main__":
    main()