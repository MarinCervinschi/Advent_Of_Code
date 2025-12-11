def part_1(graph):
    def dfs(node):
        if node == "out":
            return 1

        return sum(dfs(n) for n in graph[node])

    print(dfs("you"))


def part_2(graph):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(node, flag):
        if node == "out":
            return 1 if flag == 2 else 0

        count = 0
        for n in graph[node]:
            if n in ["dac", "fft"]:
                flag += 1
            count += dfs(n, flag)
            if n in ["dac", "fft"]:
                flag -= 1

        return count

    print(dfs("svr", 0))


def get_data(file_path):
    graph = {}
    with open(file_path, "r") as file:
        for row in file:
            row = row.strip().split()
            graph[row[0][:-1]] = row[1:]

    return graph


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    data = get_data(PATH / "puzzle.txt")
    part_1(data)
    part_2(data)