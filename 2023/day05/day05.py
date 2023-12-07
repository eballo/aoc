
def load_file(file):
    with open(file) as f:
        values = f.read().strip()
    return values


def _parse_sections(sections: list) -> dict:
    data_dict = {
        "seeds": sections[0].split(":")[1].strip().split(" "),
        "seeds_to_soil": [x.split(" ") for x in sections[1].split(":")[1].strip().split("\n")],
        "soil_to_fertilizer": [x.split(" ") for x in sections[2].split(":")[1].strip().split("\n")],
        "fertilizer_to_water": [x.split(" ") for x in sections[3].split(":")[1].strip().split("\n")],
        "water_to_light": [x.split(" ") for x in sections[4].split(":")[1].strip().split("\n")],
        "light_to_temperature": [x.split(" ") for x in sections[5].split(":")[1].strip().split("\n")],
        "temperature_to_humidity": [x.split(" ") for x in sections[6].split(":")[1].strip().split("\n")],
        "humidity_to_location": [x.split(" ") for x in sections[7].split(":")[1].strip().split("\n")],
    }
    return data_dict

maps = {
    1: "seeds_to_soil",
    2: "soil_to_fertilizer",
    3: "fertilizer_to_water",
    4: "water_to_light",
    5: "light_to_temperature",
    6: "temperature_to_humidity",
    7: "humidity_to_location",
}


def get_corresponding_number(num, x, data_dict) -> int:
    for data in data_dict[maps[x]]:
        destination_range_start = int(data[0])
        source_range_start = int(data[1])
        range_range_length = int(data[2])
        found = source_range_start <= int(num) < (source_range_start + range_range_length)
        # print(f"found {found} :  {source_range_start} <= {num} < {(source_range_start + range_range_length)}")
        if found:
            corresponding_number = destination_range_start + (int(num) - source_range_start)
            # print(f"found corresponding number {corresponding_number}")
            return corresponding_number
    return num


def part_one(file: str):
    raw_values = load_file(file)

    sections = raw_values.split("\n\n")
    data_dict = _parse_sections(sections)
    # print(result_dict)

    found_corresponding_number = []
    for seed in data_dict["seeds"]:
        # print(f"Seed {seed}")
        num = seed
        for x in range(1, len(maps)+1):
            # print(maps[x], num)
            num = get_corresponding_number(num, x, data_dict)
        found_corresponding_number.append(num)

    print(found_corresponding_number)
    print(f"lowest location number: {min(found_corresponding_number)}")


def part_two(file: str):
    raw_values = load_file(file)

    sections = raw_values.split("\n\n")
    data_dict = _parse_sections(sections)
    # print(result_dict)

    found_corresponding_number = []
    for i in range(0, len(data_dict["seeds"]), 2):
        seed_start = int(data_dict["seeds"][i])
        seed_length = int(data_dict["seeds"][i+1])
        for seed in range(seed_start, seed_start + seed_length):
            # print(f"Seed {seed}")
            num = seed
            for x in range(1, len(maps)+1):
                # print(maps[x], num)
                num = get_corresponding_number(num, x, data_dict)
            found_corresponding_number.append(num)

    print(found_corresponding_number)
    print(f"lowest location number: {min(found_corresponding_number)}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
