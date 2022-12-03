from typing import Tuple, List
import string

LOWERCASE = dict(zip(string.ascii_lowercase, range(1, 27)))
UPPERCASE = dict(zip(string.ascii_uppercase, range(27, 57)))


def load_file(file: str) -> Tuple[str, str, str]:
    with open(file, "r") as f:
        for line in f:
            rucksack = line.split()[0]
            yield rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:], rucksack


def translate_rucksack_to_numbers(rucksack: str) -> List[int]:
    rucksack_number = []
    for letter in rucksack:
        if letter.islower():
            rucksack_number.append(LOWERCASE[letter])
        if letter.isupper():
            rucksack_number.append(UPPERCASE[letter])
    return rucksack_number


def part_one(file: str):
    raw_data = load_file(file)

    total = 0
    for first_rucksack, second_rucksack, _ in raw_data:
        # print(f"{first_rucksack} {second_rucksack}")
        first_rucksack_number = translate_rucksack_to_numbers(first_rucksack)
        second_rucksack_number = translate_rucksack_to_numbers(second_rucksack)
        intersection = set(first_rucksack_number).intersection(set(second_rucksack_number))
        # print(f"{first_rucksack_number} - {second_rucksack_number} :  intersectin {list(intersection)[0]}")
        total = total + list(intersection)[0]

    print(f"total :{total}")


def part_two(file: str):

    total = 0
    count_elfs = 0
    rucksack_list = []
    for _, _, rucksack in load_file(file):
        if count_elfs < 3:
            rucksack = translate_rucksack_to_numbers(rucksack)
            rucksack_list.append(rucksack)
            count_elfs = count_elfs + 1
        else:
            intersection = set(rucksack_list[0]) & set(rucksack_list[1]) & set(rucksack_list[2])
            total = total + list(intersection)[0]
            count_elfs = 0
            rucksack_list = []

            rucksack = translate_rucksack_to_numbers(rucksack)
            rucksack_list.append(rucksack)
            count_elfs = count_elfs + 1

    intersection = set(rucksack_list[0]) & set(rucksack_list[1]) & set(rucksack_list[2])
    total = total + list(intersection)[0]
    print(f"total :{total}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
