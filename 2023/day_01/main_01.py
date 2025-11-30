def part_1(file):
    ans = 0
    for row in file:
        row = [c for c in row if c.isdigit()]
        ans += int(row[0] + row[-1])

    print(ans)


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def find_first(row: str) -> str:
    ans = ""
    cur = float('inf')
    for digit in digits:
        try:
            i1 = row.index(digit)
            if i1 < cur:
                cur = i1
                ans = digits[digit]
        except ValueError:
            continue

    for d in range(10):
        try:
            i2 = row.index(str(d))
            if i2 < cur:
                cur = i2
                ans = str(d)
        except ValueError:
            continue
    
    return ans

def find_last(row: str) -> str:
    ans = ""
    cur = -1
    for digit in digits:
        try:
            i1 = row.rindex(digit)
            if i1 > cur:
                cur = i1
                ans = digits[digit]
        except ValueError:
            continue

    for d in range(10):
        try:
            i2 = row.rindex(str(d))
            if i2 > cur:
                cur = i2
                ans = str(d)
        except ValueError:
            continue
    
    return ans


def part_2(file):
    ans = 0
    for row in file:
        first = find_first(row)
        last = find_last(row)
        ans += int(first + last)

    print(ans)


if __name__ == "__main__":

    with open("puzzle.txt", "r") as file:
        # part_1(file)
        part_2(file)
