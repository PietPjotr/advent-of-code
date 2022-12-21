import parser

def deel1(lines):
    pass

def deel2(lines):
    pass

def move_general(cur_i, new_i, lines, el_to_index):
    ith = el_to_index.index(cur_i)
    new_i = new_i % (len(lines) - 1)

    # we remove the element from the list updating all i's that come after the current element.
    el_to_index = [i - 1 if i > cur_i else i for i in el_to_index]

    # we add the element in its new position
    el_to_index = [i + 1 if i >= new_i else i for i in el_to_index]
    el_to_index[ith] = new_i

    # now we alter the lines list to contain the element in the proper position
    el = lines.pop(cur_i)
    lines.insert(new_i, el)

    return lines, el_to_index



def main():
    lines = parser.input_as_lines('inputs/dag20.txt')
    # lines = parser.input_as_lines('inputs/dag20_test.txt')
    # lines = [4, -2, 5, 6, 7, 8, 9]

    lines = list(map(int, lines))
    el_to_index = [i for i in range(len(lines))]

    decryption_key = 811589153
    lines = [i * decryption_key for i in lines]
    rounds = 10

    for i in range(rounds):
        print(i)
        for ith in range(len(lines)):

            # find the element and calc the new index
            cur_i = el_to_index[ith]
            el = lines[cur_i]
            new_i = cur_i + el

            lines, el_to_index = move_general(cur_i, new_i, lines, el_to_index)
        # print(lines)


    index_0 = lines.index(0)
    index_1000 = (index_0 + 1000) % len(lines)
    index_2000 = (index_0 + 2000) % len(lines)
    index_3000 = (index_0 + 3000) % len(lines)
    res = [lines[index_1000], lines[index_2000], lines[index_3000]]
    print(sum(res))


if __name__ == "__main__":
    main()