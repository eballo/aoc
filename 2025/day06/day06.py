# Generated on 06-12-2025 07:13
# --- Day 6: Trash Compactor ---
import math


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def get_matrix(raw_data: list[str], split=True) -> list[list[str]]:
    column = []
    for line in raw_data:
        row = []
        content = line.split(" ")
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
    lines = raw_data[:-1]
    operations = raw_data[-1]

    # print(lines)
    print(operations)

    # In the example the first two lines have 14
    # and the 3 line has 15, that is a problem!
    # let's find the max line and then do the padding
    # left if needed
    max_len = 0
    for line in lines:
        length = len(line)
        if max_len < length:
            max_len = length

    # print(f"max length line: {max_len}")

    # Normalize all lines to the same size
    padded_lines = [line.ljust(max_len) for line in lines]

    # Change lines to vertical alignment
    # get one by one the characters of that position and add
    # them as a column
    column = []
    for x in range(len(padded_lines[0])):
        col_value = []
        for line in padded_lines:
            col_value.append(line[x])
        column.append(col_value)

    # print(column)

    # for x in range(len(column)):
    #     for j in range(len(column[x])):
    #         print(column[x][j])

    # Cephalopod math is written right-to-left in columns
    cols_reversed = column[::-1]
    # print(cols_reversed)

    # I need to group all numbers
    # the problem is that some columns are 3 numbers and others are 4 others 2,
    # so I need to group all numbers in a list of values that needs to be calculated
    # if all the values in a list are empty means is the empty column
    problems = []
    current_problem = []

    for col in cols_reversed:
        if all(c == " " for c in col):
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)

    if current_problem:
        problems.append(current_problem)

    print(problems)

    # get the list of operations
    # the length should be the same as the problems
    operator = []
    for op in operations:
        if op != " ":
            operator.append(op)
    print(operator)
    assert len(problems) == len(operator)

    # reverse operators list too
    reversed_operator = operator[::-1]

    total = 0
    for x in range(0, len(problems)):
        print(f" Problem: {x}, numbers: {problems[x]}")
        numbers = []
        total_cols = 0
        for cols in problems[x]:
            # print(f"operator {reversed_operator[x]}, {cols}")
            numbers.append(int("".join(cols)))
        if reversed_operator[x] == "+":
            total_cols = sum(numbers)
        elif reversed_operator[x] == "*":
            total_cols = math.prod(numbers)
        print(f"total cols: {total_cols}")
        total += total_cols

    print(
        f"What is the grand total found by adding together all of the answers to the individual problems? {total}"
    )


if __name__ == "__main__":
    # print("=== Part 1 Example ==")
    # part_one("example.txt")
    #
    # print("=== Part 1 Input ==")
    # part_one("input.txt")

    print("=== Part 2 Example ==")
    part_two("example.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
