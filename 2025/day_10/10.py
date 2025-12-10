import numpy as np
import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import deque



def part1(pattern, buttons):
    """
    pattern: string like ".##."
    buttons: list of tuples of ints (already normalized, single ints as 1-tuple)
    Returns: (min_presses, parity_vector)
    """
    nlights = len(pattern)
    m = len(buttons)

    # convert pattern to target bitmask
    target_mask = 0
    for i, ch in enumerate(pattern):
        if ch == "#":
            target_mask |= (1 << i)

    # precompute button masks
    button_masks = []
    for btn in buttons:
        mask = 0
        for idx in btn:
            mask ^= (1 << idx)
        button_masks.append(mask)

    # BFS
    start = 0
    q = deque([start])
    prev = {start: None}  # maps mask -> (prev_mask, button_index_pressed)

    while q:
        s = q.popleft()
        if s == target_mask:
            # reconstruct parity vector
            parity = [0] * m
            cur = s
            while prev[cur] is not None:
                pmask, bj = prev[cur]
                parity[bj] ^= 1
                cur = pmask
            presses = sum(parity)
            return presses, parity

        for j, bmask in enumerate(button_masks):
            ns = s ^ bmask
            if ns not in prev:
                prev[ns] = (s, j)
                q.append(ns)

    return None, None


def part2(targets, buttons):
    nlights = len(targets)
    m = len(buttons)

    # build matrix A (nlights x nbuttons)
    A = np.zeros((nlights, m), dtype=float)
    for j, btn in enumerate(buttons):
        for i in btn:
            A[i, j] = 1.0

    b = np.array(targets, dtype=float)

    # Use least-squares which works for singular / rectangular matrices
    x = np.linalg.lstsq(A, b, rcond=None)[0]

    # Round to nearest integer
    xr = np.rint(x).astype(int)

    total = int(np.sum(xr))
    return total, xr.tolist()


L = p.input_as_lines('inputs/inp.txt')

p1 = 0
p2 = 0
for l in L:
    l = l.split()
    target = l[0][1:-1]
    buttons = [eval(el) if isinstance(eval(el), tuple) else (eval(el),) for el in l[1:-1]]
    joltage = eval(l[-1][1:-1])

    t, _ = part1(target, buttons)
    p1 += t

    t, _ = part2(joltage, buttons)
    p2 += t

print(p1)
print(p2)
