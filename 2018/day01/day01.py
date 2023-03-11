def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    raw_values = load_file(file)

    total = 0
    for values in raw_values:
        total += int(values)
    print(f"values : {total}")


def part_two(file: str):
    raw_values = load_file(file)

    total_frequency = 0
    unique_frequency = {total_frequency}
    while True:
        for value in raw_values:
            total_frequency += int(value)
            if total_frequency in unique_frequency:
                print(f"unique value found : {total_frequency} ")
                return
            unique_frequency.add(total_frequency)
        # print(f"values : {total_frequency}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
