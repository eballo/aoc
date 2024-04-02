
def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def initialize_grid():
    return [[False] * 1000 for _ in range(1000)]


def apply_instruction_part_one(grid, instruction):
    parts = instruction.split()

    action = parts[0]  # turn on/off or toggle
    start_x, start_y = map(int, parts[-3].split(','))
    end_x, end_y = map(int, parts[-1].split(','))

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "turn":
                state = parts[1]
                if state == "on":
                    grid[x][y] = True
                elif state == "off":
                    grid[x][y] = False
            elif action == "toggle":
                grid[x][y] = not grid[x][y]


def apply_instruction_part_two(grid, instruction):
    parts = instruction.split()

    action = parts[0]  # turn on/off or toggle
    start_x, start_y = map(int, parts[-3].split(','))
    end_x, end_y = map(int, parts[-1].split(','))

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "turn":
                state = parts[1]
                if state == "on":
                    grid[x][y] += 1
                elif state == "off":
                    grid[x][y] = max(0, grid[x][y] - 1)
            elif action == "toggle":
                grid[x][y] += 2


def part_one(file: str):
    grid = initialize_grid()
    raw_values = load_file(file)

    for instruction in raw_values:
        apply_instruction_part_one(grid, instruction)

    count = sum(sum(row) for row in grid)
    print(f"lights that are lit: {count}")


def part_two(file: str):
    grid = initialize_grid()
    raw_values = load_file(file)

    for instruction in raw_values:
        apply_instruction_part_two(grid, instruction)

    count = sum(sum(row) for row in grid)
    print(f"Total brightness: {count}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
