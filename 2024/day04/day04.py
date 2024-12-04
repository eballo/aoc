# Generated on 04-12-2024 08:12
# --- Day 4: Ceres Search ---

def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values

# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....

def find_word(raw_data: list[str], position: tuple[int, int], direction: tuple[int, int], word:str, matrix_size:tuple[int, int]) -> bool:
    dx, dy = direction
    for i, letter in enumerate(word):
        px = position[0] + i * dx
        py = position[1] + i * dy
        if not (0 <= px < matrix_size[0] and 0 <= py < matrix_size[1]):
            return False
        if raw_data[px][py] == letter:
            print(f"{letter} found!")
        if raw_data[px][py] != letter:
            return False
    return True


def get_all_possible_directions_from_a_position() -> list[tuple[int, int]]:
    """
    # dd = [(-1,-1), (-1,0), (-1,1),
    #       (0,-1),          (0,1),
    #       (1,-1),  (1,0),  (1,1)]
    """
    all_possible_directions = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                all_possible_directions.append((dx, dy))
    return all_possible_directions

def part_one(file: str):
    raw_data = get_raw_data(file)

    all_possible_directions = get_all_possible_directions_from_a_position()
    # print(all_possible_directions)

    row_size = len(raw_data)
    col_size = len(raw_data[0])
    matrix_size =(row_size, col_size)

    total = 0
    for row in range(row_size):
        for col in range(col_size):
            for direction in all_possible_directions:
                total += find_word(raw_data,(row, col), direction, "XMAS", matrix_size)

    print(f"How many times does XMAS appear? {total}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")