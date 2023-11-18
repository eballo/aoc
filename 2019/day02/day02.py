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


def get_inputs(numbers: List[str], val1_idx: int, val2_idx: int) -> (int, int):
    return int(numbers[int(val1_idx)]), int(numbers[int(val2_idx)])


def show_output(numbers, index, total):
    print(f"{index} - total {total} => numbers {numbers}")


def set_total(numbers, output_idx, total):
    numbers[int(output_idx)] = total


def part_one(file: str, restore: bool = False):
    raw_values = load_file(file)
    for value in raw_values:
        numbers = value.split(",")

    # restore the gravity assist program
    if restore:
        numbers[1] = 12
        numbers[2] = 2

    for index in range(0, len(numbers), 4):
        optcode = int(numbers[index])
        opcode = get_operation_code(optcode)

        if opcode == "halt":
            break

        val1_idx = int(numbers[index + 1])
        val2_idx = int(numbers[index + 2])
        output_idx = int(numbers[index + 3])

        value1, value2 = get_inputs(numbers, val1_idx, val2_idx)

        if opcode == "add":
            total = value1 + value2
        elif opcode == "multiply":
            total = value1 * value2

        set_total(numbers, output_idx, total)
        show_output(numbers, index, total)


def part_two(file: str):
    raw_values = load_file(file)
    total = 0
    original_numbers = []
    for value in raw_values:
        original_numbers = value.split(",")

    found = False
    for noun in range(0, 100):
        if found:
            break
        for verb in range(0, 100):
            numbers = original_numbers.copy()
            # print(f"noun: {noun}, verb: {verb}")
            # print(f"numbers: {numbers}")
            numbers[1] = noun
            numbers[2] = verb
            if found:
                break

            for index in range(0, len(numbers), 4):
                optcode = int(numbers[index])
                opcode = get_operation_code(optcode)

                if opcode == "halt":
                    break

                val1_idx = int(numbers[index + 1])
                val2_idx = int(numbers[index + 2])
                output_idx = int(numbers[index + 3])

                value1, value2 = get_inputs(numbers, val1_idx, val2_idx)

                if opcode == "add":
                    total = value1 + value2
                elif opcode == "multiply":
                    total = value1 * value2

                set_total(numbers, output_idx, total)
                # show_output(numbers, index, total)

                if total == 19690720:
                    print(f"noun: {noun}, verb: {verb}, total: {total}, answer: {100 * noun + verb}")
                    found = True


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt", True)
    print("=== Part 2 Input ==")
    part_two("input.txt")
