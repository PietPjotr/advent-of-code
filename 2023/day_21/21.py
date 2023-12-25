import sys
sys.path.append('..')
import my_parser as p

L = p.input_as_lines('inputs/inp.txt')
G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

s = (0, 0)
for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            s = (r, c)

sr, sc = s
assert sr == sc == R // 2


def fill(r, c, steps):
    stack = set([(r, c)])
    for i in range(steps):
        new_stack = set()
        for r, c in stack:
            for dr, dc in ((0,1), (1,0), (-1,0), (0,-1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and G[nr][nc] != '#':
                    new_stack.add((nr, nc))
        stack = new_stack
    return len(stack)


score = fill(*s, 64)
print(score)

size = len(G)
steps = 26501365
assert size % 2 == 1  # uneven
assert (steps - (size - 1) // 2) % size == 0  # end exactly at the end of a grid

width = steps // size
no_uneven = ((width - 1) // 2 * 2 + 1) ** 2
no_even = (width // 2 * 2) ** 2

even = fill(sr, sc, size * 2 + 2)
uneven = fill(sr, sc, size * 2 + 1)

top = fill(size - 1, sc, size - 1)
right = fill(sr, 0, size - 1)
bottom = fill(0, sc, size - 1)
left = fill(sr, size - 1, size - 1)

small_steps = size // 2 - 1

tr_small = fill(size - 1, 0, small_steps)
tl_small = fill(size - 1, size - 1, small_steps)
br_small = fill(0, 0, small_steps)
bl_small = fill(0, size - 1, small_steps)

large_steps = 3 * size // 2 - 1

tr_large = fill(size - 1, 0, large_steps)
tl_large = fill(size - 1, size - 1, large_steps)
br_large = fill(0, 0, large_steps)
bl_large = fill(0, size - 1, large_steps)

print(no_even * even +
      no_uneven * uneven +
      top + right + bottom + left +
      width * (tr_small + br_small + bl_small + tl_small) +
      (width - 1) * (tr_large + br_large + bl_large + tl_large)
)