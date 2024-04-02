from collections import defaultdict


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


# -1 0 1
#  . . .  1
#  . n .  0
#  . . * -1
def _has_adjacent_symbol(engine, r, c, nrows, ncols, has_adjacent_symbol, adjacent_symbol_position=None) -> bool:
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < nrows and 0 <= nc < ncols:
            character = engine[nr][nc]
            if not character.isdigit() and character != '.':
                has_adjacent_symbol = True
                if adjacent_symbol_position is not None:
                    adjacent_symbol_position.append((nr, nc))
                break
    return has_adjacent_symbol


def check_when_no_digit(number, has_adjacent_symbol, adjacents_numbers, not_adjacents_numbers):
    if len(number) > 0:
        # print(f"number : {number} {has_adjacent_symbol}")
        if has_adjacent_symbol:
            # print(f" We have a number {number} with adjacent symbol")
            adjacents_numbers.append(int(number))
        else:
            # print(f" We have a number {number} without adjacent symbol")
            not_adjacents_numbers.append(int(number))


def check_when_no_digit_adjacent(number, adjacent_symbol_position, has_adjacent_symbol, gear_ratio_candidates):
    if len(number) > 0 and len(adjacent_symbol_position) > 0:
        if has_adjacent_symbol:
            for position in adjacent_symbol_position:
                gear_ratio_candidates[position].append(int(number))


def part_one(file: str):
    raw_lines = load_file(file)

    engine = [[c for c in line] for line in raw_lines]
    nrows, ncols = len(engine), len(engine[0])
    adjacents_numbers = []
    not_adjacents_numbers = []

    for r in range(nrows):
        number = ""
        has_adjacent_symbol = False
        for c in range(ncols):
            if engine[r][c].isdigit():
                number += engine[r][c]
                has_adjacent_symbol = _has_adjacent_symbol(engine, r, c, nrows, ncols, has_adjacent_symbol)
            else:
                check_when_no_digit(number, has_adjacent_symbol, adjacents_numbers, not_adjacents_numbers)
                has_adjacent_symbol = False
                number = ""

        # edge case when the number finish at the end of the line
        check_when_no_digit(number, has_adjacent_symbol, adjacents_numbers, not_adjacents_numbers)

    print(f"adjacents numbers list : {adjacents_numbers}")
    print(f"no adjacents numbers list: {not_adjacents_numbers}")
    print(f"Total : {sum(adjacents_numbers)}")


def part_two(file: str):
    raw_lines = load_file(file)

    engine = [[c for c in line] for line in raw_lines]
    nrows, ncols = len(engine), len(engine[0])

    # I will keep the gear ratio candidates in a dict
    # gear_ratio_candidates = {(x, y): [numbers]}
    gear_ratio_candidates = defaultdict(list)

    for r in range(nrows):
        number = ""
        has_adjacent_symbol = False
        adjacent_symbol_position = []
        for c in range(ncols):
            if engine[r][c].isdigit():
                number += engine[r][c]
                if adjacent_symbol_position:
                    continue
                has_adjacent_symbol = _has_adjacent_symbol(engine, r, c, nrows, ncols, has_adjacent_symbol, adjacent_symbol_position)
            else:
                check_when_no_digit_adjacent(number, adjacent_symbol_position, has_adjacent_symbol, gear_ratio_candidates)
                has_adjacent_symbol = False
                number = ""
                adjacent_symbol_position = []

        # edge case when the number finish at the end of the line
        check_when_no_digit_adjacent(number, adjacent_symbol_position, has_adjacent_symbol, gear_ratio_candidates)

    print(f"gear ratio candidates : {gear_ratio_candidates}")
    print(f"Sum of gears ratio candidates : {sum(gears[0] * gears[1] for gears in gear_ratio_candidates.values() if len(gears) == 2)}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
