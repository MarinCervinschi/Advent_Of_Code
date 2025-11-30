from itertools import cycle, product

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        puzzle = []

        machine = []
        order = cycle(['A', 'B', 'Prize'])
        for row in f:
            row = row.strip()

            if row != '':
                button = next(order)
                row = row.split(':')    
                row = row[1].split(',')

                A = row[0].split('+') if button != 'Prize' else row[0].split('=')
                B = row[1].split('+') if button != 'Prize' else row[1].split('=')
                
                machine.append((button, int(A[1]), int(B[1])))
            else:
                temp1 = tuple([machine[i][1] for i in range(3)])
                temp2 = tuple([machine[i][2] for i in range(3)])
                puzzle.append([temp1, temp2])
                machine = []

        temp1 = tuple([machine[i][1] for i in range(3)])
        temp2 = tuple([machine[i][2] for i in range(3)])
        puzzle.append([temp1, temp2])


        # xA * 94(x) + xB * 22(x) = 8400
        # xA * 34(y) + xB * 67(y) = 5400

        def linear_eq():
            from sympy import symbols, Eq, solve

            xA, xB = symbols('xA xB')

            tokens = 0
            for row in puzzle:
                #print(row)
                eq1 = Eq(xA * row[0][0] + xB * row[0][1], row[0][2] + 10000000000000)
                eq2 = Eq(xA * row[1][0] + xB * row[1][1], row[1][2] + 10000000000000)

                solution = solve((eq1, eq2), (xA, xB))
                
                if solution[xA].is_integer and solution[xB].is_integer:
                    tokens += solution[xA] * 3 + solution[xB]

            print(f"Tokens ->> {tokens}")

        linear_eq()

        def brute_force(presses):
            
            def calc(times_press_A, button_A, times_press_B, button_B):
                return times_press_A * button_A + times_press_B * button_B
            
            tokens = 0
            for row in puzzle:

                combs = list(product(range(presses), repeat=2))

                for comb in combs:
                    a, b = comb[0], comb[1]
                    if a == 0 or b == 0:
                        continue
                    res_X = calc(a, row[0][0], b, row[0][1])
                    res_Y = calc(a, row[1][0], b, row[1][1])
                    if res_X == row[0][2] and res_Y == row[1][2]:
                        tokens += (a * 3 + b)
                        break


            print(f"Tokens ->> {tokens}")