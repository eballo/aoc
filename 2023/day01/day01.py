
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
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
    raw_lines = load_file(file)

    numbers = []
    for line in raw_lines:
        number = ""
        for x, character in enumerate(line):
            if character.isdigit():
                number += character
            for n, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[x:].startswith(value):
                    number += str(n+1)
            # print(character)
        numbers.append(int(number[0] + number[-1]))

    print(numbers)
    total = 0
    for number in numbers:
        total += number
    print(total)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
