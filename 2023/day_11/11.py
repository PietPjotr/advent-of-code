import sys
sys.path.append('..')
import my_parser as p

lines = p.input_as_lines('inputs/inp.txt')
lines = [[c for c in l] for l in lines]


def get_empty_rows(lines):
    empty_rows = []
    for i, line in enumerate(lines):
        if all([c == '.' for c in line]):
            empty_rows.append(i)
    return empty_rows


def get_empty_cols(lines):
    empty_cols = []
    for i in range(len(lines[0])):
        col = [lines[j][i] for j in range(len(lines))]
        if all([c == '.' for c in col]):
            empty_cols.append(i)
    return empty_cols


def get_galaxies(lines):
    galaxies = set()
    for i, row in enumerate(lines):
        for j, char in enumerate(row):
            if char == '#':
                galaxies.add((i, j))
    return galaxies


def get_all_distances(galaxies, empty_rows, empty_cols, size):
    distances = []
    for galaxy in galaxies:
        d = []
        for other in galaxies:
            rows = 0
            for empty_row in empty_rows:
                if empty_row in range(min(galaxy[0], other[0]), max(galaxy[0], other[0])):
                    rows += 1
            cols = 0
            for empty_col in empty_cols:
                if empty_col in range(min(galaxy[1], other[1]), max(galaxy[1], other[1])):
                    cols += 1
            d.append(abs(galaxy[0] - other[0]) + abs(galaxy[1] - other[1]) + (rows + cols) * (size - 1))
        distances.append(d)
    return distances


def get_result(galaxies, distances):
    result = 0
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            if i != j:
                result += distances[i][j]
    return result


def main():
    empty_rows = get_empty_rows(lines)
    empty_cols = get_empty_cols(lines)

    galaxies = get_galaxies(lines)

    distances1 = get_all_distances(galaxies, empty_rows, empty_cols, 2)
    distances2 = get_all_distances(galaxies, empty_rows, empty_cols, 10**6)

    result1 = get_result(galaxies, distances1)
    result2 = get_result(galaxies, distances2)
    print(result1)
    print(result2)


if __name__ == '__main__':
    main()