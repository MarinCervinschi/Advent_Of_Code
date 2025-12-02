import re


def solve(ids, pattern):
    ans = 0
    for i in range(0, len(ids), 2):
        s, e = int(ids[i]), int(ids[i + 1])
        for id in range(s, e + 1):
            id_str = str(id)
            if re.fullmatch(pattern, id_str):
                ans += id
    print(ans)


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    with open(PATH / "puzzle.txt", "r") as file:
        ids = re.findall(r"\d+", file.read())
        # part 1
        solve(ids, pattern=r"(\d+)\1")
        # part 2
        solve(ids, pattern=r"(\d+)\1+")
