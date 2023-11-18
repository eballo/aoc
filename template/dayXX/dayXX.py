
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    # Find the two entries that sum to 2020; what do you get if you multiply them together?
    raw_values = load_file(file)

    for value in range(len(raw_values)):
        print(value)


def part_two(file: str):
    raw_values = load_file(file)
    for value in range(len(raw_values)):
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    # print("=== Part 1 Input ==")
    # part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
