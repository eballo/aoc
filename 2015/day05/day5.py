
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def is_nice_string_part_one(text: str) -> bool:
    vowels = 'aeiou'
    disallowed_substrings = ['ab', 'cd', 'pq', 'xy']

    # 1 - Check contains at least three vowels
    vowel_count = sum(1 for char in text if char in vowels)
    if vowel_count < 3:
        return False

    # 2- Check contains at least one double letter
    has_double_letter = any(text[i] == text[i + 1] for i in range(len(text) - 1))
    if not has_double_letter:
        return False

    # 3 - Check for disallowed substrings
    if any(substring in text for substring in disallowed_substrings):
        return False

    # If all conditions (1 + 2 + 3) are met, the string is nice
    return True


def is_nice_string_part_two(text: str) -> bool:
    pairs = set()  # To store pairs of letters that appear twice without overlapping
    has_repeating_with_one_between = False  # Flag to indicate if the string contains repeating letter with one between

    for i in range(0, len(text) - 1):
        # 1 - Check for pairs of letters that appear twice without overlapping
        pair = text[i:i + 2]
        if pair in text[i + 2:]:
            pairs.add(pair)

        # 2 - Check for repeating letter with one between
        if i < len(text) - 2 and text[i] == text[i + 2]:
            has_repeating_with_one_between = True

    # Check if the string satisfies both conditions (1 + 2)
    return len(pairs) > 0 and has_repeating_with_one_between


def part_one(file: str):
    raw_values = load_file(file)

    counter = 0
    for value in raw_values:
        if is_nice_string_part_one(value):
            counter += 1

    print(f"We have a total of {counter} nice strings")


def part_two(file: str):
    raw_values = load_file(file)

    counter = 0
    for value in raw_values:
        if is_nice_string_part_two(value):
            counter += 1

    print(f"We have a total of {counter} nice strings")


if __name__ == "__main__":
    # print("=== Part 1 Input ==")
    # part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
