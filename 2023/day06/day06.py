from collections import defaultdict


def load_file(file):
    with open(file) as f:
        values = f.read().strip()
    return values


def _parse_data(raw_values):
    time_raw = raw_values.split("\n")[0].split(":")[1].strip().split(" ")
    distances_raw = raw_values.split("\n")[1].split(":")[1].strip().split(" ")
    time = [int(x) for x in time_raw if x.isdigit()]
    distances = [int(x) for x in distances_raw if x.isdigit()]
    return distances, time


def _parse_data_part2(raw_values):
    time_raw = raw_values.split("\n")[0].split(":")[1].strip().replace(" ", "")
    distances_raw = raw_values.split("\n")[1].split(":")[1].strip().replace(" ", "")
    time = int(time_raw)
    distances = int(distances_raw)
    return distances, time


def part_one(file: str):
    raw_values = load_file(file)

    distances, time = _parse_data(raw_values)

    race = defaultdict(list)
    for i in range(0, len(time)):
        # print(f"time {time[i]} milliseconds, distances {distances[i]} millimeters")
        for x in range(0, time[i]+1):
            speed = x
            total_time = time[i] - x
            # print(f"hold button {x} milliseconds - Then, the boat will travel at a speed of {speed} millimeter per millisecond for {total_time} milliseconds, reaching a total distance traveled of {total_time * speed} millimeters")
            if total_time * speed > distances[i]:
                # print(f"candidate to win the game: hold button {x} milliseconds")
                race[i+1].append(x)

    print(race)
    total = 1
    for x in race.values():
        total *=len(x)

    print(total)


def part_two(file: str):
    raw_values = load_file(file)

    distances, time = _parse_data_part2(raw_values)

    race = defaultdict(list)

    for x in range(0, time + 1):
        speed = x
        total_time = time - x
        # print(f"hold button {x} milliseconds - Then, the boat will travel at a speed of {speed} millimeter per millisecond for {total_time} milliseconds, reaching a total distance traveled of {total_time * speed} millimeters")
        if total_time * speed > distances:
            # print(f"candidate to win the game: hold button {x} milliseconds")
            race[1].append(x)

    print(race)
    total = 1
    for x in race.values():
        total *= len(x)

    print(total)


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
