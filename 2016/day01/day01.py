from typing import Tuple, Optional


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"x: {self.x}, y: {self.y}")


#    N
# W     E
#    S
def where_to_go(direction: str, move: str, blocks: int, pos: Point) -> Tuple[Point, str]:
    match direction:
        case 'N':
            if move == 'R':
                pos.x += blocks
                return pos, 'E'
            else:
                pos.x -= blocks
                return pos, 'W'
        case 'S':
            if move == 'R':
                pos.x -= blocks
                return pos, 'W'
            else:
                pos.x += blocks
                return pos, 'E'
        case 'E':
            if move == 'R':
                pos.y -= blocks
                return pos, 'S'
            else:
                pos.y += blocks
                return pos, 'N'
        case 'W':
            if move == 'R':
                pos.y += blocks
                return pos, 'N'
            else:
                pos.y -= blocks
                return pos, 'S'


def get_str_pos(pos: Point) -> str:
    return str(pos.x) + '_' + str(pos.y)


def is_visited_position(pos: Point, visited_pos: list) -> bool:
    current_pos = get_str_pos(pos)
    if current_pos in visited_pos:
        print(f"visited {current_pos} - {calculate_taxicab(pos)} - {visited_pos} ")


def add_position(pos: Point, visited_pos: list) -> None:
    pos = get_str_pos(pos)
    visited_pos.append(pos)


def where_to_go_2(direction: str, move: str, blocks: int, pos: Point, visited_pos: list) -> Tuple[Optional[Point], str]:
    match direction:
        case 'N':
            if move == 'R':
                for block in range(blocks):
                    pos.x += 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "E"
            else:
                for block in range(blocks):
                    pos.x -= 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "W"
        case 'S':
            if move == 'R':
                for block in range(blocks):
                    pos.x -= 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "W"
            else:
                for block in range(blocks):
                    pos.x += 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "E"
        case 'E':
            if move == 'R':
                for block in range(blocks):
                    pos.y -= 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "S"
            else:
                for block in range(blocks):
                    pos.y += 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "N"
        case 'W':
            if move == 'R':
                for block in range(blocks):
                    pos.y += 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "N"
            else:
                for block in range(blocks):
                    pos.y -= 1
                    is_visited_position(pos, visited_pos)
                    add_position(pos, visited_pos)
                return pos, "S"


def update_position_and_return_pos_if_found(pos, visited_pos) -> Optional[Point]:
    if is_visited_position(pos, visited_pos):
        return pos
    else:
        add_position(pos, visited_pos)
        return None


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def part_one(file: str):
    """
    the taxicab distance between two points (x1, y1) and (x2,y2) is |x1 - x2| + |y1 - y2|
    it is the sum of the absolute values of the differences in both coordinates.
    """
    raw_values = load_file(file)

    initial_direction = 'N'
    initial_pos = Point(0, 0)  # Initial start point is 0,0

    # print(raw_values)
    for line in raw_values:
        values = [x.strip() for x in line.split(',')]
        print(values)
        final_pos = Point(0, 0)
        direction = initial_direction
        for value in values:
            move = value[0]
            blocks = int(value[1:])
            final_pos, direction = where_to_go(direction, move, blocks, final_pos)

        print(final_pos.x, final_pos.y)

        taxicab = calculate_taxicab(final_pos, initial_pos)
        print(f"taxicab: {taxicab}")


def calculate_taxicab(final_pos, initial_pos=Point(0, 0)):
    return abs(initial_pos.x - final_pos.x) + abs(initial_pos.y - final_pos.y)


def part_two(file: str):
    """
    the first location you visit twice, In order to know that I will keep a list with the visited positions
    """
    raw_values = load_file(file)

    initial_direction = 'N'

    for line in raw_values:
        values = [x.strip() for x in line.split(',')]

        visited_pos = []
        pos = Point(0, 0)
        add_position(pos, visited_pos)
        direction = initial_direction
        print(values)
        for value in values:
            move = value[0]
            blocks = int(value[1:])
            pos, direction = where_to_go_2(direction, move, blocks, pos, visited_pos)
        # print(visited_pos)


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
