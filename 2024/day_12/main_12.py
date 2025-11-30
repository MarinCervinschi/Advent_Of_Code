from collections import deque

class Solution:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])
        self.areas = []
        self.perimeters = []
        self.sides = []
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def valid(self, pos):
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols
    
    # -------------------------- Part 1 -------------------------- #
        
    def bfs_1(self, visited, pos):
        stack = deque([pos])
        perimeter = dict()

        area, perim = 0, 0
        while stack:
            x, y = stack.popleft()

            if (x, y) not in visited:
                visited.add((x, y))
                area += 1

                for dx, dy in self.directions:
                    nx, ny = x + dx, y + dy

                    if self.valid((nx, ny)) and self.puzzle[x][y] == self.puzzle[nx][ny]:
                        stack.append((nx, ny))
                    else:
                        perim += 1
                        # for part 2
                        if (dx, dy) not in perimeter:
                            perimeter[(dx, dy)] = set()

                        perimeter[(dx, dy)].add((x, y))
        
        plot = self.puzzle[pos[0]][pos[1]]
        self.areas.append((plot, area))
        self.perimeters.append((plot, perim))

        return perimeter # for part 2
        
    def part_1(self, part_2=False):
        visited = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in visited:
                    perimeter = self.bfs_1(visited, (r, c))
                    if part_2:
                        self.bfs_2(perimeter, self.puzzle[r][c])
        if part_2:
            return
        return sum(area[1] * perimeter[1] for (area, perimeter) in zip(self.areas, self.perimeters))
    
    # -------------------------- Part 2 -------------------------- #
    
    def bfs_2(self, perimeter, plot):
        sides = 0
        for _, dir in perimeter.items():

            visited = set()
            for dx, dy in dir:
                if (dx, dy) not in visited:
                    sides += 1
                    stack = deque([(dx, dy)])

                    while stack:
                        x, y = stack.popleft()
                        if (x, y) not in visited:
                            visited.add((x, y))
                            for dx1, dy1 in self.directions:
                                nx, ny = x + dx1, y + dy1

                                if (nx, ny) in dir:
                                    stack.append((nx, ny))
        
        self.sides.append((plot, sides))

    def part_2(self):
        self.part_1(part_2=True)
        
        return sum(area[1] * side[1] for (area, side) in zip(self.areas, self.sides))

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [[i for i in row.strip()] for row in f]
        
        sol = Solution(puzzle)
        print([sol.part_1(), sol.part_2()])