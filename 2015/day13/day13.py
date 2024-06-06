import itertools
import json
from typing import List


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def parse_raw_data(raw_values: List[str]):
    """ Parse raw data values and return a dictionary with the parsed values"""
    happiness_map = {}
    for line in raw_values:
        words = line.split()
        person1 = words[0]
        person2 = words[-1].strip('.')
        happiness = int(words[3])
        if words[2] == 'lose':
            happiness = -happiness

        if person1 not in happiness_map:
            happiness_map[person1] = {}

        happiness_map[person1][person2] = happiness

    return happiness_map


def calculate_happiness(seating: tuple, happiness_map: dict):
    total_happiness = 0
    for i in range(len(seating)):
        person1 = seating[i]
        person2 = seating[(i + 1) % len(seating)]
        total_happiness += happiness_map[person1].get(person2, 0)
        total_happiness += happiness_map[person2].get(person1, 0)
    return total_happiness


def find_optimal_happiness(happiness_map: dict):
    people = list(happiness_map.keys())
    max_happiness = float('-inf')
    for seating in itertools.permutations(people):
        happiness = calculate_happiness(seating, happiness_map)
        if happiness > max_happiness:
            max_happiness = happiness
    return max_happiness


def add_myself(happiness_map: dict):
    people = list(happiness_map.keys())
    happiness_map['myself'] = {person: 0 for person in people}
    for person in people:
        happiness_map[person]['myself'] = 0


def part_one(file: str):
    raw_values = load_file(file)

    happiness_map = parse_raw_data(raw_values)
    print(json.dumps(happiness_map, sort_keys=True, indent=2))
    max_happiness = find_optimal_happiness(happiness_map)
    print(f"The maximum total happiness is: {max_happiness}")


def part_two(file: str):
    raw_values = load_file(file)

    happiness_map = parse_raw_data(raw_values)
    add_myself(happiness_map)
    print(json.dumps(happiness_map, sort_keys=True, indent=2))
    max_happiness = find_optimal_happiness(happiness_map)
    print(f"The maximum total happiness is: {max_happiness}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
