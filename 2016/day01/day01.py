from typing import Tuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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

        taxicab = abs(initial_pos.x - final_pos.x) + abs(initial_pos.y - final_pos.y)
        print(f"taxicab: {taxicab}")


def part_two(file: str):
    raw_values = load_file(file)


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
