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


def is_periodic_id(number: int) -> bool:
    """
    Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice.
    Examples:
      11 (1 repeated 2x) -> True
      111 (1 repeated 3x) -> True
      121212 (12 repeated 3x) -> True
      123123 (123 repeated 2x) -> True
      123123123 (123 repeated 3x) -> True
      123124 (not a repetition) -> False
    """
    s = str(number)
    length = len(s)

    # Divide the string lenth by 2 and round down to get the max chunk size
    for chunk_len in range(1, (length // 2) + 1):

        # only consider chunk lengths that divide evenly into the string length
        if length % chunk_len == 0:
            # get the chunk pattern
            pattern = s[:chunk_len]
            # determine how many times it should repeat
            multiplier = length // chunk_len

            # Reconstruct what the string should look like
            if pattern * multiplier == s:
                return True
    return False


def part_one(file: str):
    raw_data = get_raw_data(file)
    list_of_values = raw_data[0].split(",")
    invalid_ids_found = []
    for value in list_of_values:
        first, last = value.split("-")
        # print(first, last)
        for num in range(int(first), int(last) + 1):
            if is_repeated_sequence(num):
                invalid_ids_found.append(num)

    print(f"Found {len(invalid_ids_found)} invalid IDs.")
    print(
        f"What do you get if you add up all of the invalid IDs? {sum(invalid_ids_found)}"
    )


def part_two(file: str):
    raw_data = get_raw_data(file)
    list_of_values = raw_data[0].split(",")
    invalid_ids_found = []
    for value in list_of_values:
        first, last = value.split("-")
        # print(first, last)
        for num in range(int(first), int(last) + 1):
            if is_periodic_id(num):
                invalid_ids_found.append(num)

    print(
        f"What do you get if you add up all of the invalid IDs using these new rules? {sum(invalid_ids_found)}"
    )


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
