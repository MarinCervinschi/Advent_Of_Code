import re
from copy import deepcopy

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = [] 

        for row in f:
            matches = re.findall(r'[-]?\d+', row)
            p_v = [int(match) for match in matches]
            puzzle.append([(p_v[0], p_v[1]), (p_v[2], p_v[3])])

        rows, cols = 103, 101
        
        def move(s, puzzle):
            k = 28
            for i in range(s):
                if i == k:
                    k += 101
                    with open('output_matrix.txt', 'a') as out_file:
                        for row in bathroom:
                            out_file.write(''.join(row) + '\n')

                        out_file.write(50 * '#' + '\n')
                        out_file.write(f"SECONDS -->> {i}\n\n")

                new_puzzle = []
                bathroom = [['.' for _ in range(cols)] for _ in range(rows)]
                for (y, x), (dy, dx) in puzzle:
                    y += dy
                    x += dx
                    if x >= rows:
                        x %= rows
                    if y >= cols:
                        y %= cols
                    if x <= -rows:
                        x = rows % x
                    if y <= -cols:
                        y = cols % y
                        
                    new_puzzle.append([(y, x), (dy, dx)])
                    
                    if bathroom[x][y] == '.':
                        bathroom[x][y] = '1'
                    else:
                        bathroom[x][y] = str(int(bathroom[x][y]) + 1)

                    
                puzzle = new_puzzle

            return bathroom
        
        def remove_X(matrix):

            new = deepcopy(matrix)

            for r in range(rows):
                for c in range(cols):
                    if c == cols // 2 or r == rows // 2:
                        new[r][c] = ' '

            return new

        bathroom = move(10000, puzzle)
        new = remove_X(bathroom)

        def split_into_quadrants(matrix):
            mid_row = rows // 2
            mid_col = cols // 2
            
            q1 = [row[:mid_col] for row in matrix[:mid_row]]
            
            q2 = [row[mid_col:] for row in matrix[:mid_row]]
            
            q3 = [row[:mid_col] for row in matrix[mid_row:]]
            
            q4 = [row[mid_col:] for row in matrix[mid_row:]]
            
            return q1, q2, q3, q4
        
        q1, q2, q3, q4 = split_into_quadrants(new)

        ans = 1
        for q in [q1, q2, q3, q4]:
            count = sum(int(i) for row in q for i in row if i.isdigit())
            ans *= count
       
        print(ans)