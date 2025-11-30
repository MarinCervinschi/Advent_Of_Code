
class Solution:

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rows = len(self.puzzle)
        self.cols = len(self.puzzle[0])
        self._dict = {}
        self.visited = set()
        self.hiking_trails = 0
        self.direction_vectors = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
        }

    def valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def move(self, pos, dir):
        dx, dy = self.direction_vectors[dir]
        return pos[0] + dx, pos[1] + dy 
    
    def find_dir(self, pos):
        x, y, count = pos[0], pos[1], []
        for dir, (dx, dy) in self.direction_vectors.items():
            if (self.valid(x + dx, y + dy)) and (
                self.puzzle[x + dx][y + dy] == self.puzzle[x][y] + 1):
                    count.append(dir)
                
        return count
    
    # -------------------------- Part 1 -------------------------- #
    
    def find_rec_1(self, pos, start_pos):
        directions = self.find_dir(pos)
        init_pos = pos
        for dir in directions:
            while True:
                next_pos = self.move(pos, dir)
                if ((next_pos[0], next_pos[1]), start_pos) in self.visited:
                    pos = init_pos
                    break

                if (not self.valid(next_pos[0], next_pos[1])) or \
                    (self.puzzle[next_pos[0]][next_pos[1]] != self.puzzle[pos[0]][pos[1]] + 1):
                    pos = init_pos
                    break
                
                pos = next_pos
                if self.puzzle[pos[0]][pos[1]] == 9 :
                    self.visited.add(((pos[0], pos[1]), start_pos))
                    self._dict[start_pos] = self._dict.get(start_pos, 0) + 1
                    pos = init_pos
                    break
                
                self.find_rec_1(pos, start_pos)
                pos = init_pos
                break
    
    def part_1(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.puzzle[r][c] == 0:
                    self.find_rec_1(pos=(r, c), start_pos=(r, c))

        return sum(v for _, v in self._dict.items())
    
    # -------------------------- Part 2 -------------------------- #
    
    def find_rec_2(self, pos):

        directions = self.find_dir(pos)
        init_pos = pos
        for dir in directions:
            while True:
                next_pos = self.move(pos, dir)

                if not (self.valid(next_pos[0], next_pos[1])) or \
                   (self.puzzle[next_pos[0]][next_pos[1]] != (self.puzzle[pos[0]][pos[1]] + 1)):
                    pos = init_pos
                    break

                pos = next_pos

                if self.puzzle[pos[0]][pos[1]] == 9 :
                    self.hiking_trails += 1
                    pos = init_pos
                    break
                
                self.find_rec_2(pos)
                pos = init_pos
                break

    def part_2(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.puzzle[r][c] == 0:
                    self.find_rec_2(pos=(r, c))

        return self.hiking_trails

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [[int(i) for i in row.strip()] for row in f]

        sol = Solution(puzzle)

        print([sol.part_1(), sol.part_2()])