import json
from typing import List


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def parse_raw_data(raw_values: List[str]):
    """ Parse raw data values and return a dictionary with the parsed values"""
    reindeer_map = {}
    for line in raw_values:
        parts = line.split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])
        reindeer_map[name] = {
            'speed': speed,
            'fly_time': fly_time,
            'rest_time': rest_time,
            'distance': 0,
            'points': 0,
            'current_fly_time': 0,
            'current_rest_time': 0,
            'is_flying': True
        }
    return reindeer_map


def calculate_distance(reindeer: dict, total_time: int) -> int:
    cycle_time = reindeer['fly_time'] + reindeer['rest_time']
    full_cycles = total_time // cycle_time
    remaining_time = total_time % cycle_time

    distance = full_cycles * reindeer['speed'] * reindeer['fly_time']
    distance += min(remaining_time, reindeer['fly_time']) * reindeer['speed']

    return distance


def find_longest_distance(reindeer_map: dict, total_time: int) -> tuple[int, str]:
    max_distance = 0
    reindeer_name = None
    for reindeer in reindeer_map.keys():
        distance = calculate_distance(reindeer_map[reindeer], total_time)
        if distance > max_distance:
            max_distance = distance
            reindeer_name = reindeer
    return max_distance, reindeer_name


def end_of_second_calculation(reindeer_map: dict):
    for reindeer in reindeer_map.keys():
        if reindeer_map[reindeer]['is_flying']:
            reindeer_map[reindeer]['distance'] += reindeer_map[reindeer]['speed']
            reindeer_map[reindeer]['current_fly_time'] += 1
            if reindeer_map[reindeer]['current_fly_time'] == reindeer_map[reindeer]['fly_time']:
                reindeer_map[reindeer]['is_flying'] = False
                reindeer_map[reindeer]['current_fly_time'] = 0
        else:
            reindeer_map[reindeer]['current_rest_time'] += 1
            if reindeer_map[reindeer]['current_rest_time'] == reindeer_map[reindeer]['rest_time']:
                reindeer_map[reindeer]['is_flying'] = True
                reindeer_map[reindeer]['current_rest_time'] = 0


def award_points(reindeer_map: dict):
    max_distance = max(reindeer_map[reindeer]['distance'] for reindeer in reindeer_map.keys())
    for reindeer in reindeer_map.keys():
        if reindeer_map[reindeer]['distance'] == max_distance:
            reindeer_map[reindeer]['points'] += 1


def find_max_points(reindeer_map: dict, total_time: int) -> tuple[int, str]:
    for _ in range(total_time):
        end_of_second_calculation(reindeer_map)
        award_points(reindeer_map)

    max_points = max(reindeer_map[reindeer]['points'] for reindeer in reindeer_map.keys())
    reindeer_name = list(reindeer for reindeer in reindeer_map.keys() if reindeer_map[reindeer]['points'] == max_points )
    return max_points, reindeer_name[0]


def part_one(file: str):
    raw_values = load_file(file)

    reindeer_map = parse_raw_data(raw_values)
    # print(json.dumps(reindeer_map, indent=2))

    total_time = 2503
    max_distance, reinder_name = find_longest_distance(reindeer_map, total_time)
    print(f"what distance has the winning reindeer traveled?: {max_distance} - {reinder_name}")


def part_two(file: str):
    raw_values = load_file(file)

    reindeer_map = parse_raw_data(raw_values)
    # print(json.dumps(reindeer_map, indent=2))

    total_time = 2503
    max_points, reinder_name = find_max_points(reindeer_map, total_time)
    print(f"how many points does the winning reindeer have?: {max_points} - {reinder_name}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
