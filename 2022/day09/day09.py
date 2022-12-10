from typing import Tuple


# UP, LEFT, RIGHT, DOWN
DIRECTIONS = {
    "U": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
    "D": (0, -1)
}


def load_file(file: str) -> Tuple[str, int]:
    with open(file, "r") as f:
        for line in f:
            direction, steps = line.split()
            yield direction, int(steps)


def move_tail(head, tail):
    x_distance = head[0] - tail[0]
    y_distance = head[1] - tail[1]
    if abs(x_distance) <= 1 and abs(y_distance) <= 1:
        # must always be touching (diagonally adjacent and even overlapping both count as touching)
        pass
    elif abs(x_distance) >= 2 and abs(y_distance) >= 2:
        # If the head is ever two steps directly up, down, left, or right from the tail, the tail must
        # also move one step in that direction so it remains close enough
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1] - 1 if tail[1] < head[1] else head[1] + 1)
    elif abs(x_distance) >= 2:
        # Otherwise, if the head and tail aren't touching and aren't in the same row the tail always
        # moves one step diagonally to keep up
        tail = (head[0] - 1 if tail[0] < head[0] else head[0] + 1, head[1])
    elif abs(y_distance) >= 2:
        # Otherwise, if the head and tail aren't touching and aren't in the same column the tail always
        # moves one step diagonally to keep up
        tail = (head[0], head[1] - 1 if tail[1] < head[1] else head[1] + 1)
    return tail


def part_one(file: str):
    raw_data = load_file(file)

    # start position
    Head = (0, 0)
    Tail = (0, 0)

    tail_unique_positions = set()
    tail_unique_positions.add(Tail)

    for direction, steps in raw_data:
        # print(f" direction {direction}, steps {steps}")
        for _ in range(steps):
            Head = (Head[0] + DIRECTIONS[direction][0], Head[1] + DIRECTIONS[direction][1])
            # print(f"head {Head}")

            Tail = move_tail(Head, Tail)

            tail_unique_positions.add(Tail)
            # print(Head, Tail)

    total = len(tail_unique_positions)
    print(f"How many positions does the tail of the rope visit at least once? {total}")


def part_two(file: str):
    raw_data = load_file(file)

    # start position
    head = (0, 0)
    tail = [(0, 0) for _ in range(9)]

    tail_unique_positions = set()
    tail_unique_positions.add(tail[0])

    for direction, steps in raw_data:
        # print(f" direction {direction}, steps {steps}")
        for _ in range(steps):
            head = (head[0] + DIRECTIONS[direction][0], head[1] + DIRECTIONS[direction][1])
            # print(f"head {Head}")

            # move tail first position
            tail[0] = move_tail(head, tail[0])

            # move the rest of the tail
            for i in range(1, 9):
                tail[i] = move_tail(tail[i-1], tail[i])

            tail_unique_positions.add(tail[8])
            # print(Head, Tail)

    total = len(tail_unique_positions)
    print(f"How many positions does the tail of the rope visit at least once? {total}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
