# Generated on 01-12-2024 12:00
# --- Day 1: Historian Hysteria ---

def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip().split("   ") for line in f.readlines()]
    return values

def part_one(file: str):
    raw_data = get_raw_data(file)

    total_distance = []
    left = []
    right = []
    for value in raw_data:
        left.append(int(value[0]))
        right.append(int(value[1]))

    left.sort()
    right.sort()
    sorted_list = zip(left, right)
    for element in sorted_list:
        total_distance.append(abs(element[0] - element[1]))

    print(f"What is the total distance between your lists? {sum(total_distance)}")

def part_two(file: str):
    raw_data = get_raw_data(file)

    total_similarity_score = []
    left = []
    right = []
    for value in raw_data:
        left.append(int(value[0]))
        right.append(int(value[1]))

    left.sort()
    right.sort()
    for element in left:
        total_similarity_score.append(element * right.count(element))

    print(f"What is the total similarity score between your lists? {sum(total_similarity_score)}")

if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")