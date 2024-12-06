# Generated on 05-12-2024 07:59
# --- Day 5: Print Queue ---
from typing import Tuple, List


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values

def parse_data(raw_data: list[str]) -> tuple[list[tuple[int, ...]], list[list[int]]]:
    page_ordering_rules = []
    pages_to_produce = []
    for data in raw_data:
        print(data)
        if "|" in data:
            page_ordering_rules.append(tuple(map(int, data.split("|"))))
        elif "," in data:
            pages_to_produce.append(list(map(int, data.split(","))))
    return page_ordering_rules, pages_to_produce


def follows_the_rules(page: list[int], page_ordering_rules: list[tuple[int, ...]]) -> bool:
    idx = {}
    for i, page in enumerate(page):
        idx[page] = i
    # print(idx)
    for a, b in page_ordering_rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False
    return True


def part_one(file: str):
    raw_data = get_raw_data(file)
    page_ordering_rules, pages_to_produce = parse_data(raw_data)
    print(page_ordering_rules)
    print(pages_to_produce)

    middle_page_number = 0
    for page in pages_to_produce:
        rules = follows_the_rules(page, page_ordering_rules)
        if rules:
            print(page)
            print(rules)
            middle_page_number += page[len(page)//2]

    print(f"What do you get if you add up the middle page number from those correctly-ordered updates?{middle_page_number}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")