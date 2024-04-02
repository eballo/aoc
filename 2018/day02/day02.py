from typing import List


def load_file(file: str) -> List[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    raw_values = load_file(file)

    appears_twice = 0
    appears_thrice = 0
    for value in raw_values:
        for letter in value:
            if value.count(letter) == 2:
                appears_twice += 1
                break
        for letter in value:
            if value.count(letter) == 3:
                appears_thrice += 1
                break

    print(appears_twice * appears_thrice)


def part_two(file: str):
    raw_values = load_file(file)

    for i in range(len(raw_values)):
        for j in range(i + 1, len(raw_values)):
            if sum([1 for x, y in zip(raw_values[i], raw_values[j]) if x == y]) == len(raw_values[i]) - 1:
                print(raw_values[i])
                print(raw_values[j])
                print("".join([x for x, y in zip(raw_values[i], raw_values[j]) if x == y]))
                return


if __name__ == "__main__":

    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
