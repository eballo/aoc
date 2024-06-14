from typing import List


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def parse_input(raw_values: List[str]) -> List[List[int]]:
    triangle = []
    for line in raw_values:
        triangle.append(list(map(int, line.split())))
    return triangle


def is_valid_triangle(triangle: List[int]) -> bool:
    a, b, c = sorted(triangle)
    return a + b > c


def calculate_how_many_are_valid(triangles: List[List[int]]) -> int:
    valid = 0
    for triangle in triangles:
        if is_valid_triangle(triangle):
            valid += 1
    return valid


def calculate_how_many_are_valid_by_column(triangles: List[List[int]]) -> int:
    valid = 0
    for i in range(0, len(triangles), 3):
        group = triangles[i:i + 3]  # group the first 3 rows
        # print(group)
        # There should always be 3 lines in a group, or skip if less
        if len(group) < 3:
            continue
        # Transpose the lines to get columns
        for j in range(0, 3):
            sides = [group[0][j], group[1][j], group[2][j]]
            if is_valid_triangle(sides):
                valid += 1
    return valid


def part_one(file: str):
    raw_values = load_file(file)

    triangles = parse_input(raw_values)
    # print(triangles)
    total_valid = calculate_how_many_are_valid(triangles)
    print(f"how many of the listed triangles are possible? {total_valid}")


def part_two(file: str):
    raw_values = load_file(file)
    triangles = parse_input(raw_values)
    # print(triangles)
    total_valid = calculate_how_many_are_valid_by_column(triangles)
    print(f"how many of the listed triangles are possible? {total_valid}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
