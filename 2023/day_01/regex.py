import re

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


def part_1(file):
    ans = 0
    for row in file:
        matches = re.findall(r"(?=(\d))", row)
        ans += int(matches[0] + matches[-1])

    print(ans)


def part_2(file):
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    ans = 0
    for row in file:
        matches = re.findall(pattern, row)
        first = digits.get(matches[0], matches[0])
        last = digits.get(matches[-1], matches[-1])

        assert isinstance(first, str)
        assert isinstance(last, str)

        ans += int(first + last)

    print(ans)


if __name__ == "__main__":

    with open("puzzle.txt", "r") as file:
        # part_1(file)
        part_2(file)
