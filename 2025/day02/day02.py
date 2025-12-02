# Generated on 02-12-2025 07:06
# --- Day 2: Gift Shop ---


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def is_repeated_sequence(number: int) -> bool:
    """
    Checks if the number is made of a sequence repeated twice.
    Examples: 55, 6464, 123123.
    """
    s = str(number)
    length = len(s)

    # If length is odd, it can't be split into two equal parts
    if length % 2 != 0:
        return False

    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]

    return first_half == second_half


def part_one(file: str):
    raw_data = get_raw_data(file)
    list_of_values = raw_data[0].split(",")
    invalid_ids_found = []
    for value in list_of_values:
        first, last = value.split("-")
        print(first, last)
        for num in range(int(first), int(last) + 1):
            if is_repeated_sequence(num):
                invalid_ids_found.append(num)

    print(f"Found {len(invalid_ids_found)} invalid IDs.")
    print(
        f"What do you get if you add up all of the invalid IDs?{sum(invalid_ids_found)}"
    )


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
