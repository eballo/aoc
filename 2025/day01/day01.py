# Generated on 01-12-2025 07:12
# --- Day 1: Secret Entrance ---

def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values

def parse_data(raw_data: list[str]) -> list[(str, int)]:
    """
    Parse raw data into a list of tuples of string and integers.
    the first part is always the first word, the second part is always the integer following it.
    sample input: ["R412", "L3", "R2", "R4", "L2", L1"]
    """
    parsed = []
    for line in raw_data:
        direction = line[0]
        distance = int(line[1:])
        parsed.append((direction, distance))
    return parsed


def calculate_rotations(parsed: list[tuple[str, int]])-> int:
    """
    Calculate the rotations based on the parsed data.
    numbers goes from 0 to 99 and directions is R or  L.
    everytime that we meet 0 or 99 we need to increase the rotation counter by 1.
    We start at 50.
    """
    rotation = 50
    times_is_around = 0
    for direction, distance in parsed:
        if direction == "R":
            rotation += distance
        elif direction == "L":
            rotation -= distance

        while rotation < 0:
            rotation += 100
        while rotation >= 100:
            rotation -= 100

        if rotation == 0:
            times_is_around += 1
        # print(f"Current rotation: {rotation}")
    return times_is_around

def calculate_rotations_always(parsed: list[tuple[str, int]])-> int:
    """
    Calculate the rotations based on the parsed data.
    numbers goes from 0 to 99 and directions is R or  L.
    everytime that we meet 0 or 99 we need to increase the rotation counter by 1.
    We need to count every time we pass through 0.

    Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

    We start at 50.
    """
    rotation = 50
    times_is_around = 0

    for direction, distance in parsed:
        for _ in range(distance):
            if direction == "R":
                rotation += 1
                if rotation == 100:
                    rotation = 0
            elif direction == "L":
                rotation -= 1
                if rotation == -1:
                    rotation = 99

            if rotation == 0:
                times_is_around += 1
    return times_is_around


def part_one(file: str):
    raw_data = get_raw_data(file)

    parsed = parse_data(raw_data)
    # for direction, distance in parsed:
    #     print(f"Direction: {direction}, Distance: {distance}")
    rotation = calculate_rotations(parsed)
    print(f"What's the actual password to open the door?{rotation}")

def part_two(file: str):
    raw_data = get_raw_data(file)

    parsed = parse_data(raw_data)
    rotation = calculate_rotations_always(parsed)
    print(f"What's the actual password to open the door?{rotation}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")