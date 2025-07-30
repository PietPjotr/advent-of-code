import sys
sys.path.append('..')
import my_parser as p
from utils import *
from collections import defaultdict

S = p.input_as_string('inputs/inp.txt')

print(S)

nums = get_all_numbers(S)

G = Grid([['.']])
print(G)
G.show()

# more annoying ass intcode shit skip