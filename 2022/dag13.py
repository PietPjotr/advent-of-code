import parser
import ast

# returns 0 if equal, 1 if left is smaller, -1 if right is smaller
def eval2(left, right):
    stack = []
    stack.append((left, right))
    i = 0
    while stack:
        left, right = stack.pop()
        i += 1
        for i in range(max(len(left), len(right))):
            # try except blocks to enforce the rule saying that if all the elements are equal then the
            # left list should be smaller than the right list
            try:
                el_right = right[i]
            except IndexError:
                return -1 # False
            try:
                el_left = left[i]
            except IndexError:
                return 1 # True

            if type(el_left) == int and type(el_right) == int:
                if el_left < el_right:
                    return 1 # True
                elif el_left == el_right:
                    # print("{} and {} are equal".format(el_left, el_right))
                    continue
                else:
                    return -1 # False

            elif type(el_left) == int and type(el_right) == list:
                stack.append((left[i + 1:], right[i + 1:]))
                stack.append(([el_left], el_right))
                break

            elif type(el_left) == list and type(el_right) == int:
                stack.append((left[i + 1:], right[i + 1:]))
                stack.append((el_left, [el_right]))
                break

            elif type(el_left) == list and type(el_right) == list:
                stack.append((left[i + 1:], right[i + 1:]))
                stack.append((el_left, el_right))
                break

            else:
                print('error')

    return -1 # False

def main():
    def deel1():
        f = open('inputs/dag13.txt')
        lines = f.read().split('\n\n')

        iis = []
        for i, el in enumerate(lines):
            left, right = el.split('\n')
            left = ast.literal_eval(left)
            right = ast.literal_eval(right)

            if eval2(left, right) == 1:
                iis.append(i + 1)

        print(sum(iis))

    def deel2():
        lines = parser.input_as_lines('inputs/dag13.txt')

        packets = [ast.literal_eval(line) for line in lines if line]
        packets.append([[2]])
        packets.append([[6]])

        # sort the packets based on the eval2 function
        from functools import cmp_to_key
        packets = sorted(packets, key=cmp_to_key(lambda item1, item2: eval2(item1, item2)), reverse=True)
        print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))

    deel1()
    deel2()


if __name__ == "__main__":
    main()