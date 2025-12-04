# Generated on 04-12-2025 07:44
# --- Day 4: Printing Department ---

# UP, LEFT, RIGHT, DOWN
DIRECTIONS = {"U": (0, 1), "L": (-1, 0), "R": (1, 0), "D": (0, -1)}


def get_raw_data(file: str) -> list[list[str]]:
    field = []
    with open(file) as f:
        for line in f:
            height = []
            row = line.split()  # remove end of line
            for i in range(0, len(row[0])):
                height.append(str(row[0][i]))
            field.append(height)
    return field


def calculate_total_papper_rolls_accessible_by_forklift(data: list[list[str]]) -> int:
    total_rolls = 0
    positions = []
    for row in data:
        for cell in row:
            if cell == "@":
                if can_folklift_access_rolls(data, row.index(cell), data.index(row)):
                    total_rolls += 1
                    postions = []

    return total_rolls


def part_one(file: str):
    raw_data = get_raw_data(file)

    print(raw_data)
    total = calculate_total_papper_rolls_accessible_by_forklift(raw_data)

    print(f"How many rolls of paper can be accessed by a forklift? {total}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
