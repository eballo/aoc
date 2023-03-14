from typing import List

import numpy as np


def load_file(file: str) -> List[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    raw_values = load_file(file)
    total = 0
    for values in raw_values:
        values_list = []
        for value in values.split():
            values_list.append(int(value))
        max_value = np.max(values_list)
        min_value = np.min(values_list)
        total += max_value - min_value
        # print(f"values : {values_list} - {max_value} - {min_value} - {total}")
    print(f"values : {total}")


def part_two(file: str):
    raw_values = load_file(file)
    total = 0
    for values in raw_values:
        values_list = []
        for value in values.split():
            values_list.append(int(value))

        for x in range(0, len(values_list)):
            for y in range(0, len(values_list)):
                if x != y:
                    if values_list[x] % values_list[y] == 0:
                        # print(f"{values_list[x]} / {values_list[y]}")
                        result_division = int(values_list[x] / values_list[y])
                        # print(result_division)
                        total += result_division
        print(f"values : {values_list} - {total}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
