# Generated on 26-10-2025 17:36
# Day 3: Spiral Memory
import math

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def calculate_steps_back_to_origin(start_position: int)-> int:
    # 1) Find the ring -> k = ceil((sqrt(n) - 1) / 2)
    # 2) Find the largest value on that ring -> m = (2k + 1)^2
    # 3) Find the midpoints of each side
    #   They’re m - k, m - 3k, m - 5k, m - 7k.
    #   offset = abs( ( (n - (m - k)) mod (2k) ) - k )
    # 4) Total manhattan distance -> distance = k + offset

    if start_position == 1:
        return 0
    ring = math.ceil((math.sqrt(start_position) - 1) / 2)  # ring index
    max_value = (2 * ring + 1) ** 2  # max value on ring
    side = 2 * ring  # steps per side
    # distance from n to the nearest side midpoint on this ring
    # compute position along the ring starting at the corner m and going backwards
    pos = (max_value - start_position) % (4 * side)
    # midpoints occur at side//2 before each corner when walking backwards
    # equivalently, distance to nearest of {side//2, 3*side//2, 5*side//2, 7*side//2}
    offset = min(abs(pos - side // 2),
                 abs(pos - 3 * side // 2),
                 abs(pos - 5 * side // 2),
                 abs(pos - 7 * side // 2))
    return ring + offset


def part_one(file: str):
    raw_data = get_raw_data(file)
    start_position = int(raw_data[0])

    total_steps = calculate_steps_back_to_origin(start_position)
    print(f"total steps from {start_position} to 1: {total_steps}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")