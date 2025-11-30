
if __name__ == '__main__':

    with open('puzzle.txt') as f:
        # part 1
        list_of_numbers = f.read().split('\n')
        list_of_numbers = [i.split('  ') for i in list_of_numbers]
        list_left = [int(i[0]) for i in list_of_numbers]
        list_right = [int(i[1]) for i in list_of_numbers]
        _list_right = sorted(list_right)
        _list_left = sorted(list_left)
        print(sum(abs(l - r) for l, r in zip(_list_left, _list_right)))

         # part 2
        print(sum(l * list_right.count(l) for l, r in zip(list_left, list_right)))