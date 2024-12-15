from copy import deepcopy
import time
import os

class Solution:

    def __init__(self, puzzle, moves):
        self.puzzle = puzzle
        self.rows = len(self.puzzle)
        self.cols = len(self.puzzle[0])
        self.moves = moves
        self.directions = {
            '^' : (-1, 0),
            'v' : (1, 0),
            '<' : (0, -1),
            '>' : (0, 1),
        }

    def valid(self, pos, puzzle):
        return 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols and puzzle[pos[0]][pos[1]] != '#'

    def _move(self, pos, dir):
        dx, dy = self.directions[dir]
        return pos[0] + dx, pos[1] + dy
    
    def visualisation(self, puzzle, move, index):
        time.sleep(0.001)
        os.system('clear')  # For Linux/OS X
        #os.system('cls')  # For Windows
        print(f"Move: {move} ({index} out of {len(self.moves)})")
        for row in puzzle:
            print(''.join(row))

        print(50 * '-')

    # -------------------------- Part 1 -------------------------- #
    
    def solve_1(self, pos, puzzle):
        for i, move in enumerate(self.moves):
            next_pos = self._move(pos, move)

            if not self.valid(next_pos, puzzle):
                continue

            if puzzle[next_pos[0]][next_pos[1]] == 'O':
                next_next_pos = self._move(next_pos, move)

                flag = True
                temp_pos = next_pos[:]
                while puzzle[next_next_pos[0]][next_next_pos[1]] != '.':
                    next_next_pos = self._move(temp_pos, move)
                    if not self.valid(next_next_pos, puzzle):
                        flag = False
                        break
                    temp_pos = next_next_pos

                if flag:
                    puzzle[next_next_pos[0]][next_next_pos[1]] = 'O'
                else:
                    continue
            
            puzzle[pos[0]][pos[1]], puzzle[next_pos[0]][next_pos[1]] = '.' , '@'
            pos = next_pos

            # Uncomment if you want to visualize the robot's movements.
            #self.visualisation(puzzle, move, i)
        
        return puzzle

    def part_1(self):
        init_pos = ()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.puzzle[r][c] == '@':
                    init_pos = (r, c)
                    break
            else:
                continue
            break
    
        new_puzzle = self.solve_1(init_pos, deepcopy(self.puzzle))
        return sum([(r * 100 + c) for r in range(self.rows) for c in range(self.cols) if new_puzzle[r][c] == 'O'])
    

    # -------------------------- Part 2 -------------------------- #
    
    def solve_2(self, pos, puzzle):
        for i, move in enumerate(moves):
            targets = [pos]
            flag = True
            for _pos in targets:
                next_pos = self._move(_pos, move)
                if (next_pos[0], next_pos[1]) in targets:
                    continue

                if puzzle[next_pos[0]][next_pos[1]] == '#':
                    flag = False
                    break
                if puzzle[next_pos[0]][next_pos[1]] == '[':
                    targets.append((next_pos[0], next_pos[1]))
                    targets.append((next_pos[0], next_pos[1] + 1))
                if puzzle[next_pos[0]][next_pos[1]] == ']':
                    targets.append((next_pos[0], next_pos[1]))
                    targets.append((next_pos[0], next_pos[1] - 1))

            if not flag:
                continue

            copy = [list(row) for row in puzzle]
            dx, dy = self.directions[move]
            puzzle[pos[0]][pos[1]], puzzle[pos[0] + dx][pos[1] + dy] = '.', '@'

            for br, bc in targets[2:]:
                puzzle[br][bc] = "."
            for br, bc in targets[1:]:
                puzzle[br + dx][bc + dy] = copy[br][bc]

            pos = pos[0] + dx, pos[1] + dy

            # Uncomment if you want to visualize the robot's movements.
            #self.visualisation(puzzle, move, i)
            
        return puzzle

    def trasform_puzzle(self, puzzle):
        items = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
        return [list("".join(items[char] for char in line)) for line in puzzle]

    def part_2(self):
        puzzle = self.trasform_puzzle(self.puzzle)
        rows = len(puzzle)
        cols = len(puzzle[0])
        init_pos = next((r, c) for r in range(rows) for c in range(cols) if puzzle[r][c] == '@')
    
        new_puzzle = self.solve_2(init_pos, puzzle)
        return sum(100 * r + c for r in range(rows) for c in range(cols) if new_puzzle[r][c] == "[")
        
if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [] 
        moves = []
        for row in f:
            row = row.strip()
            if row and '#' in row:
                puzzle.append(list(row))
            elif row:
                moves.extend(list(row))

        sol = Solution(puzzle, moves)
        print([sol.part_1(), sol.part_2()])