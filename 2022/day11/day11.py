import math
import re
from dataclasses import dataclass
import parse


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


@dataclass
class Monkey:
    monkey_id: int
    items: list[int]
    operation: dict
    test: dict
    inspected_items: int = 0

    def add_item(self, item: int):
        self.items.append(item)

    def __str__(self):
        return f"Monkey {self.monkey_id} - items: {self.items} - operation: {self.operation} - test: {self.test}"


def parse_monkeys(lines: list[str]) -> list[Monkey]:
    monkeys = []
    for index in range(0, len(lines), 7):
        monkey_id = get_monkey_id(lines[index])
        items = get_starting_items(lines[index + 1])
        operations = get_operations(lines[index + 2])
        test_divisible_by = get_test_divisible_by(lines[index + 3])
        test_true = get_test_true(lines[index + 4])
        test_false = get_test_false(lines[index + 5])
        test_dict ={
            "divisible_by": test_divisible_by,
            "true": test_true,
            "false": test_false
        }
        # end = lines[index + 6] not needed

        # print(monkey_id, items, operations, test_dict)
        monkey = Monkey(monkey_id, items, operations, test_dict)
        monkeys.append(monkey)

    return monkeys


def get_monkey_id(line: str) -> int:
    monkey_id = int(parse.parse("Monkey {}:", line)[0])
    return monkey_id


def get_starting_items(line: str) -> list[int]:
    numbers = re.findall(r'\b\d+\b', line)
    return [int(number) for number in numbers]


def get_operations(line: str) -> dict:
    action = parse.parse("  Operation: new = old {}", line)[0]
    operation, argument = action.split(" ")
    operations = {
        "operation": operation,
        "argument": int(argument) if argument.isdigit() else argument
    }
    return operations


def get_test_divisible_by(line: str) -> list[int]:
    divisible_by = parse.parse("  Test: divisible by {}", line)[0]
    return int(divisible_by)


def get_test_true(line: str, ) -> int:
    throw_monkey_to = parse.parse("    If true: throw to monkey {}", line)[0]
    return int(throw_monkey_to)


def get_test_false(line: str, ) -> int:
    throw_monkey_to = parse.parse("    If false: throw to monkey {}", line)[0]
    return int(throw_monkey_to)


def part_one(file: str):
    raw_data = load_file(file)
    monkeys = parse_monkeys(raw_data)
    rounds = 20

    for round in range(rounds):
        print(f"Round {round + 1} ----------------------- ")
        for monkey in monkeys:
            print(f"Monkey {monkey.monkey_id}:")
            print(f"  Items: {monkey.items}")
            divisible_by = False
            insected_items = []
            for item in monkey.items:
                insected_items.append(item)
                print(f"    Monkey inspects an item with a worry level of {item}")

                if monkey.operation['argument'] == "old":
                    argument = item
                else:
                    argument = monkey.operation['argument']

                if monkey.operation['operation'] == "+":
                    operation = item + argument
                elif monkey.operation['operation'] == "*":
                    operation = item * argument

                print(f"    Worry level is {monkey.operation['operation']} by {argument} to {operation}")

                worry_level = math.floor(operation / 3)
                print(f"    Monkey gets bored with item. Worry level is divided by 3 to {worry_level}.")

                if worry_level % monkey.test['divisible_by'] == 0:
                    divisible_by = True
                    print(f"    Current worry level is divisible by {monkey.test['divisible_by']}")
                else:
                    print(f"    Current worry level is not divisible by {monkey.test['divisible_by']}")
                    divisible_by = False

                if divisible_by:
                    print(f"    Item with worry level {worry_level} is thrown to monkey {monkey.test['true']}.")
                    monkeys[monkey.test['true']].add_item(worry_level)
                else:
                    print(f"    Item with worry level {worry_level} is thrown to monkey {monkey.test['false']}.")
                    monkeys[monkey.test['false']].add_item(worry_level)
            print(f"    removed item {insected_items} from monkey {monkey.monkey_id}")
            for item in insected_items:
                monkey.items.remove(item)  # remove item from current monkey
                monkey.inspected_items += 1  # increment inspected items
        print("----------------------- ")
        print(f"Items after round {round + 1}:")
        for monkey in monkeys:
            print(f"Monkey {monkey.monkey_id}: {monkey.items}")
        print("----------------------- ")

    print("Final results:")
    final_results = []
    for monkey in monkeys:
        print(f"Monkey {monkey.monkey_id}: {monkey.inspected_items}")
        final_results.append(monkey.inspected_items)

    final_results = sorted(final_results)

    print(f"The level of monkey business : {final_results[-1]} * {final_results[-2]} = {final_results[-1] * final_results[-2]}")

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
