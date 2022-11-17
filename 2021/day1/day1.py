def load_file(file):
    with open(file) as f:
        values = [int(line) for line in f.readlines()]
    return values


def part_one(file: str):
    values = load_file(file)

    # print(values)

    count = 0
    previous_value = values[0]
    for x in range(1, len(values)):
        # print(f"{previous_value} - {values[x]} -  {previous_value < values[x]}")
        if previous_value < values[x]:
            count = count + 1

        previous_value = values[x]

    print(f"Increase times {count}")


def part_two(file: str):
    raw_values = load_file(file)

    # print(raw_values)
    #
    # for i in range(1, 4):
    #     print(f"{raw_values[i - 1]} + {raw_values[i]} + {raw_values[i + 1]}")

    values = [raw_values[i - 1] + raw_values[i] + raw_values[i + 1] for i in range(1, len(raw_values)-1)]

    # print(values)

    count = 0
    previous_value = values[0]
    for x in range(1, len(values)):
        # print(f"{previous_value} - {values[x]} -  {previous_value < values[x]}")
        if previous_value < values[x]:
            count = count + 1

        previous_value = values[x]

    print(f"Increase times {count}")


if __name__ == "__main__":
    part_one("test.txt")
    part_one("input.txt")
    part_two("test.txt")
    part_two("input.txt")
