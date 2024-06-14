from typing import List


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def parse_input(raw_values: List[str]) -> tuple[list[(str, str)], str]:
    replacements = []
    for line in raw_values:
        if line != "":  # the empty line is the last value for the replacements
            src, dest = line.split(" => ")
            replacements.append((src, dest))
        else:
            break

    molecule = raw_values[-1]
    return replacements, molecule


def parse_input_reversed(raw_values: List[str]) -> tuple[list[(str, str)], str]:
    replacements = []
    for line in raw_values:
        if line != "":  # the empty line is the last value for the replacements
            src, dest = line.split(" => ")
            replacements.append((dest, src))  # reversed
        else:
            break

    molecule = raw_values[-1]
    return replacements, molecule


def calculate_distinct_molecules(replacements: List[tuple[str, str]], molecule:str) -> set:
    distinct_molecules = set()
    for src, dest in replacements:
        start = 0
        while True:
            start = molecule.find(src, start)
            if start == -1:
                break
            new_molecule = molecule[:start] + dest + molecule[start + len(src):]
            # print(new_molecule)
            distinct_molecules.add(new_molecule)
            start += 1
    return distinct_molecules


def apply_reverse_transformations(replacements: List[tuple[str, str]], molecule: str) -> int:
    steps = 0
    while molecule != 'e':
        for src, dest in replacements:
            if src in molecule:
                molecule = molecule.replace(src, dest, 1)
                print(molecule)
                steps += 1
                break
    return steps


def part_one(file: str):
    raw_values = load_file(file)
    replacements, molecule = parse_input(raw_values)
    distinct_molecules = calculate_distinct_molecules(replacements, molecule)
    print(f"How many distinct molecules can be created? {len(distinct_molecules)}")


def part_two(file: str):
    raw_values = load_file(file)
    replacements_reversed, molecule = parse_input_reversed(raw_values)
    print(replacements_reversed, molecule)
    # Sort rules by descending length of the src to apply the longest replacements first
    replacements_reversed.sort(key=lambda x: len(x[0]), reverse=True)
    print(f"sorted {replacements_reversed}")
    steps = apply_reverse_transformations(replacements_reversed, molecule)
    print(f"How long will it take to make the medicine? {steps}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
