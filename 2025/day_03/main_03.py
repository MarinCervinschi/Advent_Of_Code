def solve(nums, size):
    ans = 0
    for num in nums:
        stack = []
        for i, d in enumerate(num):
            left = len(num) - i

            while stack and d > stack[-1] and len(stack) + left > size:
                stack.pop()

            if len(stack) < size:
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
        solve(nums, size=2)
        solve(nums, size=12)
