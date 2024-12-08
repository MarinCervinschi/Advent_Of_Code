from itertools import combinations

class Solution:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(self.puzzle)
        self.cols = len(self.puzzle[0])
        self._map = self._init_map()
        self.unique_locations = set()

    def _init_map(self):
        _map = {}
        for r in range(self.rows):
            for c in range(self.cols):
                if puzzle[r][c] != '.':
                    _map.setdefault(puzzle[r][c], []).append((r, c))
        
        return _map

    def valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols 
    
    def new_points(self, x1, y1, x2, y2):
        dx, dy = x2 - x1, y2 - y1
                    
        return [
            (x1 + dx, y1 + dy),
            (x1 - dx, y1 - dy),
            (x2 + dx, y2 + dy),
            (x2 - dx, y2 - dy)
        ]
    
    # -------------------------- Part 1 -------------------------- #
    def part_1(self):
        for antenna, locations in self._map.items():
            combs = list(combinations(locations, 2))
            for comb in combs:
                x1, y1 = comb[0][0], comb[0][1]
                x2, y2 = comb[1][0], comb[1][1]

                for nx, ny in self.new_points(x1, y1, x2, y2):
                    if self.valid(nx, ny) and self.puzzle[nx][ny] != antenna:
                        self.unique_locations.add((nx, ny))
                    

        return len(self.unique_locations)
    
    # -------------------------- Part 2 -------------------------- #
    def part_2(self):
        for _, locations in self._map.items():
            combs = list(combinations(locations, 2))
            for comb in combs:
                x1, y1 = comb[0][0], comb[0][1]
                x2, y2 = comb[1][0], comb[1][1]

                dx, dy = x2 - x1, y2 - y1

                def put_antennas(nx, ny, dir):
                    while self.valid(nx, ny):
                        self.unique_locations.add((nx, ny))
                            
                        nx += dx if dir == 'down' else -dx
                        ny += dy if dir == 'down' else -dy

                for nx, ny in self.new_points(x1, y1, x2, y2):
                    put_antennas(nx, ny, 'down')
                    put_antennas(nx, ny, 'up')

        return len(self.unique_locations)

    
if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [[c for c in row.strip()] for row in f]
        
        sol = Solution(puzzle)
        print([sol.part_1(), sol.part_2()])
        