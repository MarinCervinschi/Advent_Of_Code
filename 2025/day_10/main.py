def solve(data):
    part_1, part_2 = 0, 0
    for light, buttons, joltage in zip(*data):
        b1 = [int("".join(b), 2) for b in buttons]
        part_1 += bfs_1(goal=light, buttons=b1)

        b2 = [list(map(int, b)) for b in buttons]
        part_2 += solve_with_z3(goal=joltage, buttons=b2)

    print(part_1, part_2)


def bfs_1(goal, buttons):
    from collections import deque

    visited = set()
    queue = deque([(0, 0)])  # press count, state

    while queue:
        curr, state = queue.popleft()

        if state == goal:
            return curr

        for button in buttons:
            next_state = state ^ button

            if next_state not in visited:
                visited.add(next_state)
                queue.append((curr + 1, next_state))

    return -1


# sum x_i * button_i[r] = goal[r]
def solve_with_z3(goal, buttons):
    from z3 import Optimize, Int, Sum, sat

    s = Optimize()

    x = [Int(f"x_{i}") for i in range(len(buttons))]

    # Add constraint: presses must be non-negative
    for var in x:
        s.add(var >= 0)

    # Add constraint: For each counter, sum of button effects = goal
    num_counters = len(goal)
    for r in range(num_counters):
        row_sum = 0
        for col, btn in enumerate(buttons):
            row_sum += x[col] * btn[r]
        s.add(row_sum == goal[r])

    s.minimize(Sum(x))

    if s.check() == sat:
        model = s.model()
        return sum(model[v].as_long() for v in x)  # type: ignore
    else:
        return 0


def get_data(file_path):
    import re

    with open(file_path, "r") as file:
        lights = []
        buttons = []
        joltages = []
        for row in file:
            row_buttons = []
            line = row.split(" ")
            goal = "".join(["0" if c == "." else "1" for c in line[0][1:-1]])
            lights.append(int(goal, 2))
            temp = re.findall(r"\(([\d,]+)\)", row)
            for b in temp:
                button = ["0"] * len(goal)
                for i in b.split(","):
                    button[int(i)] = "1"
                row_buttons.append(button)
            buttons.append(row_buttons)
            joltages.append(
                [int(x) for x in re.findall(r"\{([\d,]+)\}", line[-1])[0].split(",")]
            )

    return lights, buttons, joltages


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    data = get_data(PATH / "puzzle.txt")
    solve(data)
