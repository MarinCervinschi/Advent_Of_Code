if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [[c for c in row.strip()] for row in f]
        """ for row in puzzle:
            print(row) """

        rows, cols = len(puzzle), len(puzzle[0])

        direction_order = ['up', 'right', 'down', 'left'] 
        direction_vectors = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
        }

        unique_positions = set()
        guard_pos = 0
        def turn_right(pos, direction):
            dx, dy = direction_vectors[direction]
            return pos[0] + dx, pos[1] + dy
        
        def next_direction(current_dir):
            index = direction_order.index(current_dir)
            return direction_order[(index + 1) % len(direction_order)]

        def valid_move(pos):
            x, y = pos
            return 0 <= x < rows and 0 <= y < cols 
        
        # part 1
        def part_1():
            
            def simulate(pos):
                dir = 'up'
                while(True):
                    next_pos = turn_right(pos, dir)
                    if not valid_move(next_pos):
                        unique_positions.add(pos)
                        break
                    
                    if puzzle[next_pos[0]][next_pos[1]] == '#':
                        dir = next_direction(dir)
                        continue
                    
                    unique_positions.add(pos)

                    pos = next_pos

            for r in range(rows):
                for c in range(cols):
                    if puzzle[r][c] == '^':
                        global guard_pos
                        guard_pos = (r, c)
                        simulate((r, c))
                        break

            return len(unique_positions)
        
        print(part_1())

        # part 2
        def part_2():
            
            def simulate(guard_pos):
                visited = set()
                pos, dir = guard_pos, 'up'

                while True:
                    if (pos, dir) in visited:
                        return True
                    visited.add((pos, dir))

                    next_pos = turn_right(pos, dir)

                    if not valid_move(next_pos):
                        return False

                    if puzzle[next_pos[0]][next_pos[1]] in ['#', 'O']:
                        dir = next_direction(dir)
                        continue 

                    pos = next_pos

        
            loop_cases = 0
            for x in range(rows):
                for y in range(cols):
                    if (x, y) in unique_positions and puzzle[x][y] != '^':
                        puzzle[x][y] = 'O' 
                        if simulate(guard_pos): 
                            loop_cases += 1
                        puzzle[x][y] = '.'
        
            return loop_cases

        print(part_2())