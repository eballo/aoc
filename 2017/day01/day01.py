def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    raw_values = load_file(file)

    for values in raw_values:
        total = 0
        for x in range(1, len(values)):
            if values[x] == values[x - 1]:
                total += int(values[x])
        if values[0] == values[len(values)-1]:
            total += int(values[0])
        print(f"values : {total}")


def part_two(file: str):
    raw_values = load_file(file)

    for values in raw_values:
        total = 0
        for x in range(0, len(values)):
            if values[x] == values[int(x + len(values) / 2) % len(values)]:
                total += int(values[x])
        print(f"values : {total} - {values}")


if __name__ == "__main__":

    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
