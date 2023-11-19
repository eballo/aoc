
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    # Find the two entries that sum to 2020; what do you get if you multiply them together?
    raw_values = load_file(file)

    total_valid = 0
    total_invalid =0
    for line in raw_values:
        columns = line.split(" ")
        min_max = columns[0].split("-")
        min = int(min_max[0])
        max = int(min_max[1])
        letter = columns[1].replace(":", "")
        password = columns[2]
        count = password.count(letter)
        if count >= min and count <= max:
            print(f"{line} is valid")
            total_valid += 1
        else:
            print(f"{line} is not valid")
            total_invalid += 1
    print(f"Total valid passwords: {total_valid}")
    print(f"Total invalid passwords: {total_invalid}")


def part_two(file: str):
    raw_values = load_file(file)
    for value in range(len(raw_values)):
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
