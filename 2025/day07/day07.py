# Generated on 07-12-2025 07:16
# --- Day 7: Laboratories ---


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def update_line(
    pos_list: list[int], line: str, total: int
) -> tuple[list[int], str, int]:
    updated_pos = []
    line_list = list(line)
    for col in pos_list:
        # print(line[col])
        if line[col] == "S":
            updated_pos.append(col)
            # print("Start point !")
        if line[col] == ".":
            # print("continues")
            line_list[col] = "|"
            updated_pos.append(col)
        if line[col] == "^":
            # print("split path")
            total = total + 1
            line_list[col - 1] = "|"
            line_list[col + 1] = "|"
            updated_pos.append(col - 1)
            updated_pos.append(col + 1)
            # print(total)
    return list(set(updated_pos)), "".join(line_list), total


def part_one(file: str):
    raw_data = get_raw_data(file)

    col = raw_data[0].find("S")
    new_path = []
    updated_pos = [col]
    total = 0

    for line in raw_data:
        # print(f"{updated_pos}, {line}")
        updated_pos, updated_line, total = update_line(updated_pos, line, total)
        new_path.append(updated_line)
    # print(raw_data)
    # print(new_path)
    print(f"How many times will the beam be split? {total}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Example ==")
    part_one("example.txt")

    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Example ==")
    # part_two("example.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
