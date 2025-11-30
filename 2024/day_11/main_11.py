
def stupit(puzzle, blink):
    for _ in range(blink):
        new = []

        for num in puzzle:
            if num == '0':
                new.append('1')
            else:
                num_len = len(num)
                if num_len % 2 == 0:
                    half = num_len // 2
                    left, right = int(num[:half]), int(num[half:])
                    new.extend([str(left), str(right)])
                else:
                    new.append(str(int(num) * 2024))

        puzzle = new

    return len(new)

def tricky(puzzle, blinks):
    current_count = {}

    for num in puzzle:
        current_count[num] = current_count.get(num, 0) + 1
        
    for _ in range(blinks):
        new_count = {}
        for num, count in current_count.items():
            if num == 0:
                new_count[1] = new_count.get(1, 0) + count
            elif len(str(num)) % 2 == 0:
                half = len(str(num)) // 2
                left, right = int(str(num)[:half]), int(str(num)[half:])
                new_count[left] = new_count.get(left, 0) + count
                new_count[right] = new_count.get(right, 0) + count
            else:
                new_num = num * 2024
                new_count[new_num] = new_count.get(new_num, 0) + count

        current_count = new_count

    return sum(current_count.values())

if __name__ == '__main__':
    with open('puzzle.txt') as f:
        nums = f.read()
        puzzle = list(map(int, nums.split()))

        print(stupit(nums.split(), 25))
        print(tricky(puzzle, 75))
