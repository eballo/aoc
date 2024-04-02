import copy
from typing import List, Tuple

TEST_DATA = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
INPUT_DATA = [
    ['R', 'P', 'C', 'D', 'B', 'G'],
    ['H', 'V', 'G'],
    ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
    ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'],
    ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
    ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'],
    ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
    ['C', 'M', 'D', 'B', 'F'],
    ['F', 'C', 'Q', 'G']
]


def load_file(file: str) -> List[str]:
    with open(file, "r") as f:
        return f.readlines()


def get_moves(line: str) -> Tuple[int, int, int]:
    x = line.rsplit()
    amount = int(x[1])
    from_col = int(x[3])
    to_col = int(x[5])
    return amount, from_col, to_col


def part_one(file: str):
    raw_data = load_file(file)

    if "test" in file:
        data = copy.deepcopy(TEST_DATA)
    else:
        data = copy.deepcopy(INPUT_DATA)

    for line in raw_data:

        if "move" in line:
            # print(data)
            # print(f"this is a move : {line}")
            amount, from_col, to_col = get_moves(line)
            # print(f" amount {amount}, from {from_col}, to {to_col}")
            # print(data[from_col - 1])
            for x in range(0, amount):
                value = data[from_col - 1].pop()
                data[to_col-1].append(value)

    print(data)
    if "test" in file:
        print(f" final {data[0].pop()} {data[1].pop()} {data[2].pop()}")
    else:
        print(f" final {data[0].pop()} {data[1].pop()} {data[2].pop()} {data[3].pop()} {data[4].pop()} {data[5].pop()} {data[6].pop()} {data[7].pop()} {data[8].pop()}")


def part_two(file: str):
    raw_data = load_file(file)

    if "test" in file:
        data = copy.deepcopy(TEST_DATA)
    else:
        data = copy.deepcopy(INPUT_DATA)
    for line in raw_data:
        if "move" in line:
            # print(data)
            # print(f"this is a move : {line}")
            amount, from_col, to_col = get_moves(line)
            # print(f" amount {amount}, from {from_col}, to {to_col}")
            # print(data[from_col - 1])
            data[to_col - 1].extend(data[from_col - 1][-amount:])
            data[from_col - 1] = data[from_col - 1][:-amount]
            # print(data[to_col - 1])

    print(data)
    top = [value[-1] for value in data]
    print("".join(top))


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
