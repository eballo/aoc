def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def increment_password(password: str):
    """ Increment the password by treating it as a base-26 number """
    pw = list(password)
    for i in range(len(pw) - 1, -1, -1):
        if pw[i] == 'z':
            pw[i] = 'a'
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break
    return ''.join(pw)


def has_increasing_straight(password):
    """ Check for at least one increasing straight of three letters """
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(password[i + 2]):
            return True
    return False


def has_no_invalid_letters(password):
    """ Check that password does not contain 'i', 'o', or 'l' """
    return all(c not in password for c in 'iol')


def has_two_non_overlapping_pairs(password):
    """ Check for at least two different, non-overlapping pairs of letters """
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2


def is_valid_password(password):
    """ Check if the password meets all the criteria """
    return (has_increasing_straight(password) and
            has_no_invalid_letters(password) and
            has_two_non_overlapping_pairs(password))


def next_valid_password(password: str):
    """ Generate the next valid password """
    password = increment_password(password)
    while not is_valid_password(password):
        password = increment_password(password)
    return password


def part_one(file: str):
    raw_values = load_file(file)

    next_password = next_valid_password(raw_values[0])
    print(f"Next valid password after {raw_values[0]} is {next_password}")


def part_two(file: str):
    raw_values = load_file(file)

    raw_values = load_file(file)

    next_password1 = next_valid_password(raw_values[0])
    next_password2 = next_valid_password(next_password1)
    print(f"Next valid password after {raw_values[0]} is {next_password1} and after is {next_password2}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
