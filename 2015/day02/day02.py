def load_file(file):
    with open(file) as f:
        values = [str(line) for line in f.readlines()]
    return values


def calculate_wrapping(length, width, height):
    side_one = length * width
    side_two = width * height
    side_three = height * length
    sides = [side_one, side_two, side_three]
    sides.sort()
    smallest_side = sides[0]
    total = (2 * side_one) + (2 * side_two) + (2 * side_three) + smallest_side
    return total


def calculate_ribbon(length, width, height):
    total = 0
    sides = [length, width, height]
    sides.sort()
    smallest_side = sides[0]
    second_smallest_side = sides[1]
    total += (smallest_side * 2) + (second_smallest_side * 2)
    return total


def part_one(file: str):
    raw_values = load_file(file)
    total=0
    for value in raw_values:
        dimensions = value.split("x")
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        result = calculate_wrapping(l, w, h)
        total += result
        print(f"result: {result}")
    print(f"total: {total}")


def part_two(file: str):
    raw_values = load_file(file)
    total = 0
    for value in raw_values:
        dimensions = value.split("x")
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        ribbon = calculate_ribbon(l, w, h)
        bow = l * w * h
        result = ribbon + bow
        total += result

        print(f"ribbon: {ribbon}")
        print(f"bow: {bow}")
        print(f"result: {result}")
        print("---------")

    print(f"total: {total}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
