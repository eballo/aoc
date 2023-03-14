def load_file(file):
    with open(file) as f:
        values = [str(line.replace("\n", "")) for line in f.readlines()]
    return values


buttons = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

buttons2 = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
    ]


directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


def move(start, direction):
    new_x = start[0] + direction[0]
    new_y = start[1] + direction[1]
    if new_x < 0 or new_x > 2:
        new_x = start[0]
    if new_y < 0 or new_y > 2:
        new_y = start[1]
    return new_x, new_y


def move2(start, direction):
    new_x = start[0] + direction[0]
    new_y = start[1] + direction[1]
    if new_x < 0 or new_x > 4:
        new_x = start[0]
    if new_y < 0 or new_y > 4:
        new_y = start[1]
    if buttons2[new_x][new_y] is None:
        return start
    return new_x, new_y


def part_one(file: str):
    raw_values = load_file(file)
    start = (1, 1)
    for values in raw_values:
        for i in range(len(values)):
            x, y = move(start, directions[values[i]])
            start = (x, y)
        print(buttons[start[0]][start[1]])


def part_two(file: str):
    raw_values = load_file(file)
    start = (2, 0)
    for values in raw_values:
        for i in range(len(values)):
            x, y = move2(start, directions[values[i]])
            start = (x, y)
            # print(f"{values[i]} - {start}")
        print(buttons2[start[0]][start[1]])


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
