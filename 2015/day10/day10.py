
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def look_and_say(sequence: str):
    result = []
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + sequence[i])
        i += 1
    return ''.join(result)


def part_one(file: str):
    raw_values = load_file(file)

    sequence = raw_values[0]
    process_times = 40

    for _ in range(process_times):
        sequence = look_and_say(sequence)

    print(f"the length of the result is: {len(sequence)}")


def part_two(file: str):
    raw_values = load_file(file)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
