from typing import List


def load_file(file: str) -> List[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def parse_input(instructions: List[str]) -> dict:
    parsed_instructions = {}
    for line in instructions:
        parts = line.strip().split(' -> ')
        parsed_instructions[parts[1]] = parts[0]
    return parsed_instructions


def get_signal(wire: str, parsed_instructions: dict, memo: dict):
    if wire.isdigit():
        return int(wire)
    if wire in memo:
        return memo[wire]

    instruction = parsed_instructions[wire]

    if 'AND' in instruction:
        operands = instruction.split(' AND ')
        signal = get_signal(operands[0], parsed_instructions, memo) & get_signal(operands[1], parsed_instructions, memo)
    elif 'OR' in instruction:
        operands = instruction.split(' OR ')
        signal = get_signal(operands[0], parsed_instructions, memo) | get_signal(operands[1], parsed_instructions, memo)
    elif 'LSHIFT' in instruction:
        operand, shift_amount = instruction.split(' LSHIFT ')
        signal = get_signal(operand, parsed_instructions, memo) << int(shift_amount)
    elif 'RSHIFT' in instruction:
        operand, shift_amount = instruction.split(' RSHIFT ')
        signal = get_signal(operand, parsed_instructions, memo) >> int(shift_amount)
    elif 'NOT' in instruction:
        operand = instruction[4:]
        signal = ~get_signal(operand, parsed_instructions, memo) & 0xFFFF  # Apply bitwise NOT and mask with 16 bits
    else:
        signal = get_signal(instruction, parsed_instructions, memo)

    memo[wire] = signal
    return signal


def part_one(file: str):
    raw_values = load_file(file)

    print(raw_values)
    parsed_instructions = parse_input(raw_values)
    print(parsed_instructions)
    memo = {}
    signal = get_signal('a', parsed_instructions, memo)
    print(f" The ultimate signal to wire a is {signal}")


def part_two(file: str):
    raw_values = load_file(file)

    for value in raw_values:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
