
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    # Find the two entries that sum to 2020; what do you get if you multiply them together?
    raw_lines = load_file(file)

    numbers = []
    for line in raw_lines:
        number = ""
        for character in line:
            if character.isdigit():
                number += character
            # print(character)
        numbers.append(int(number[0] + number[-1]))

    print(numbers)
    total = 0
    for number in numbers:
        total += number
    print(total)

    
def part_two(file: str):
    raw_values = load_file(file)
    for value in range(len(raw_values)):
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
