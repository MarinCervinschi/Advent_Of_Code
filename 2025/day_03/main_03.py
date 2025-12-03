def part_1(nums):
    ans = 0
    first = last = 0
    for num in nums:
        temp = max(num)
        i = num.index(temp)
        if i == len(num) - 1:
            last = temp
            first = max(num[:-1])
        else:
            first = temp
            last = max(num[i + 1 :])

        ans += int(str(first) + str(last))

    print(ans)


def part_2(nums):
    ans = 0
    for num in nums:
        stack = []
        for i, d in enumerate(num):

            left = len(num) - i

            while stack and d > stack[-1] and len(stack) + left > 12:
                stack.pop()

            if len(stack) < 12:
                stack.append(d)

        temp = "".join(stack)
        ans += int(temp)

    print(ans)


if __name__ == "__main__":
    from pathlib import Path
    import re

    PATH = Path(__file__).parent

    with open(PATH / "puzzle.txt", "r") as file:
        nums = re.findall(r"\d+", file.read())
        part_1(nums)
        part_2(nums)
