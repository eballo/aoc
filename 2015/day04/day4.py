import hashlib


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def find_lowest_number_with_5_zeros(secret_key):
    number = 1
    while True:
        # Combine the secret key with the current number
        combined_key = secret_key + str(number)
        # Calculate the MD5 hash of the combined key
        hash_value = hashlib.md5(combined_key.encode()).hexdigest()
        # Check if the hash starts with at least five zeroes
        if hash_value[:5] == '00000':
            return number
        number += 1


def find_lowest_number_with_6_zeros(secret_key):
    number = 1
    while True:
        # Combine the secret key with the current number
        combined_key = secret_key + str(number)
        # Calculate the MD5 hash of the combined key
        hash_value = hashlib.md5(combined_key.encode()).hexdigest()
        # Check if the hash starts with at least five zeroes
        if hash_value[:6] == '000000':
            return number
        number += 1


def part_one(file: str):
    raw_values = load_file(file)

    secret_key = raw_values[0]
    number = find_lowest_number_with_5_zeros(secret_key)
    print(f"Lowest number for secret key {number}")


def part_two(file: str):
    raw_values = load_file(file)

    secret_key = raw_values[0]
    number = find_lowest_number_with_6_zeros(secret_key)
    print(f"Lowest number for secret key {number}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
