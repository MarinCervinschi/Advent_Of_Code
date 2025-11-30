
def solve(puzzle, word):
    rows, cols = len(puzzle), len(puzzle[0])
    word_len = len(word)

    def search(x, y, dx, dy):
        for i in range(word_len):
            if not (0 <= x < rows and 0 <= y < cols) or puzzle[x][y] != word[i]:
                return False
            x += dx
            y += dy
        return True
    
    def part_1():
        direction = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1),]

        find = 0
        for x in range(rows):
            for y in range(cols):
                for dir in direction:
                    if (search(x, y, dir[0], dir[1])):
                        find += 1

        return find
    
    def part_2():
        def valid(x, y, char):
           return (0 <= x < rows and 0 <= y < cols) and puzzle[x][y] == char
        
        find = 0
        for x in range(rows):
            for y in range(cols):
                if (puzzle[x][y] == 'A'):
                    if ((valid(x - 1, y -1, 'M') and valid(x + 1, y + 1, 'S')) or 
                        (valid(x - 1, y -1, 'S') and valid(x + 1, y + 1, 'M'))):
                        if ((valid(x + 1, y - 1, 'M') and valid(x - 1, y + 1, 'S')) or
                            (valid(x + 1, y - 1, 'S') and valid(x - 1, y + 1, 'M'))):
                                find += 1
                    
        return find
    
    return [part_1(), part_2()]

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [[c for c in row.strip()] for row in f]
        for row in puzzle:
            print(row)

        print(solve(puzzle, 'XMAS'))

        