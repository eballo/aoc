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
            row_string = line.strip()
            matrix.append(list(row_string))
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


def get_accessible_rolls(data: list[list[str]]) -> list[tuple[int, int]]:
    rows = len(data)
    cols = len(data[0])
    rolls = []
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "@":
                neighbors = count_adjacent_rolls(data, r, c)
                if neighbors < 4:
                    rolls.append((r, c))
    return rolls


def part_one(file: str):
    raw_data = get_raw_data(file)
    print(raw_data)
    rolls = get_accessible_rolls(raw_data)
    print(f"How many rolls of paper can be accessed by a forklift? {len(rolls)}")


def part_two(file: str):
    raw_data = get_raw_data(file)
    grand_total_removed = 0
    round_number = 1

    while True:
        # Scan for rolls to be removed
        rolls_to_remove = get_accessible_rolls(raw_data)

        count = len(rolls_to_remove)
        if count == 0:
            print("No more moves possible.")
            break

        # update the grid
        # print(f"Round {round_number}: Removing {count} rolls...")
        for r, c in rolls_to_remove:
            raw_data[r][c] = "."

        grand_total_removed += count

        # next round
        round_number += 1

    print(f"Total rolls removed: {grand_total_removed}")


if __name__ == "__main__":
    print("=== Part 1 Example ==")
    part_one("example.txt")

    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Example ==")
    part_two("example.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
