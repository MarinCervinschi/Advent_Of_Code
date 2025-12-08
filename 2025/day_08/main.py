from collections import defaultdict
from math import prod
import heapq


def part_1(data):
    LIMIT = len(data)
    heap = get_heap(data)

    parent = list(range(len(data)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    for _ in range(LIMIT):
        _, p1, p2 = heapq.heappop(heap)
        union(p1, p2)

    circuits = defaultdict(set)
    for i in range(len(data)):
        circuits[find(i)].add(i)

    circuits_size = [len(c) for c in circuits.values()]

    circuits_size.sort(reverse=True)
    print(prod(circuits_size[:3]))


def get_heap(data):
    heap = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            dist = euclidian_distance(data[i], data[j])

            heapq.heappush(heap, (dist, i, j))
    return heap


def part_2(data):

    heap = get_heap(data)
    parent = list(range(len(data)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[px] = py
        return True

    components = len(data)
    while heap:
        _, p1, p2 = heapq.heappop(heap)
        if union(p1, p2):
            components -= 1
            if components == 1:
                break

    print(data[p1].x * data[p2].x)


class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)


def euclidian_distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2) ** 0.5


def get_data(file_path):
    import re

    with open(file_path, "r") as file:
        data = re.findall(r"(\d+),(\d+),(\d+)", file.read())
        points = [Point(x, y, z) for x, y, z in data]
    return points


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    points = get_data(PATH / "puzzle.txt")
    part_1(points)
    part_2(points)
