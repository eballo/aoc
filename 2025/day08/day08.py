# Generated on 08-12-2025 07:28
# --- Day 8: Playground ---
import math


def get_raw_data(file: str) -> list[str]:
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def calculate_distance(points: tuple[int, int, int]) -> dict:
    """
    The Euclidean distance formula calculates the straight-line distance
    between two points. For a two-dimensional space with
    points P1(x_1, y_1) and P2(x_2, y_2), the formula
    is d=sqrt((x_2-x_1)^2+(y_2-y_1)^2).
    This can be generalized to any number of dimensions,
    where you sum the squared differences of each corresponding
    coordinate and then take the square root of the total
    """
    edges = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            # Euclidean distance formula
            dist = math.sqrt(
                (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
            )
            edges[dist] = {"point1": p1, "point2": p2, "index1": i, "index2": j}
        return edges


def part_one(file: str, connections: int):
    raw_data = get_raw_data(file)

    points = []
    for line in raw_data:
        x, y, z = map(int, line.split(","))
        points.append((x, y, z))
    print(f"points: x y z : {points}")
    print(f"--total points: {len(points)}")

    # calculate straight-line distance (euclides distance)
    # calculate all distances combination
    # Store as tuple: (distance, index_1, index_2)
    edges = calculate_distance(points)
    print("Euclides distance")
    print(f"--distance, index1, index2 =  {edges}")
    # number of unique pairs (edges) (20*19)/2 = 190
    print(f"--total edges : {len(edges)}")

    # sort by distance (shortest first)
    sorted_edges = dict(sorted(edges.items()))
    print(f"--sorted edges {sorted_edges}")

    for i, (key, values) in enumerate(sorted_edges.items()):
        if i == connections:
            break
        point1 = values["point1"]
        index1 = values["index1"]
        point2 = values["point2"]
        index2 = values["index2"]

        print(
            f"Distance: {key:.2f} | Point 1: {point1} | Index 1: {index1} |  Point 2: {point2} | Index 2: {index2}"
        )

    result = 0
    print(
        f"what do you get if you multiply together the sizes of the three largest circuits? {result}"
    )


def part_two(file: str):
    raw_data = get_raw_data(file)

    for value in raw_data:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Example ==")
    part_one("example.txt", 10)

    # print("=== Part 1 Input ==")
    # part_one("input.txt")

    # print("=== Part 2 Input ==")
    # part_two("input.txt")
