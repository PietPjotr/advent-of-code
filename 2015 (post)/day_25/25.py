def iterate(num, n):
    for i in range(1, n):
        nex = (num * 252533) % 33554393
        num = nex

    return nex


def get_nth(r, c):
    return int((c + 1) * (c / 2) + (c + (c + r) - 2) * (r - 1) / 2)


def solve():
    r = 2947
    c = 3029

    nth = get_nth(r, c)
    nth_number = iterate(20151125, nth)
    print(nth_number)


solve()
