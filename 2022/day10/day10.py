from typing import Tuple, List


def load_file(file: str) -> Tuple[str, int]:
    with open(file, "r") as f:
        for line in f:
            values = line.split()
            if len(values) == 1:
                yield values[0], None
            else:
                yield values[0], int(values[1])


def handle_cycles(t: int, x: int , total: int) -> int:
    if t in [20, 60, 100, 140, 180, 220]:
        total += x * t
    return total


def handle_cycles_crt(command: str, value: int, t: int, x: int, crt: List[List[str]], start: bool) -> None:
    col = (t-1) // 40
    row = (t-1) % 40

    # print(col, row)
    if abs(x - row) <= 1:
        crt[col][row] = '#'
    else:
        crt[col][row] = ' '

    # if command == "addx":
    #     if start:
    #         print(f"Start cycle {t}: begin executing {command} {value}")
    #     print(f"During cycle {t}: CRT draws pixel in position {t-1}")
    #     if not start:
    #         print(f"End of cycle {t}: begin executing {command} {value}")
    #         print(f"Sprite position: {''.join(crt[col])}")


def part_one(file: str):
    raw_data = load_file(file)

    x = 1  # starting cycle
    t = 0
    total = 0

    for instruction, value in raw_data:
        # print(f" instruction {instruction}, value {value}")
        if instruction == "addx":
            t += 1
            total = handle_cycles(t, x, total)
            t += 1
            total = handle_cycles(t, x, total)
            x += value
        else:
            t += 1
            total = handle_cycles(t, x, total)

    print(f"What is the sum of these six signal strengths? {total}")


def part_two(file: str):
    raw_data = load_file(file)

    crt = [['.' for _ in range(40)] for _ in range(6)]

    x = 1  # starting cycle
    t = 0

    for instruction, value in raw_data:
        # print(f" instruction {instruction}, value {value}")
        if instruction == "addx":
            t += 1
            handle_cycles_crt("addx", value, t, x, crt, True)
            t += 1
            handle_cycles_crt("addx", value, t, x, crt, False)
            x += value
        else:
            t += 1
            handle_cycles_crt("noop", value, t, x, crt, False)

    print(f"What eight capital letters appear on your CRT?")
    print(" ")
    for cycles in range(len(crt)):
        print(''.join(crt[cycles]))


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
