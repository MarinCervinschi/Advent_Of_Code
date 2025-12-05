def part_1(ids_range, ids):
    ranges = [(int(s), int(e)) for s, e in ids_range]
    id_list = [int(_id) for _id in ids]

    fresh = sum(any(s <= _id <= e for s, e in ranges) for _id in id_list)
    print(fresh)


def part_2(ids_range):
    pairs = sorted((int(s), int(e)) for s, e in ids_range)
    fresh = 0

    cur_s, cur_e = pairs[0]
    for new_s, new_e in pairs[1:]:
        if cur_e >= new_s:
            cur_e = max(cur_e, new_e)
        else:
            fresh += cur_e - cur_s + 1
            cur_s, cur_e = new_s, new_e

    fresh += cur_e - cur_s + 1
    print(fresh)


if __name__ == "__main__":
    from pathlib import Path
    import re

    PATH = Path(__file__).parent

    with open(PATH / "puzzle.txt", "r") as file:
        data = file.read()
        data = data.split("\n\n")
        ids_range = re.findall(r"(\d+)-(\d+)", data[0])
        ids = re.findall(r"\d+", data[1])

        part_1(ids_range, ids)
        part_2(ids_range)
