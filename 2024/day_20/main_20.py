from collections import deque
import os
class Solution:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])
        self.count_cheats = 0
        self.picoseconds = 0
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.visited = set()


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

    def valid(self, x, y, puzzle, flag):
        if not flag:
            return 1 <= x < self.rows - 1 and 1 <= y < self.cols - 1 and puzzle[x][y] != '#'
        return 1 <= x < self.rows - 1 and 1 <= y < self.cols - 1
    
    # -------------------------- Part 1 -------------------------- #
    
    def bfs_1(self, puzzle, start, end, search):
        queue = deque([((start), 0)])
        visited = set()
        while queue:
            pos, distance = queue.popleft()

            if pos == end:
                return distance

            if pos in visited:
                continue

            visited.add(pos)
            for (dx, dy) in self.directions:
                nx, ny = pos[0] + dx, pos[1] + dy

                if not self.valid(nx, ny, puzzle, search) or (nx, ny) in visited:
                    continue

                if search and puzzle[pos[0]][pos[1]] == '#':
                    if puzzle[nx][ny] == '.' and pos not in self.visited:
                        self.visited.add(pos)
                        puzzle[pos[0]][pos[1]] = '1'
                        ps = self.bfs_1(puzzle, start, end, False)
                        if self.picoseconds - ps >= 100:
                            self.count_cheats += 1

                        puzzle[pos[0]][pos[1]] = '#'
                else:
                    queue.append(((nx, ny), distance + 1))

        return 0

    def part_1(self):
        start = next((r, c) for c in range(self.cols) for r in range(self.rows) if self.puzzle[r][c] == 'S')
        end = next((r, c) for c in range(self.cols) for r in range(self.rows) if self.puzzle[r][c] == 'E')

        self.picoseconds = self.bfs_1(self.puzzle, start, end, False)
        self.bfs_1(puzzle, start, end, True)
                    
        print(f"Cheats --> {self.count_cheats}")
    
    # -------------------------- Part 2 -------------------------- #               

    def part_2(self):
        puzzle = [list(row) for row in self.puzzle]
        for i in range(len(self.coordinates)):
            x, y = self.coordinates[i]
            puzzle[y][x] = '#'

            steps = self.bfs_1(puzzle, start=(0, 0), end=(self.rows - 1, self.cols - 1))
            if steps == 0:
                print(f"Find --> {x},{y}")
                return


if __name__ == '__main__':
    with open('puzzle.txt') as f:
        puzzle = [list(row.strip()) for row in f]

        sol = Solution(puzzle)
        sol.part_1()