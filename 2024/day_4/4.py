import sys
sys.path.append('..')
import my_parser as p


L = p.input_as_lines('inputs/inp.txt')
R = len(L)
C = len(L[0])


def part1():
    res = 0
    for r, l in enumerate(L):
        res += l.count('XMAS')
        res += l[::-1].count('XMAS')

        # down, up, diags
        deltas = [(1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for c, char in enumerate(l):
            if char == 'X':
                for dr, dc in deltas:
                    diagonal = 'X'
                    nr, nc = r, c
                    for _ in range(3):
                        nr += dr
                        nc += dc
                        if 0 <= nr < R and 0 <= nc < C:
                            diagonal += L[nr][nc]
                        else:
                            break
                    if diagonal == 'XMAS':
                        res += 1

    print(res)


def part2():
    p2 = 0
    for r, l in enumerate(L):
        for c, char in enumerate(l):
            if char == 'A':
                diagonals = []

                # up left, up right, down right, down left
                deltas = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
                for dr, dc in deltas:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        diagonals.append(L[nr][nc])
                    else:
                        diagonals.append(None)

                if diagonals.count('M') == 2 and diagonals.count('S') == 2 and \
                   diagonals[0] != diagonals[2]:
                    p2 += 1

    print(p2)


part1()
part2()