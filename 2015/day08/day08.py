
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def count_literal_and_memory_characters(strings):
    total_literal = 0
    total_memory = 0

    for s in strings:
        # Count literal characters
        literal_count = len(s)
        total_literal += literal_count

        # Count memory characters by evaluating the string
        memory_count = len(eval(s))
        total_memory += memory_count

    return total_literal, total_memory


def part_one(file: str):
    raw_values = load_file(file)

    total_literal, total_memory = count_literal_and_memory_characters(raw_values)
    print(f"Total:{total_literal - total_memory}")


def part_two(file: str):
    raw_values = load_file(file)

    for value in raw_values:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
