import numpy as np


def part_1(data):
    raw_shapes, regions = data

    shape_areas = [np.sum(s) for s in raw_shapes]

    lookup = {}
    for i, s in enumerate(raw_shapes):
        variations = set()
        curr = np.array(s, dtype=bool)

        for _ in range(4):
            curr = np.rot90(curr)
            variations.add(tuple(map(tuple, curr)))
            variations.add(tuple(map(tuple, np.fliplr(curr))))

        lookup[i] = [np.array(v, dtype=bool) for v in variations]

    def solve_region(width, length, list_of_presents):
        memo = {}

        def grid_hash(grid):
            ys, xs = np.where(grid)
            if len(xs) == 0:
                return 0
            miny, maxy = ys.min(), ys.max()
            minx, maxx = xs.min(), xs.max()
            return hash(grid[miny : maxy + 1, minx : maxx + 1].tobytes())

        def dfs(grid, present_indices):
            if not present_indices:
                return True

            grid_key = grid_hash(grid)
            presents_key = tuple(present_indices)
            cache_key = (grid_key, presents_key)

            if cache_key in memo:
                return memo[cache_key]

            empty_area = np.sum(~grid)
            needed_area = sum(shape_areas[idx] for idx in present_indices)
            if empty_area < needed_area:
                memo[cache_key] = False
                return False

            next_present_idx = present_indices[0]
            remaining_indices = present_indices[1:]

            for shape_arr in lookup[next_present_idx]:
                grid_h, grid_w = grid.shape
                h, w = shape_arr.shape

                for r in range(grid_h - h + 1):
                    for c in range(grid_w - w + 1):
                        region = grid[r : r + h, c : c + w]

                        if not np.any(region & shape_arr):
                            grid[r : r + h, c : c + w] |= shape_arr

                            if dfs(
                                grid,
                                remaining_indices,
                            ):
                                memo[cache_key] = True
                                return True

                            grid[r : r + h, c : c + w] &= ~shape_arr

            memo[cache_key] = False
            return False

        grid = np.zeros((length, width), dtype=bool)
        return dfs(grid, list_of_presents)

    fit_all = 0
    from tqdm import tqdm

    for region in tqdm(regions):
        width, length = region[:2]

        list_of_presents = []
        for shape_idx, quantity in enumerate(region[2:]):
            list_of_presents.extend([shape_idx] * quantity)

        list_of_presents.sort(key=lambda x: shape_areas[x], reverse=True)

        empty_area = width * length
        needed_area = sum(shape_areas[idx] for idx in list_of_presents)
        if empty_area < needed_area:
            continue

        if solve_region(width, length, list_of_presents):
            fit_all += 1

    print(f"Part 1: {fit_all} regions can fit all presents.")


def get_data(file_path):
    import re

    shapes = []
    regions = []
    with open(file_path, "r") as file:
        shape_flag = False
        index = -1
        for row in file:
            row = row.strip()
            m = re.findall(r"\d+", row)
            if m and "x" not in row:
                index = int(m[0])
                shapes.append([])
                shape_flag = True
                continue
            elif m and "x" in row:
                regions.append(tuple(map(int, m)))
                shape_flag = False
            if shape_flag:
                if row == "":
                    shape_flag = False
                    continue
                shapes[index].append([1 if c == "#" else 0 for c in row])

    return shapes, regions


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    data = get_data(PATH / "puzzle.txt")
    part_1(data) # 2 min 35s
