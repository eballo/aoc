
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


def count_encoded_and_literal_characters(strings):
    total_encoded = 0
    total_literal = 0

    for s in strings:
        # Count literal characters
        literal_count = len(s)
        total_literal += literal_count

        # Encode the string and count encoded characters
        encoded_string = '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

        # Explanation:
        # s.replace('\\', '\\\\') -> This part replaces every single backslash (\) in the string with
        # double backslashes (\\).
        # For example: abc\def, it will become abc\\def.

        # next part .replace('"', '\\"') -> This part replaces every double quote (") in the string with an escaped
        # double quote (\").
        # For example: abc"def, it will become abc\"def.

        # Final example: 'abc"def\\ghi'
        # encoded string should be: "abc\"def\\ghi"

        encoded_count = len(encoded_string)
        total_encoded += encoded_count

    return total_encoded, total_literal


def part_one(file: str):
    raw_values = load_file(file)

    total_literal, total_memory = count_literal_and_memory_characters(raw_values)
    print(f"Total:{total_literal - total_memory}")


def part_two(file: str):
    raw_values = load_file(file)

    total_encoded, total_literal = count_encoded_and_literal_characters(raw_values)
    print(f"Total:{total_encoded - total_literal}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
