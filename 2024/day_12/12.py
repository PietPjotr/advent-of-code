import sys
sys.path.append('..')
import my_parser as p
from collections import defaultdict

dirs = [
    (-1, 0), (0, -1), (0, 1), (1, 0),
]

G = p.input_as_grid('inputs/inp.txt')
R = len(G)
C = len(G[0])

# from every position, get its positions with the same character
# and add the position to the visited set, also keep track of
# intermediate positions
components = []
visited = set()
for r in range(R):
    for c in range(C):
        if (r, c) in visited:
            continue
        stack = [(r, c)]
        poss = set(stack)
        while stack:
            r, c = stack.pop()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nc < C and 0 <= nr < R and (nr, nc) not in visited and G[nr][nc] == G[r][c]:
                    stack.append((nr, nc))
                    visited.add((nr, nc))
                    poss.add((nr, nc))
        if poss:
            components.append(poss)

# determine perimeters: check up right down left for all positions in the
# area, and if not in area, then its add 1 to the counter
perimeter_lengths = []
perimeter_positions_list = []  # gets quarter of the position between actual grid coords
areas = []
for s in components:
    perimeter_positions = []
    perimeter_length = 0
    for r, c in s:
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if (nr, nc) not in s:
                perimeter_length += 1
                perimeter_positions.append((r + 0.25 * dr, c + 0.25 * dc))
    perimeter_lengths.append(perimeter_length)
    areas.append(len(s))
    perimeter_positions_list.append(perimeter_positions)

p1 = 0
for i, (p, area) in enumerate(zip(perimeter_lengths, areas)):
    p1 += p * area

print(p1)


# find the different sides of an area using the perimeter positions
all_no_sides = []
for positions in perimeter_positions_list:
    no_sides = 0
    visited = set()
    for r, c in positions:
        if (r, c) in visited:
            continue
        # look into the right and left direction
        if (r, c+1) in positions or (r, c-1) in positions:
            while (r, c+1) in positions:
                visited.add((r, c+1))
                c += 1
            while (r, c-1) in positions:
                visited.add((r, c-1))
                c -= 1
        # look into the up and down direction
        if (r+1, c) in positions or (r-1, c) in positions:
            while (r+1, c) in positions:
                visited.add((r+1, c))
                r += 1
            while (r-1, c) in positions:
                visited.add((r-1, c))
                r -= 1
        no_sides += 1

    all_no_sides.append(no_sides)

p2 = 0
for no_sides, area in zip(all_no_sides, areas):
    p2 += no_sides * area

print(p2)
