# Generated on 03-12-2024 19:33
# --- Day 3: Mull It Over ---

import re

def get_raw_data(file: str) -> str:
    with open(file) as f:
        line = f.read().strip()
    return line


def part_one(file: str):
    raw_data = get_raw_data(file)
    results = re.findall(r"mul\((\d+),(\d+)\)",raw_data)

    print(results)
    total =0
    for instruction in results:
        total += int(instruction[0]) * int(instruction[1])

    print(f"What do you get if you add up all of the results of the multiplications? {total}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    print(raw_data[0])



if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")