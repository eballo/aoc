from typing import List


def load_file(file: str) -> List[List[int]]:
    with open(file, "r") as f:
        line = f.readline()
        elfs = []
        energy = []
        while line:
            if line == "\n":
                elfs.append(energy)
                energy = []
            else:
                calories = int(line.split()[0])
                energy.append(calories)
            line = f.readline()
    return elfs


def part_one(file: str):
    raw_values = load_file(file)

    max_value = 0
    for elfs in raw_values:
        total_elf = 0
        for calories in elfs:
            total_elf = total_elf + calories
        if max_value < total_elf:
            max_value = total_elf

    print(f"Elf with Max number of calories : {max_value}")


def part_two(file: str):
    raw_values = load_file(file)

    total_by_elf = []
    for elfs in raw_values:
        total_elf = 0
        for calories in elfs:
            total_elf = total_elf + calories
        total_by_elf.append(total_elf)

    total_by_elf = sorted(total_by_elf)
    total_sum = total_by_elf[-1] + total_by_elf[-2] + total_by_elf[-3]

    print(f"The sum of the Calories carried by these three elves : {total_sum}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
