from itertools import combinations
from typing import List


def load_file(file):
    with open(file) as f:
        values = [int(line.rstrip()) for line in f.readlines()]
    return values


def find_total_different_combinations(raw_values: List[int], liters: int):
    total_different_combinations = 0
    for i in range(1, len(raw_values) + 1):
        for combo in combinations(raw_values, i):
            # print(i, combo)
            if sum(combo) == liters:
                # print(f"found! {i}, {combo}")
                total_different_combinations += 1
    return total_different_combinations


def part_one(file: str):
    raw_values = load_file(file)

    print(raw_values)
    result = find_total_different_combinations(raw_values, 150)
    print(f"How many different combinations of containers can exactly fit all 150 liters of eggnog? {result}")


def part_two(file: str):
    raw_values = load_file(file)

    for value in raw_values:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
