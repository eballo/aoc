from typing import List


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def get_operation_code(number: int):
    if number == 1:
        return "add"
    elif number == 2:
        return "multiply"
    elif number == 99:
        return "halt"


def get_inputs(numbers: List[str], index: int) -> (int, int):
    return int(numbers[int(numbers[index + 1])]), int(numbers[int(numbers[index + 2])])


def show_output(numbers, index, total):
    print(f"{index} - total {total} => numbers {numbers}")


def set_total(numbers, index, total):
    numbers[int(numbers[index + 3])] = total


def part_one(file: str, restore: bool = False):
    raw_values = load_file(file)
    total = 0
    for value in raw_values:
        numbers = value.split(",")

        # restore the gravity assist program
        if restore:
            numbers[1] = 12
            numbers[2] = 2

        for index in range(0, len(numbers), 4):
            opcode = get_operation_code(int(numbers[index]))
            if opcode == "add":
                value1, value2 = get_inputs(numbers, index)
                total = value1 + value2
                set_total(numbers, index, total)
                show_output(numbers, index, total)
            elif opcode == "multiply":
                value1, value2 = get_inputs(numbers, index)
                total = value1 * value2
                set_total(numbers, index, total)
                show_output(numbers, index, total)
            elif opcode == "halt":
                break


def part_two(file: str):
    pass


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt", True)
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
