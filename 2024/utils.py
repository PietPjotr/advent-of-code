from typing import Dict, List, Set, Iterable, Union
import heapq
from collections import defaultdict
import re


class Pos:
    def __init__(self, r: int, c: int) -> None:
        self.r = r
        self.c = c

    def __add__(self, other: Union['Pos', int, Iterable[int]]) -> 'Pos':
        other = self._convert_to_pos(other)
        if isinstance(other, Pos):
            return Pos(self.r + other.r, self.c + other.c)
        return NotImplemented

    def __sub__(self, other: Union['Pos', int, Iterable[int]]) -> 'Pos':
        other = self._convert_to_pos(other)
        if isinstance(other, Pos):
            return Pos(self.r - other.r, self.c - other.c)
        return NotImplemented

    def __mul__(self, other: Union['Pos', int, Iterable[int]]) -> 'Pos':
        other = self._convert_to_pos(other)
        if isinstance(other, Pos):
            return Pos(self.r * other.r, self.c * other.c)
        return NotImplemented

    def __floordiv__(self, other: Union['Pos', int, Iterable[int]]) -> 'Pos':
        other = self._convert_to_pos(other)
        if isinstance(other, Pos):
            return Pos(self.r // other.r, self.c // other.c)
        return NotImplemented

    def __mod__(self, other: Union['Pos', int, Iterable[int]]) -> 'Pos':
        other = self._convert_to_pos(other)
        if isinstance(other, Pos):
            return Pos(self.r % other.r, self.c % other.c)
        return NotImplemented

    def __lt__(self, other: 'Pos') -> bool:
        return (self.r, self.c) < (other.r, other.c)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Pos):
            return self.r == other.r and self.c == other.c
        return False

    def __hash__(self) -> int:
        return hash((self.r, self.c))

    def __repr__(self) -> str:
        return f"({self.r}, {self.c})"

    def __iter__(self):
        return iter((self.r, self.c))

    def dirs(self) -> List['Pos']:
        return [Pos(-1, 0), Pos(0, 1), Pos(1, 0), Pos(0, -1)]

    def nbs(self) -> List['Pos']:
        return [self + d for d in self.dirs()]

    @staticmethod
    def range(self, other: 'Pos') -> List['Pos']:
        rmin = min(self.r, other.r)
        rmax = max(self.r, other.r)
        cmin = min(self.c, other.c)
        cmax = max(self.c, other.c)
        return [Pos(r, c) for r in range(rmin, rmax + 1) for c in range(cmin, cmax + 1)]

    @staticmethod
    def dist(pos1: 'Pos', pos2: 'Pos') -> int:
        """Calculate the Manhattan distance between two Pos objects."""
        return abs(pos1.r - pos2.r) + abs(pos1.c - pos2.c)

    @staticmethod
    def _convert_to_pos(other: Union['Pos', int, Iterable[int]]) -> Union['Pos', int]:
        if isinstance(other, Iterable):
            other = list(other)
            if len(other) == 2 and all(isinstance(x, int) for x in other):
                return Pos(*other)
        return other


class Grid:
    def __init__(self, grid_dict: List[List[str]]) -> None:
        self.grid: Dict[Pos, str] = defaultdict(lambda: '#')
        self.Rmin = 0
        self.Rmax = len(grid_dict) - 1
        self.Cmin = 0
        self.Cmax = len(grid_dict[0]) - 1

        for r in range(self.Rmin, self.Rmax + 1):
            for c in range(self.Cmin, self.Cmax + 1):
                self.grid[Pos(r, c)] = grid_dict[r][c]

    def __getitem__(self, key: Pos) -> str:
        return self.grid[key]

    def __setitem__(self, key: Pos, value: str) -> None:
        self.grid[key] = value

    def __delitem__(self, key: Pos) -> None:
        del self.grid[key]

    def __contains__(self, key: Pos) -> bool:
        return key in self.grid

    def __len__(self) -> int:
        return len(self.grid)

    def __repr__(self) -> str:
        return f"Grid({self.grid})"

    def __min__(self) -> int:
        return min(*self)

    def __max__(self) -> int:
        return max(*self)

    def range(self):
        return Pos(self.Rmin, self.Cmin).range(Pos(self.Rmax, self.Cmax))

    def keys(self):
        return self.grid.keys()

    def values(self):
        return self.grid.values()

    def items(self):
        return self.grid.items()


    def find(self, target_char: str) -> List[Pos]:
        for pos, char in self.items():
            if char == target_char:
                return pos
        return None

    def findall(self, target_char: str) -> List[Pos]:
        return [p for p, c in self.items() if c == target_char]

    def to_string(self) -> str:
        result = ""
        for r in range(self.Rmin, self.Rmax + 1):
            row_str = ''.join(self.grid.get(Pos(r, c), ' ') for c in range(self.Cmin, self.Cmax + 1))
            result += row_str + "\n"
        return result

    def to_grid(self, string: str) -> Dict[Pos, str]:
        grid_dict: Dict[Pos, str] = {}
        rows = string.splitlines()

        for row_index, row in enumerate(rows):
            for col_index, char in enumerate(row):
                grid_dict[Pos(row_index, col_index)] = char

        return grid_dict

    def show(self, positions: Set[Pos]=set(), show_func=lambda x: 'X') -> None:
        for r in range(self.Rmin, self.Rmax + 1):
            for c in range(self.Cmin, self.Cmax + 1):
                p = Pos(r, c)
                if p not in positions:
                    print(self[p], end='')
                else:
                    print(show_func(Pos(r, c)), end='')
            print()
        print()

    def remove(self, chars: Set[str]) -> None:
        keys_to_remove = [pos for pos, char in self.items() if char in chars]
        for key in keys_to_remove:
            del self.grid[key]


def bfs(grid: Grid, startpos: Pos, endpos: Pos) -> Dict[Pos, int]:
    queue = [startpos]
    distances = {startpos: 0}

    while queue:
        current = queue.pop(0)
        current_distance = distances[current]
        for neighbour in current.nbs():
            if neighbour in grid and neighbour not in distances:
                distances[neighbour] = current_distance + 1
                queue.append(neighbour)

    return distances


def dijkstra(grid: Grid, startpos: Pos, endpos: Pos) -> Dict[Pos, int]:
    queue = [(0, startpos)]
    distances = {startpos: 0}
    visited = set()

    while queue:
        current_distance, current_pos = heapq.heappop(queue)

        if current_pos in visited:
            continue
        visited.add(current_pos)

        for neighbour in current_pos.nbs():
            if neighbour in grid and neighbour not in visited:
                new_distance = current_distance + 1
                if neighbour not in distances or new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    heapq.heappush(queue, (new_distance, neighbour))

    return distances


def all_paths(grid: Grid, startpos: Pos, endpos: Pos) -> List[List[Pos]]:
    visited = set()
    all_paths = []

    def dfs(pos: Pos, target: Pos, path: List[Pos]):
        if pos == target:
            all_paths.append(path)
            return
        visited.add(pos)
        for neighbour in pos.nbs():
            if neighbour in grid and neighbour not in visited:
                dfs(neighbour, target, path + [neighbour])
        visited.remove(pos)

    dfs(startpos, endpos, [startpos])
    return all_paths


def all_shortest_paths(grid: Grid, startpos: Pos, endpos: Pos) -> List[List[Pos]]:
    distances = bfs(grid, startpos, endpos)
    min_distance = distances.get(endpos, float('inf'))

    def find_paths(pos: Pos, target: Pos, path: List[Pos]) -> List[List[Pos]]:
        if pos == target:
            return [path]
        paths = []
        for neighbour in pos.nbs():
            if neighbour in grid and distances.get(neighbour, float('inf')) == distances[pos] - 1:
                new_paths = find_paths(neighbour, target, path + [neighbour])
                paths.extend(new_paths)
        return paths

    return find_paths(startpos, endpos, [startpos])


def longest_path(grid: Grid, startpos: Pos, endpos: Pos) -> List[Pos]:
    paths = all_paths(grid, startpos, endpos)
    return max(paths, key=len, default=[])


def get_all_nums(string):
    return [int(el) for el in re.findall(r'\d+', string)]


def get_all_digits(string):
    return [int(el) for el in re.findall(r'\d', string)]


def test_functions():
    pass

test_functions()