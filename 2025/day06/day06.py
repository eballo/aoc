# Generated on 06-12-2025 07:13
# --- Day 6: Trash Compactor ---
import math


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def get_matrix(raw_data: list[str]) -> list[list[str]]:
    column = []
    for line in raw_data:
        row = []
        content = line.split()
        for data in content:
            if data.isdigit():
                row.append(int(data))
            else:
                row.append(data)
        column.append(row)
    return column


def part_one(file: str):
    raw_data = get_raw_data(file)
    matrix = get_matrix(raw_data)

    # for c in range(len(matrix)):
    #     for r in range(len(matrix[c])):
    #         print(f" column {c} row {r} : {matrix[c][r]}")
    # print("----")

    # iterate by columns to get the numbers
    total = 0
    for c in range(len(matrix[0])):
        numbers = []
        for r in range(len(matrix)):
            # print(f" column {c} row {r} : {matrix[r][c]}")
            if r == len(matrix) - 1:
                operation = matrix[r][c]
                print(numbers, operation)
                if operation == "+":
                    o_total = sum(numbers)
                elif operation == "*":
                    o_total = math.prod(numbers)
                total += o_total
            numbers.append(matrix[r][c])

    print(
        f"What is the grand total found by adding together all of the answers to the individual problems? {total}"
    )


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Example ==")
    part_one("example.txt")

    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
