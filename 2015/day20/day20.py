
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def calculate_lowest_number_of_houses(target_presents: int) -> int | None:
    limit = target_presents // 10  # A reasonable upper bound for the number of houses
    houses = [0] * (limit + 1)  # initialize a list with value zero by the size of limit +1

    # the idea is to iterate and fill the houses array with the number of presents
    # print(houses)
    for elf in range(1, limit + 1):
        for house in range(elf, limit + 1, elf):
            houses[house] += elf * 10
    # print(houses)

    # iterate over the array that is filled with the number of presents by house and then check wich one has
    # the lowest number
    for house, presents in enumerate(houses):
        if presents >= target_presents:
            return house

    return None


def part_one(file: str):
    raw_values = load_file(file)
    number = int(raw_values[0])
    result = calculate_lowest_number_of_houses(number)
    print(f"What is the lowest house number of the house to get at least as many presents as the number in your puzzle input? {result}")


def part_two(file: str):
    raw_values = load_file(file)

    for value in raw_values:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
