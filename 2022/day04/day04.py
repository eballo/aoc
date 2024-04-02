from typing import Tuple


def load_file(file: str) -> Tuple[str, str]:
    with open(file, "r") as f:
        for line in f:
            elfs_section = line.rstrip().split(',')
            yield elfs_section[0], elfs_section[1]


def fully_contains(elf_one_section, elf_two_section) -> bool:
    elf1 = elf_one_section.split("-")
    elf2 = elf_two_section.split("-")
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        return True
    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        return True
    else:
        return False


def contains_overlap(elf_one_section, elf_two_section) -> Tuple[bool]:
    elf1 = elf_one_section.split("-")
    elf2 = elf_two_section.split("-")
    if int(elf1[0]) == int(elf2[0]) or int(elf1[1]) == int(elf2[0]) \
            or int(elf1[0]) == int(elf2[1]) or int(elf1[1]) == int(elf2[1]):
        return True
    elif int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        return True
    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        return True
    elif int(elf2[0]) <= int(elf1[0]) <= int(elf2[1]) <= int(elf1[1]):
        return True
    elif int(elf1[0]) <= int(elf2[0]) <= int(elf1[1]) <= int(elf2[1]):
        return True
    else:
        return False


def part_one(file: str):
    raw_data = load_file(file)

    total = 0
    for elf_one_section, elf_two_section in raw_data:
        contains = fully_contains(elf_one_section, elf_two_section)
        # print(f" {elf_one_section} , {elf_two_section} : {contains}")
        if contains:
            total = total + 1

    print(f"total : {total}")


def part_two(file: str):
    raw_data = load_file(file)

    total = 0
    for elf_one_section, elf_two_section in raw_data:
        contains = contains_overlap(elf_one_section, elf_two_section)
        # print(f" {elf_one_section} , {elf_two_section} : {contains}")
        if contains:
            total = total + 1

    print(f"total : {total}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
