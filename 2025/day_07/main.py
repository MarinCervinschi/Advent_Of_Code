from collections import Counter


def solve(grid, start_col):

    dp = Counter()

    dp[start_col] = 1
    splits = 0
    for r in range(1, len(grid)):
        next_dp = Counter()
        for c, count in dp.items():
            if grid[r][c] == "^":
                splits += 1

                next_dp[c - 1] += count
                next_dp[c + 1] += count
            else:
                next_dp[c] += count
        dp = next_dp

    print(splits)
    print(dp.total())


def get_data(file_path):
    with open(file_path, "r") as file:
        data = [list(row.strip()) for row in file]
    return data


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    data = get_data(PATH / "puzzle.txt")
    start_col = data[0].index("S")
    solve(grid=data, start_col=start_col)
