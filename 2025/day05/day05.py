# Generated on 05-12-2025 07:30
# --- Day 5: Cafeteria ---
from typing import Any


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def get_ranges(value: str) -> list[int]:
    return [int(x) for x in value.split("-")]


def get_data(raw_data: list[str]) -> tuple[list[Any], list[Any]]:
    no_ingredients = True
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


def get_merged_ranges(ranges_list: list[Any]) -> list[list[int]]:
    ranges_list.sort(key=lambda x: x[0])
    print(f"sorted ranges {ranges_list}")
    current_start, current_end = ranges_list[0]
    merged_ranges = []
    for j in range(1, len(ranges_list)):
        start, end = ranges_list[j]

        # overlap
        # If the next range starts inside (or immediately after) the current one
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            # No overlap
            merged_ranges.append([current_start, current_end])
            current_start, current_end = start, end

    merged_ranges.append([current_start, current_end])
    return merged_ranges


def part_one(file: str):
    raw_data = get_raw_data(file)
    ingredients, ranges_list = get_data(raw_data)

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
    _, ranges_list = get_data(raw_data)

    print(f"Ranges: {ranges_list}")
    print("-----")

    # NOTE: There are ranges with overlapping numbers
    # and this is causing issues
    # I want to make unique ranges that does not have overlap
    merged_ranges = get_merged_ranges(ranges_list)

    print(f"merged ranges {merged_ranges}")
    count = 0
    for j in range(len(merged_ranges)):
        start, end = merged_ranges[j]
        diff = end - start
        count += diff + 1
        # print(f" ranges {start}-{end}: {diff} - {count}")

    print(
        f"How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges? {count}"
    )


if __name__ == "__main__":
    print("=== Part 1 Example ==")
    part_one("example.txt")

    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Example ==")
    part_two("example.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
