# Generated on 05-12-2025 07:30
# --- Day 5: Cafeteria ---
from typing import Any


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def get_ranges(value: str) -> list[int]:
    return [int(x) for x in value.split("-")]


def get_data(no_ingredients: bool, raw_data: list[str]) -> tuple[list[Any], list[Any]]:
    ranges_list = []
    ingredients = []
    for line in raw_data:
        # print(line)
        if line == "":
            no_ingredients = False

        if no_ingredients:
            ranges = get_ranges(line)
            ranges_list.append(ranges)
        elif line != "":
            ingredients.append(int(line))
    return ingredients, ranges_list


def part_one(file: str):
    raw_data = get_raw_data(file)
    no_ingredients = True
    ingredients, ranges_list = get_data(no_ingredients, raw_data)

    print(f"Ranges: {ranges_list}")
    print(f"Ingredients: {ingredients}")
    print("-----")

    is_fresh = set()
    for x in range(len(ingredients)):
        for j in range(len(ranges_list)):
            start, end = ranges_list[j]
            if start < ingredients[x] < end:
                is_fresh.add(ingredients[x])
                # print(f"Ingredient {ingredients[x]} is in {start} - {end}")
                break

    print(f"How many of the available ingredient IDs are fresh? {len(is_fresh)}")


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
