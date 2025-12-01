def part_1(file):
    ans = 0
    dial = 50
    for row in file:
        dir = row[0]
        times = int(row[1:])

        if dir == 'L':
            dial = (dial - times) % 100
        else:
            dial = (dial + times) % 100

        if dial == 0:
            ans += 1

    print(ans)

def part_2(file):
    ans = 0
    dial = 50
    for row in file:
        dir = row[0]
        times = int(row[1:])

        gz = times // 100
        ans += gz

        leftover = times % 100
        if dir == 'L':
            if dial != 0 and (dial - leftover) < 0:
                ans += 1
            dial = (dial - times) % 100

        else:
            if (dial + leftover) > 100:
                ans += 1
            dial = (dial + times) % 100

        if dial == 0:
            ans += 1

    print(ans)


if __name__ == "__main__":

    with open("puzzle.txt", "r") as file:
        rows = file.readlines()
        part_1(rows)
        part_2(rows)
