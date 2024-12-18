from collections import deque
import os, re

class Solution:

    def __init__(self, puzzle, coordinates):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])
        self.coordinates = coordinates
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def visualisation(self, puzzle):
        os.system('clear')  # For Linux/OS X
        #os.system('cls')  # For Windows
        for row in puzzle:
            print(''.join(row))

        print(50 * '-')

    def print_path(self, path, puzzle):
        copy = [list(row) for row in puzzle]

        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in path:
                    copy[r][c] = '0'
        
        self.visualisation(copy)

    def valid(self, x, y, puzzle):
        return 0 <= x < self.rows and 0 <= y < self.cols and puzzle[x][y] != '#'
    
    # -------------------------- Part 1 -------------------------- #
    
    def bfs_1(self, puzzle, start, end):
        queue = deque([((start), [])])
        visited = set()
        path = []
        while queue:
            pos, path = queue.popleft()

            if pos == end:
                break

            if pos not in visited:
                visited.add(pos)
                path = path + [pos]
               # self.print_path(path)

                for (dx, dy) in self.directions:
                    nx, ny = pos[0] + dx, pos[1] + dy

                    if self.valid(nx, ny, puzzle):
                        queue.append(((nx, ny), path))

        return len(path)

    def part_1(self):
        puzzle = [list(row) for row in self.puzzle]
        for x, y in self.coordinates[:1024]:
            puzzle[y][x] = '#'

        steps = self.bfs_1(puzzle, start=(0, 0), end=(self.rows - 1, self.cols - 1))
        print(f"Steps --> {steps}")
    
    # -------------------------- Part 2 -------------------------- #

    def bfs_2(self, puzzle, start, end):
        queue = deque([((start), [])])
        path = []
        visited = set()
        while queue:
            pos, path = queue.popleft()

            if pos == end:
                #self.print_path(path, puzzle)
                return len(path)

            if pos not in visited:
                visited.add(pos)
                path = path + [pos]

                for (dx, dy) in self.directions:
                    nx, ny = pos[0] + dx, pos[1] + dy

                    if self.valid(nx, ny, puzzle):
                        queue.append(((nx, ny), path))

        return 0
                    

    def part_2(self):
        puzzle = [list(row) for row in self.puzzle]
        for i in range(len(self.coordinates)):
            x, y = self.coordinates[i]
            puzzle[y][x] = '#'

            steps = self.bfs_2(puzzle, start=(0, 0), end=(self.rows - 1, self.cols - 1))
            if steps == 0:
                print(f"Find --> {x},{y}")
                return


if __name__ == '__main__':
    with open('puzzle.txt') as f:
        dim = 71
        coordinates = list((int(x), int(y)) for x, y in re.findall(r'(\d+),(\d+)', f.read()))
        puzzle = [['.' for _ in range(dim)] for _ in range(dim)]

        sol = Solution(puzzle, coordinates)
        sol.part_1(), sol.part_2()