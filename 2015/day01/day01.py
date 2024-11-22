
def load_file(file):
    with open(file) as f:
        values = [str(line) for line in f.readlines()]
    return values


def part_one(file: str):
    raw_values = load_file(file)

    print(raw_values)
    for line in raw_values:
        floor = 0

        for x in range(0, len(line)):
            if line[x] == '(':
                floor = floor + 1
            elif line[x] == ')':
                floor = floor - 1

        print(f"floor: {floor}")


def part_two(file: str):
    raw_values = load_file(file)

    for line in raw_values:
        enter_first_floor_pos = []
        print(line)
        floor = 0

        for x in range(0, len(line)):
            if line[x] == '(':
                floor = floor + 1
            elif line[x] == ')':
                floor = floor - 1

            # print(floor)
            if floor == -1:
                enter_first_floor_pos.append(x + 1)
                # print(f"position: {x+1}")
        if enter_first_floor_pos:
            print(f"position: {enter_first_floor_pos[0]}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
