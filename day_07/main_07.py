
if __name__ == '__main__':

    with open('puzzle.txt') as f:
        _dict = {}
        for row in f:
            numbers = row.split(':')

            _dict[numbers[0]] = list(map(int, numbers[1].split()))
        
        from backtracking import Backtracking
        sol = Backtracking(_dict)
        print([sol.part_1(), sol.part_2()]) # 3s

        from _itertools import Itertools
        sol = Itertools(_dict)
        print([sol.part_1(), sol.part_2()]) # 21s





