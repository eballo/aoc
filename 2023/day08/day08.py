
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


LEFT = 0
RIGHT = 1


def part_one(file: str):
    raw_values = load_file(file)

    instructions, elements = raw_values[0].split(" ")[0], raw_values[2:]

    print(f" Instructions : {instructions}")
    print(f" Elements : {elements}")

    desert_map = {}
    for element in elements:
        position, LR_values = element.split("=")[0].strip(), element.split("=")[1].strip().replace("(", "").replace(")", "").strip().split(", ")
        # print(f" position : {position}")
        # print(f" LR_values : {LR_values}")
        desert_map[position] = LR_values

    print(f" Map : {desert_map}")

    pos = 'AAA'
    total = 0
    steps = 0
    while pos != "ZZZ":
        i = instructions[steps]
        # print(f" steps : {steps}")
        # print(f" pos : {pos}")
        # print(f"desert_map[pos] :{desert_map[pos]}" )
        # print(f" len(instructions) : {len(instructions)}")
        # print(f" instructions : {instructions}")
        # print(f" instructions[steps] : {i}")
        if i == "L":
            pos = desert_map[pos][LEFT]
        elif i == "R":
            pos = desert_map[pos][RIGHT]
        steps += 1
        total += 1

        # if we are at the end let's start again
        if steps == len(instructions):
            steps = 0

    print(f"final pos : {pos}")
    print(f"total steps : {total}")


def part_two(file: str):
    raw_values = load_file(file)

    instructions, elements = raw_values[0].split(" "), raw_values[2:]

    print(f" instructions : {instructions}")
    print(f" elements : {elements}")


if __name__ == "__main__":
    # print("=== Part 1 Test ==")
    # part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
