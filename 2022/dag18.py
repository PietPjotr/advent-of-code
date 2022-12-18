import parser
def adjacent(cube1, cube2):
    if abs(cube1[0] - cube2[0]) == 1 and cube1[1] == cube2[1] and cube1[2] == cube2[2]:
        return True
    elif abs(cube1[1] - cube2[1]) == 1 and cube1[0] == cube2[0] and cube1[2] == cube2[2]:
        return True
    elif abs(cube1[2] - cube2[2]) == 1 and cube1[0] == cube2[0] and cube1[1] == cube2[1]:
        return True
    else:
        return False

def main():
    lines = parser.input_as_lines('inputs/dag18.txt')
    # lines = parser.input_as_lines('inputs/dag18_test.txt')
    cubes = []
    x_max = 0
    y_max = 0
    z_max = 0

    x_min = 0
    y_min = 0
    z_min = 0
    for line in lines:
        cube = list(map(int, line.split(',')))
        cubes.append(cube)

        x_max = max(x_max, cube[0])
        y_max = max(y_max, cube[1])
        z_max = max(z_max, cube[2])
        x_min = min(x_min, cube[0])
        y_min = min(y_min, cube[1])
        z_min = min(z_min, cube[2])

    surface = 0
    for i in range(len(cubes)):
        cube_surface = 6
        for j in range(i+1, len(cubes)):
            if adjacent(cubes[i], cubes[j]):
                cube_surface -= 2

        surface += cube_surface

    print("part1:", surface)

    cubes = set(map(tuple, cubes))

    surface = 0
    start = (x_min - 1, y_min - 1, z_min - 1)
    stack = [start]
    added = set([start])
    i = 0
    while stack:
        cube = stack.pop()
        x, y, z = cube
        neighs = [(x+1, y, z), (x, y+1, z), (x, y, z+1), (x-1, y, z), (x, y-1, z), (x, y, z-1)]
        for neigh in neighs:
            if neigh in cubes:
                surface += 1
            else:
                if x_min - 1 <= neigh[0] <= x_max + 1 and y_min - 1 <= neigh[1] <= y_max + 1 and z_min - 1 <= neigh[2] \
                   <= z_max + 1:
                    if neigh not in added:
                        stack.append(neigh)
                        added.add(neigh)

    print("part2:", surface)


if __name__ == "__main__":
    main()