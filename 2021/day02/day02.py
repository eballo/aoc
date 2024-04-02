from typing import Tuple


def load_file(file: str) -> Tuple[str, int]:
    with open(file, "r") as f:
        for line in f:
            direction, value = line.split()
            yield direction, int(value)


def part_one(file: str) -> None:
    depth = 0
    horizontal = 0

    for direction, number in load_file(file):
        # print(f"direction {direction} - number {number}")
        match direction:
            case "forward":
                horizontal = horizontal + number
            case "down":
                depth = depth + number
            case "up":
                depth = depth - number
            case _:
                print("something went wrong!")

    print(f" horizontal {horizontal} - depth {depth}")
    print(f" total : {horizontal * depth}")


def part_two(file: str) -> None:
    depth = 0
    horizontal = 0
    aim = 0

    for direction, number in load_file(file):
        # print(f"direction {direction} - number {number}")
        match direction:
            case "forward":
                horizontal = horizontal + number
                depth = depth + (aim * number)
            case "down":
                aim = aim + number
            case "up":
                aim = aim - number
            case _:
                print("something went wrong!")

    print(f" horizontal {horizontal} - depth {depth}")
    print(f" total : {horizontal * depth}")


if __name__ == '__main__':
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
