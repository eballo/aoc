from typing import Tuple


def load_file(file: str) -> Tuple[str, int]:
    with open(file, "r") as f:
        for line in f:
            values = line.split()
            if len(values) == 1:
                yield values[0], None
            else:
                yield values[0], int(values[1])


def handle_cycles(t, x, total):
    if t in [20, 60, 100, 140, 180, 220]:
        total += x * t
    return total


def part_one(file: str):
    raw_data = load_file(file)

    x = 1  # starting cycle
    t = 0
    total = 0

    for instruction, value in raw_data:
        # print(f" instruction {instruction}, value {value}")
        if instruction == "addx":
            t += 1
            total = handle_cycles(t, x, total)
            t += 1
            total = handle_cycles(t, x, total)
            x += value
        else:
            t += 1
            total = handle_cycles(t, x, total)

    print(f"What is the sum of these six signal strengths? {total}")


def part_two(file: str):
    raw_data = load_file(file)
    pass


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
