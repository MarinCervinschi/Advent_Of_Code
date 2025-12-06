OP = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}


def part_1(numbers, operations):
    ans = [0 if op == "+" else 1 for op in operations]

    for i, n in enumerate(numbers):
        j = i % len(operations)
        ans[j] = OP[operations[j]](ans[j], int(n))

    print(sum(ans))


def part_2(data, operations):
    import numpy as np

    grid = [list(row) for row in data.strip().split("\n")[:-1]]
    grid = np.transpose(grid).tolist()

    ans = [0 if op == "+" else 1 for op in operations]
    j = 0
    for col in grid:
        n = "".join(col).strip()
        if n.isdigit():
            k = j % len(operations)
            ans[k] = OP[operations[k]](ans[k], int(n))
        else:
            j += 1

    print(sum(ans))


if __name__ == "__main__":
    from pathlib import Path
    import re

    PATH = Path(__file__).parent

    with open(PATH / "puzzle.txt", "r") as file:
        data = file.read()
        numbers = re.findall(r"\d+", data)
        operations = re.findall(r"[*+]", data)

        part_1(numbers, operations)
        part_2(data, operations)
