from itertools import permutations


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


def get_distances_dict(raw_values) -> dict:
    # create a dictionary that stores the distances between each pair of cities
    distances = {}
    for value in raw_values:
        # parts = ['Faerun', 'to', 'Norrath', '129']
        parts = value.split()
        city1, city2 = parts[0], parts[2]
        distance = int(parts[4])
        # print(distance, city1, city2)
        if city1 not in distances:
            distances[city1] = {}
        if city2 not in distances:
            distances[city2] = {}
        distances[city1][city2] = distance
        distances[city2][city1] = distance
    return distances


def calculate_route_distance(route, distances):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))


def find_shortest_route(distances):
    cities = list(distances.keys())
    shortest_distance = float('inf')  # infinite value
    shortest_route = None
    for route in permutations(cities):
        # sample route: ('Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight')
        distance = calculate_route_distance(route, distances)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route
    return shortest_distance, shortest_route


def find_longest_route(distances):
    cities = list(distances.keys())
    longest_distance = float(0)  # zero value
    longest_route = None
    for route in permutations(cities):
        # sample route: ('Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight')
        distance = calculate_route_distance(route, distances)
        if distance > longest_distance:
            longest_distance = distance
            longest_route = route
    return longest_distance, longest_route

def part_one(file: str):
    raw_values = load_file(file)

    print(raw_values)
    distances = get_distances_dict(raw_values)
    shortest_distance, shortest_route = find_shortest_route(distances)
    print(f"Shortest route distance is {shortest_distance} with route {shortest_route}")


def part_two(file: str):
    raw_values = load_file(file)

    print(raw_values)
    distances = get_distances_dict(raw_values)
    longest_distance, longest_route = find_longest_route(distances)
    print(f"Longest route distance is {longest_distance} with route {longest_route}")


if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")
