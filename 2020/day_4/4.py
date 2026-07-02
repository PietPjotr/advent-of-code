import sys
sys.path.append('..')
import my_parser as p
import utils as u
from collections import defaultdict

S = p.input_as_string('inputs/inp.txt')
L = p.input_as_lines('inputs/inp.txt')
G = p.input_as_grid('inputs/inp.txt')
