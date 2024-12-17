from heapq import heappop, heappush
import os

class Solution:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(puzzle)
        self.cols = len(puzzle[0])
        self.score = float('inf')
        self.tiles = set()
        self.directions = {
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1),
        }

    def visualisation(self, puzzle, move):
        os.system('clear')  # For Linux/OS X
        #os.system('cls')  # For Windows
        print(f"Move: {move}")
        for row in puzzle:
            print(''.join(row))

        print(50 * '-')

    def is_90_degree_turn(self, current_direction, next_direction):
        directions_order = ["^", ">", "v", "<"]
        current_index = directions_order.index(current_direction)
        next_index = directions_order.index(next_direction)
        
        difference = (next_index - current_index) % len(directions_order)
        
        return difference in {1, 3}
    
    # -------------------------- Part 1 -------------------------- #
    
    def bfs_1(self, visited, pos):
        heap = [(0, pos, '^')]  # (score, position, direction)
        prev = '^'
        while heap:
            score, (x, y), dir = heappop(heap)
            prev = dir
            if (x, y) not in visited:
                visited.add((x, y))

                for next_dir, (dx, dy) in self.directions.items():
                    nx, ny = x + dx, y + dy
                    if self.puzzle[nx][ny] != '#':
                        new_score = score + 1 + (1000 if self.is_90_degree_turn(prev, next_dir) else 0)
                        heappush(heap, (new_score, (nx, ny), next_dir))

                    if self.puzzle[nx][ny] == 'E':
                        self.score = min(new_score, self.score)
                        return


    def part_1(self):
        visited = set()
        init_pos = next((r, c) for c in range(self.cols) for r in range(self.rows) if self.puzzle[r][c] == 'S')
        self.bfs_1(visited, init_pos)
        return self.score + 1000
    
    # -------------------------- Part 2 -------------------------- #
    
    def print_path(self, path):
        copy = [list(row) for row in self.puzzle]

        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) in path:
                    copy[r][c] = '0'
        
        self.visualisation(copy, '0')

    def bfs_2_slow(self, pos):
        heap = [(0, pos, '^', [])] # (score, position, direction, path)
        prev = '^'
        min_score = float('inf')
        temp_path = set()
        
        while heap:
            score, (x, y), dir, path = heappop(heap)
            prev = dir

            if (x, y) not in path:

                path = path + [(x, y)]

                for next_dir, (dx, dy) in self.directions.items():
                    nx, ny = x + dx, y + dy
                    
                    if self.puzzle[nx][ny] == '#':
                        continue

                    new_score = score + 1 + (1000 if self.is_90_degree_turn(prev, next_dir) else 0)
                    
                    if new_score > min_score:
                        continue

                    heappush(heap, (new_score, (nx, ny), next_dir, path))
                    #self.print_path(path)
                    
                    if self.puzzle[nx][ny] == 'E':
                        if new_score < min_score:
                            min_score = new_score
                            temp_path = set(path + [(nx, ny)])
                        elif new_score == min_score:
                            temp_path.update(path + [(nx, ny)])
                        self.score = min_score
        
        self.tiles = temp_path

    def bfs_2(self, start, end):
        heap = [(0, [start], '^')]
        best_scores = {(*start, '^') : 0}
        prev_dir = '^'

        while heap:
            score, path, dir = heappop(heap)
            x, y = pos = path[-1]
            prev_dir = dir

            #self.print_path(path)
            if pos == end:
                self.tiles.update(path)
                self.score = score

            elif score < self.score:
                for next_dir, (dx, dy) in self.directions.items():
                    nx, ny = x + dx, y + dy

                    pos = nx, ny, dir
                    turn_cost = + (1000 if self.is_90_degree_turn(prev_dir, next_dir) else 0)
                    next_score = score + 1 + turn_cost

                    if self.puzzle[nx][ny] != '#' and best_scores.get(pos, next_score + 1) >= next_score:
                        best_scores[pos] = next_score
                        heappush(heap, (next_score, path + [(nx, ny)], next_dir))
    
                    

    def part_2(self):
        start = next((r, c) for c in range(self.cols) for r in range(self.rows) if self.puzzle[r][c] == 'S')
        end = next((r, c) for c in range(self.cols) for r in range(self.rows) if self.puzzle[r][c] == 'E')
        self.bfs_2(start, end)
        return [self.score + 1000, len(self.tiles)
]
if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [list(row.strip()) for row in f]
        
        sol = Solution(puzzle)
        print(sol.part_2())