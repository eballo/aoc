import json
from typing import Any


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def calculate_sum_all_numbers(json_data: Any):
    if isinstance(json_data, int):
        return json_data
    elif isinstance(json_data, list):
        return sum(calculate_sum_all_numbers(item) for item in json_data)
    elif isinstance(json_data, dict):
        return sum(calculate_sum_all_numbers(value) for value in json_data.values())
    return 0


def calculate_sum_all_numbers_not_red(json_data: Any):
    if isinstance(json_data, int):
        return json_data
    elif isinstance(json_data, list):
        return sum(calculate_sum_all_numbers_not_red(item) for item in json_data)
    elif isinstance(json_data, dict):
        if "red" in json_data.values():
            return 0
        return sum(calculate_sum_all_numbers_not_red(value) for value in json_data.values())
    return 0


def part_one(file: str):
    raw_values = load_file(file)

    json_data = json.loads(raw_values[0])
    total_sum = calculate_sum_all_numbers(json_data)
    print(f"Sum of all numbers: {total_sum}")


def part_two(file: str):
    raw_values = load_file(file)

    json_data = json.loads(raw_values[0])
    total_sum = calculate_sum_all_numbers_not_red(json_data)
    print(f"Sum of all numbers: {total_sum}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
