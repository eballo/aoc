from typing import List


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


known_attributes = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def parse_aunt_sue_values(raw_values: List[str]) -> dict[str, dict[str, int]]:
    aunt_sue = {}
    for aunts in raw_values:
        aunts, properties = aunts.split(": ", 1)
        properties = properties.split(",")
        aunt_sue[aunts] = {}
        for element_property in properties:
            property_name, quantity = element_property.strip().split(":")
            aunt_sue[aunts][property_name] = int(quantity)

    return aunt_sue


def matches(aunt: dict, known: dict) -> bool:
    for key in aunt:
        # print(key, aunt[key])
        if key in known and aunt[key] != known[key]:
            return False
    return True


def part_one(file: str):
    raw_values = load_file(file)
    aunts_sue = parse_aunt_sue_values(raw_values)
    print(aunts_sue)

    correct_aunt = None
    for aunt, values in aunts_sue.items():
        if matches(values, known_attributes):
            correct_aunt = aunt
            break
    print(f"Aunt {correct_aunt}")


def part_two(file: str):
    raw_values = load_file(file)

    for value in raw_values:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
