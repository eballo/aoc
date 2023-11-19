from dataclasses import dataclass
import parse


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


@dataclass
class Monkey:
    monkey_id: int

    def __str__(self):
        return f"Monkey {self.monkey_id}"


def parse_monkeys(lines: str) -> list[Monkey]:
    monkeys = []
    for index in range(0, len(lines), 7):
        monkey_id = get_monkey_id(lines[index])
        items = get_starting_items(lines[index + 1])
        operations = lines[index + 2]
        test = lines[index + 3]
        test_true = lines[index + 4]
        test_false = lines[index + 5]
        end = lines[index + 6]

        print(monkey_id, items, operations, test, test_true, test_false, end)
        monkey = Monkey(monkey_id)
        monkeys.append(monkey)

    return monkeys


def get_monkey_id(line: str) -> int:
    monkey_id = int(parse.parse("Monkey {}:", line)[0])
    return monkey_id


def get_starting_items(line: str):
    pass


def part_one(file: str):
    raw_data = load_file(file)
    monkeys = parse_monkeys(raw_data)

    for monkey in monkeys:
        print(monkey)


def part_two(file: str):
    raw_data = load_file(file)
    pass


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
