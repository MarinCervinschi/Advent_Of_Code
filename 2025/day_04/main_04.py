from copy import deepcopy


def _print(m):
    for row in m:
        print("".join(row))

    print(50 * "-")


DIRECTIONS = [
    (1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (-1, 0),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def part_1(grid):
    rows, cols = len(grid), len(grid[0])
    rolls = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                can_accessed = 0
                for x, y in DIRECTIONS:
                    nx, ny = r + x, c + y
                    if (0 <= nx < rows) and (0 <= ny < cols):
                        if grid[nx][ny] == "@":
                            can_accessed += 1
                if can_accessed < 4:
                    rolls += 1

    print(rolls)


def part_2(grid):
    rows, cols = len(grid), len(grid[0])
    rolls = 0

    while True:
        cur_rolls = 0
        temp = deepcopy(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    can_accessed = 0
                    for x, y in DIRECTIONS:
                        nx, ny = r + x, c + y
                        if (0 <= nx < rows) and (0 <= ny < cols):
                            if grid[nx][ny] == "@":
                                can_accessed += 1
                    if can_accessed < 4:
                        temp[r][c] = "."
                        cur_rolls += 1

        grid = temp
        rolls += cur_rolls
        if cur_rolls == 0:
            break

    print(rolls)


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    with open(PATH / "puzzle.txt", "r") as file:
        grid = []
        for row in file:
            grid.append(list(row.strip()))

        # _print(grid)
        part_1(grid)
        part_2(grid)
