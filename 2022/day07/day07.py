import sys
from collections import defaultdict
from typing import List, Dict


def load_file(file: str) -> List[str]:
    commands = []
    with open(file, "r") as f:
        for line in f:
            commands.append(line.split())
    return commands


def parse_data(raw_data: List[str]) -> Dict:
    stack_path = []
    sizes = defaultdict(int)
    for command in raw_data:
        if command[0] == "$":
            if command[1] == "cd":
                # print(f"change to directory {command[2]}")
                if command[2] == "..":
                    stack_path.pop()
                else:
                    stack_path.append(command[2])
            elif command[1] == "ls":
                continue
        else:
            if command[0] == "dir":
                # print(f"it is a directory {command[1]}")
                continue
            else:
                # print(f"it is a file {command[1]} with size {command[0]}")
                # I will iterate trough the stack_path, and update the value to all the previous directories,
                # to get the right total, and add the latest path with the total
                for i in range(1, len(stack_path) + 1):
                    # print(i)
                    sizes['/'.join(stack_path[:i])] += int(command[0])
                # print(sizes)

    # print(sizes)
    return sizes


def part_one(file: str):
    raw_data = load_file(file)
    sizes = parse_data(raw_data)

    total_at_most_100000 = 0
    for key, value in sizes.items():
        if value <= 100000:
            total_at_most_100000 += value

    print(f" Total at most 100000: {total_at_most_100000}")


def part_two(file: str):
    raw_data = load_file(file)
    sizes = parse_data(raw_data)

    max_used = 70000000 - 30000000  # (total disk space) + (need unused space)
    need_to_free = sizes['/'] - max_used  # (total used) - (max space that we need)
    total_size_free_up = 10000000000
    for key, value in sizes.items():
        if need_to_free <= value:
            total_size_free_up = min(total_size_free_up, value)

    print(f" Total at most 100000: {total_size_free_up}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
