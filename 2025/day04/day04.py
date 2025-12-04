# Generated on 04-12-2025 07:44
# --- Day 4: Printing Department ---

# x-1, y-1  |  x-1, y  |  x-1, y+1
# (NW)      |  (UP)    |  (NE)
# ----------------------------------
# x, y-1    |  x, y    |  x, y+1
# (LEFT)    | (CENTER) | (RIGHT)
# ----------------------------------
# x+1, y-1  |  x+1, y  |  x+1, y+1
# (SW)      | (DOWN)   | (SE)

# Order: N, NE, E, SE, S, SW, W, NW
DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def get_raw_data(file: str) -> list[list[str]]:
    matrix = []
    with open(file) as f:
        for line in f:
            column = []
            row = line.split()  # remove end of line
            for i in range(0, len(row[0])):
                column.append(str(row[0][i]))
            matrix.append(column)
    return matrix


def count_adjacent_rolls(data: list[list[str]], r: int, c: int) -> int:
    rows = len(data)
    cols = len(data[0])
    count = 0
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if data[nr][nc] == "@":
                count += 1
    return count


def calculate_accessible_rolls(data: list[list[str]]) -> int:
    total_accessible = 0
    rows = len(data)
    cols = len(data[0])
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "@":
                neighbors = count_adjacent_rolls(data, r, c)
                if neighbors < 4:
                    total_accessible += 1
    return total_accessible


def part_one(file: str):
    raw_data = get_raw_data(file)
    print(raw_data)
    total = calculate_accessible_rolls(raw_data)
    print(f"How many rolls of paper can be accessed by a forklift? {total}")


def part_two(file: str):
    raw_data = get_raw_data(file)
    print(raw_data)
    total = calculate_accessible_rolls(raw_data)
    print(
        f"How many rolls of paper in total can be removed by the Elves and their forklifts? {total}"
    )


if __name__ == "__main__":
    print("=== Part 1 Example ==")
    part_one("example.txt")

    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Example ==")
    # part_two("example.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
