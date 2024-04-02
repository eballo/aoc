import math


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def calculate_required_fuel(value):
    return math.floor(int(value) / 3) - 2


def calculate_required_fuel_recursive(value):
    fuel = calculate_required_fuel(value)
    if int(fuel) <= 0:
        return 0
    return fuel + calculate_required_fuel_recursive(fuel)


def part_one(file: str):
    raw_values = load_file(file)
    total = 0
    for value in raw_values:
        total += calculate_required_fuel(int(value))
    print(total)


def part_two(file: str):
    raw_values = load_file(file)
    total = 0
    for value in raw_values:
        total += calculate_required_fuel_recursive(value)
    print(total)


if __name__ == "__main__":

    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
