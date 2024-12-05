# Generated on 04-12-2024 08:12
# --- Day 4: Ceres Search ---

def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


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
        # if raw_data[px][py] == letter:
        #     print(f"{letter} found!")
        if raw_data[px][py] != letter:
            return False
    return True


def find_mas(raw_data: list[str], position: tuple[int, int], matrix_size:tuple[int, int]) -> bool:
    if not (1 <= position[0] < (matrix_size[0] - 1) and 1 <= position[1] < (matrix_size[1] - 1)):
        return False
    if raw_data[position[0]][position[1]] != "A":
        return False

    # Check diagonals
    # -1 +1    +1 +1
    #       A
    # -1 -1    +1 -1
    diagonal1 = f"{raw_data[position[0] - 1][position[1] - 1]}{raw_data[position[0] + 1][position[1] + 1]}"
    diagonal2 = f"{raw_data[position[0] - 1][position[1] + 1]}{raw_data[position[0] + 1][position[1] - 1]}"
    if diagonal1 in ["MS", "SM"] and diagonal2 in ["MS", "SM"]:
            return True
    return False


def part_one(file: str):
    raw_data = get_raw_data(file)

    all_possible_directions = get_all_possible_directions_from_a_position()
    # print(all_possible_directions)

    row_size = len(raw_data)
    col_size = len(raw_data[0])
    matrix_size =(row_size, col_size)

    print(f"matrix_size {matrix_size}")

    total = 0
    for row in range(row_size):
        for col in range(col_size):
            for direction in all_possible_directions:
                total += find_word(
                    raw_data,
           (row, col),
                    direction,
                    "XMAS",
                    matrix_size
                )

    print(f"How many times does XMAS appear? {total}")


def part_two(file: str):
    raw_data = get_raw_data(file)

    row_size = len(raw_data)
    col_size = len(raw_data[0])
    matrix_size =(row_size, col_size)

    print(f"matrix_size {matrix_size}")

    total = 0
    for row in range(row_size):
        for col in range(col_size):
            total += find_mas(raw_data,(row, col), matrix_size)

    print(f"How many times does XMAS appear? {total}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")