import parser
import numpy as np

def deel1(lines):
    pass


def deel2(lines):
    pass

def print_scanner(scanners):
    for i, scanner in enumerate(scanners):
        print("scanner: ", i)
        print(np.matrix(scanner))

def orient(scanner, matrix):
    return [list(np.dot(coord, matrix)) for coord in scanner]

def create_delta(scanner):
    delta_list = {}
    for coord0 in scanner:
        deltas = []
        for coord1 in scanner:
            if coord0 != coord1:
                deltax = coord0[0] - coord1[0]
                deltay = coord0[1] - coord1[1]
                deltaz = coord0[2] - coord1[2]
                deltas.append([deltax, deltay, deltaz])

        delta_list[tuple(coord0)] = deltas

    return delta_list

def similar_points(scanner0, scanner1):
    similar = []
    delta_list0 = create_delta(scanner0)
    delta_list1 = create_delta(scanner1)
    for coord0 in delta_list0.keys():
        for coord1 in delta_list1.keys():
            coord0 = tuple(coord0)
            coord1 = tuple(coord1)
            amount = 0
            for delta in delta_list0[coord0]:
                if delta in delta_list1[coord1]:
                    amount += 1

            if amount == 11:
                similar.append([coord0, coord1])

    return similar

def orientation_matrices():
    matrices = []
    indices = [0, 1, 2]
    for first in indices:
        for second in set(indices) - set([first]):
            for third in set(indices) - set([first, second]):
                for i in [1, -1]:
                    for j in [1, -1]:
                        for k in [1, -1]:
                            first_row = [0, 0, 0]
                            first_row[first] = 1 * i
                            second_row = [0, 0, 0]
                            second_row[second] = 1 * j
                            third_row = [0, 0, 0]
                            third_row[third] = 1 * k
                            matrix = [first_row, second_row, third_row]
                            if np.linalg.det(matrix) == 1:
                                matrices.append(matrix)
    return matrices

def check_scanner_overlap(scanner0, scanners, matrices, i):
    ret = []
    for j in range(len(scanners) - i - 1):
        scanner1 = scanners[i + j + 1]
        for matrix in matrices:
            scanner1_rotated = orient(scanner1, matrix)
            similar = similar_points(scanner0, scanner1_rotated)
            if len(similar) == 12:
                ret.append((i, i + j + 1, similar[7], matrix))

    return ret

"""returns the coordinate of scanner1 based on the know coordinates from scanner 0 and the matrix that rotates scanner1"""
def reconstruct_scanner_coordinate(scanner_coord1, similar_row, matrix=None):
    print("inside reconstruct_scanner_coordinate")
    print(scanner_coord1)
    print(similar_row)
    print(matrix)
    return np.add(scanner_coord1, np.dot(matrix ,(np.subtract(similar_row[0], similar_row[1]))))


def test(scanners, matrices, scanner_data):
    scanner0 = scanners[0]
    scanner1 = scanners[1]
    scanner2 = scanners[2]
    scanner3 = scanners[3]
    scanner4 = scanners[4]
    for matrix in matrices:
        scanner_rotated = orient(scanner1, matrix)
        similar = similar_points(scanner0, scanner_rotated)
        if len(similar) == 12:
            break

    # reconstruct the scanner coordinates based on the scanner_data setting the origin to the first scanner
    coord_scanner0 = [0, 0, 0]
    for el in similar:
        print(el)
    coord_scanner1 = reconstruct_scanner_coordinate(coord_scanner0, similar, matrix)
    print(coord_scanner1)

def main():

    f = open("inputs/dag19.txt", "r")
    lines = f.read().split("\n\n")

    f = open("inputs/dag19_test.txt", "r")
    lines = f.read().split("\n\n")

    scanners = []
    for line in lines:
        line = line.split("\n")
        coords = []
        for el in line[1:]:
            coord = list(map(int, el.split(",")))
            coords.append(coord)

        scanners.append(coords)

    matrices = orientation_matrices()
    scanner_data = []
    for i in range(len(scanners)):
        scanner0 = scanners[i]
        data = check_scanner_overlap(scanner0, scanners, matrices, i)
        for row in data:
            if row:
                scanner_data.append(row)

    print(scanner_data)

    scanner_coords = [None for i in range(len(scanners))]
    scanner_coords[0] = [0, 0, 0]

    matrix_per_scanner = [[] for i in range(len(scanners))]
    matrix_per_scanner[0] = np.identity(3)
    for row in scanner_data:
        matrix_per_scanner[row[1]] = row[3]

    for i in range(len(scanner_data)):
        el = scanner_data[i]
        fro = el[0]
        to = el[1]
        if fro == 0:
            matrix = np.identity(3)
        else:
            matrix = matrix_per_scanner[fro]

        if len(matrix) == 0:
            matrix = matrix_per_scanner[to]
            scanner_coords[el[0]] = reconstruct_scanner_coordinate(scanner_coords[el[1]], el[2], matrix)
        scanner_coords[el[1]] = reconstruct_scanner_coordinate(scanner_coords[el[0]], el[2], matrix)

    # test(scanners, matrices, scanner_data)
    print(scanner_coords)




if __name__ == "__main__":
    main()