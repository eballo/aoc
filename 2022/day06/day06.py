

def load_file(file: str) -> str:
    with open(file, "r") as f:
        return f.read().strip()



def part_one(file: str):
    raw_data = load_file(file)

    i = 0
    while True:
        four_characters = raw_data[i:(i+4)]
        if len(set(list(four_characters))) == 4:
            marker_pos = i + 4
            print(marker_pos)
            break
        i += 1


def part_two(file: str):
    raw_data = load_file(file)

    i = 0
    while True:
        four_characters = raw_data[i:(i+14)]
        if len(set(list(four_characters))) == 14:
            marker_pos = i + 14
            print(marker_pos)
            break
        i += 1


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
