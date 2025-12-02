def part_1(row):
    row = row.strip().split(',')
    ids = [r.split('-') for r in row]
    ans = 0
    for s, e in ids:
        for id in range(int(s), int(e) + 1):
            id = str(id)
            n = len(id)
            if n % 2 != 0:
                continue

            if id[:n // 2] == id[n // 2:]:
                ans += int(id)

    print(ans)


def part_2(row):
    row = row.strip().split(',')
    ids = [r.split('-') for r in row]
    ans = 0
    for s, e in ids:
        for id in range(int(s), int(e) + 1):
            id = str(id)
            new = id + id
            new = new[1:-1]
            if id in new:
                ans += int(id)

    print(ans)


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    with open(PATH / "puzzle.txt", "r") as file:
        rows = file.read()
        part_1(rows)
        part_2(rows)
