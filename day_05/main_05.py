

if __name__ == '__main__':

    with open('puzzle.txt') as f:
        _dict = {}
        orders = []
        for row in f:
            row = row.strip()
            if '|' in row:
                numbers = list(map(int, row.split('|')))
                _dict.setdefault(numbers[0], []).append(numbers[1])
            elif row:
                orders.append(list(map(int, row.split(','))))
        
        def valid(order):
            flag = False
            for i in range(len(order) - 1):
                if (order[i] not in _dict.keys() or 
                    order[i + 1] not in _dict[order[i]]):
                    return False
                else:
                    flag = True

            return flag
        
        # part 1
        right_order, wrong_order = [], []
        [right_order.append(order) if valid(order) else wrong_order.append(order) for order in orders]

        print(sum(order[len(order) // 2] for order in right_order))
        
        # part 2
        for row in wrong_order:
            while(not valid(row)):
                for i in range(len(row) - 1):
                    if (row[i] not in _dict.keys() or 
                        row[i + 1] not in _dict[row[i]]):
                        row[i], row[i + 1] = row[i + 1], row[i]

        print(sum(order[len(order) // 2] for order in wrong_order))
        
            

        


