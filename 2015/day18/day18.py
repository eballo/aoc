from typing import List


def load_file(file):
    with open(file) as f:
        values = [list(line.rstrip()) for line in f.readlines()]
    return values

# Notes:
# 100 X 100 maximum
#  A # means "on", and a . means "off".
# The rules for updating the state of each light are:
# - A light that is on (#) stays on if 2 or 3 neighbors are on, and turns off otherwise.
# - A light that is off (.) turns on if exactly 3 neighbors are on, and stays off otherwise.


def count_neighbors_lights_on(grid: List[List[str]], x: int, y: int) -> int:
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '#':
            count += 1
    return count


def calculate_next_state(grid: List[List[str]]) -> List[List[str]]:
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[0])):
            neighbors_on = count_neighbors_lights_on(grid, i, j)
            if grid[i][j] == '#' and neighbors_on in [2, 3]:
                new_row.append('#')
            elif grid[i][j] == '.' and neighbors_on == 3:
                new_row.append('#')
            else:
                new_row.append('.')
        new_grid.append(new_row)
    return new_grid


def calculate_total_lights_on(grid: List[List[str]], steps: int) -> int:
    for _ in range(steps):
        grid = calculate_next_state(grid)

    lights_on = sum(row.count('#') for row in grid)
    return lights_on


def part_one(file: str):
    grid = load_file(file) # load grid 100x100
    # print(grid)
    total_lights = calculate_total_lights_on(grid, 100)
    print(f"how many lights are on after 100 steps? {total_lights}")


def part_two(file: str):
    raw_values = load_file(file)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
