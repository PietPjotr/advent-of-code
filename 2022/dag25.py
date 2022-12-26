import parser


def to_decimal(snafu):
    base = 1
    result = 0
    for el in snafu[::-1]:
        if el == '-':
            result -= base
        elif el == '=':
            result -= base * 2
        else:
            result += int(el) * base
        base *= 5

    return result


def to_snafu2(decimal):
    translate = {'-': -1, '=': -2, '0': 0, '1': 1, '2': 2}
    i = 0
    max_ = 2 * 5 ** i
    while decimal > max_:
        i += 1
        max_ = 2 * 5 ** i
    # now we know the number of decimal places
    length = i + 1
    res = ''
    while decimal != 0:
        closest = [abs(2 * 5 ** i - decimal), abs(5 ** i - decimal), abs(decimal), abs(5 ** i + decimal), abs(2 * 5 ** i + decimal)]
        char = ['2', '1', '0', '-', '=']
        res += char[closest.index(min(closest))]
        decimal -= 5 ** i * translate[res[-1]]
        i -= 1
    while len(res) < length:
        res += '0'
    return res


def main():
    lines = parser.input_as_lines('inputs/dag25.txt')
    res = 0
    for line in lines:
        res += to_decimal(line)
    print(to_snafu2(res))


if __name__ == "__main__":
    main()