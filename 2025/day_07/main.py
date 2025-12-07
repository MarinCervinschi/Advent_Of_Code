from re import split


def part_1(grid, start):

    up = (-1, 0)
    current_positions = [start]
    splits = 0
    rows, cols = len(grid), len(grid[0])
    for r in range(1, rows):
        for c in range(cols):
            nx, ny = r + up[0], c + up[1]

            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) in current_positions:
                    if grid[r][c] == "^":
                        splits += 1
                        grid[r][c - 1] = "|"
                        grid[r][c + 1] = "|"
                        current_positions.append((r, c + 1))
                        current_positions.append((r, c - 1))
                    else:
                        grid[r][c] = "|"
                        current_positions.append((r, c))
    print(splits)
    return grid


def part_2(grid, start_col):
    rows, cols = len(grid), len(grid[0])

    dp = [[0] * cols for _ in range(rows)]
    dp[1][start_col] = 1
    for r in range(1, rows - 1):
        for c in range(cols):
            if dp[r][c] > 0:
                if grid[r][c] == "|":
                    dp[r + 1][c] += dp[r][c]
                elif grid[r][c] == "^":
                    dp[r + 1][c + 1] += dp[r][c]
                    dp[r + 1][c - 1] += dp[r][c]

    end_paths = [i for i, c in enumerate(grid[-1]) if c == "|"]
    print(sum(dp[-1][c] for c in end_paths))


def get_data(file_path):
    with open(file_path, "r") as file:
        data = [list(row.strip()) for row in file]
    return data


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    data = get_data(PATH / "puzzle.txt")
    start = data[0].index("S")
    grid = part_1(grid=data, start=(0, start))
    part_2(grid=grid, start_col=start)
