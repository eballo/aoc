# Generated on 03-12-2025 07:10
# --- Day 3: Lobby ---


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


JOLTS = [9, 8, 7, 6, 5, 4, 3, 2, 1]
NUMBER_OF_BATTERIES_TO_TURN_ON = 2


def get_two_jolts_by_given_line(line_of_digits: str) -> int:
    batteries = 0
    length = len(line_of_digits)

    # print(f"find jolt for digits:{line_of_digits}")
    for jolt in JOLTS:
        pos = line_of_digits.find(str(jolt))
        if pos != -1 and pos < length - 1:
            # print(f" found jolt:{jolt} at pos:{pos}")

            # continue checking from next position with reminding digits
            remiding_digits = line_of_digits[pos + 1 :]
            # print(f" remiding_digits:{remiding_digits}")

            # fin the max digit in remiding_digits
            max_digit = find_max_digit(remiding_digits)

            # print(f" found jolt:{max_digit}")
            batteries = int(str(jolt) + str(max_digit))
            break

    return batteries


def find_max_digit(remiding_digits: str) -> int:
    max_digit = 0
    for digit in remiding_digits:
        if int(digit) > max_digit:
            max_digit = int(digit)
    return max_digit


def get_twelve_jolts_by_given_line(line_of_digits: str) -> int:

    length = len(line_of_digits)
    current_pos = 0
    batteries = ""

    # we can't have more than 12 batteries
    # strategy is to find the max digit in the window that shrinks each iteration
    # this way we ensure we have enough digits left to complete 12 batteries

    # print(f"find jolt for digits:{line_of_digits}")
    for i in range(12):
        digits_still_needed = 11 - i
        end_limit = len(line_of_digits) - digits_still_needed
        # print("Iteration:", i)
        window = line_of_digits[current_pos:end_limit]
        # print(f" window to search in:{window}")

        best_digit = find_max_digit(window)
        # print(f" found best_digit:{best_digit}")

        batteries += str(best_digit)
        # print(f" batteries:{batteries}")
        current_pos += window.find(str(best_digit)) + 1

    return int(batteries)


def part_one(file: str):
    raw_data = get_raw_data(file)

    total_jolts = []
    for line_of_digits in raw_data:
        # print(line_of_digits)
        jolts = get_two_jolts_by_given_line(line_of_digits)
        total_jolts.append(jolts)
    print(f"total_jolts :{total_jolts}")
    print(f"total_jolts :{sum(total_jolts)}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    total_jolts = []
    for line_of_digits in raw_data:
        # print(line_of_digits)
        jolts = get_twelve_jolts_by_given_line(line_of_digits)
        total_jolts.append(jolts)
    print(f"total_jolts :{total_jolts}")
    print(f"total_jolts :{sum(total_jolts)}")


if __name__ == "__main__":
    print("=== Example Input ==")
    part_one("example.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Example Input ==")
    part_two("example.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
