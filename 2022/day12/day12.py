# Generated on 23-11-2024 19:12
# --- Day 12: Hill Climbing Algorithm ---
import queue
import string
from collections import deque

LOWERCASE = dict(zip(string.ascii_lowercase, range(1, 27)))

class Heightmap:

    def __init__(self, field: list[list[str]]) -> None:
        self.field = field
        self.visited_positions = set()
        self.queue = None

    def get_start_position(self) -> tuple[int,int]:
        return self._get_and_replace_position_for_letter("S", "a")

    def get_end_position(self) -> tuple[int,int]:
        return self._get_and_replace_position_for_letter("E", "z")

    def _get_and_replace_position_for_letter(self, letter: str, replace_letter: str) -> tuple[int,int]:
        for x, row in enumerate(self.field):
            for y, column in enumerate(row):
                if column == letter:
                    self.field[x][y] = replace_letter
                    return x,y

    def find_distance_path_from_all_possible_start_positions(self, start_positions: list[tuple[int,int]], end_position:tuple[int,int]) -> list[int]:
        distance_paths =[]
        for position in start_positions:
            new_distance = self.find_distance_path(position, end_position)
            distance_paths.append(new_distance)
        return distance_paths


    def find_distance_path(self, start_position: tuple[int,int], end_position: tuple[int, int]) -> int:
        self.visited_positions.add(start_position)
        self.queue = deque()
        distance = 1
        self.queue.append((distance, start_position)) # distance, position
        finished = False
        while self.queue or finished:
            if finished:
                break
            distance, position = self.queue.popleft()
            position = self.get_possible_paths(position)
            finished = self.found_position_or_queue(distance, position, end_position, finished)

        return distance

    def found_position_or_queue(self, distance: int, position: list[tuple[int, int]], end_position: tuple[int, int], finished:bool) -> bool:
        for position in position:
            if position == end_position:
                print("position found!")
                finished = True
            else:
                self.visited_positions.add(position)
                self.queue.append((distance + 1, position))
        return finished

    def get_possible_paths(self, position) -> list[tuple[int,int]]:
        # UP, LEFT, RIGHT, DOWN
        DIRECTIONS = [(position[0], position[1] + 1),(position[0] - 1, position[1]),(position[0] + 1, position[1]),(position[0], position[1] - 1)]
        positions = []
        for x_next, y_next in DIRECTIONS:
            # check that we are not in the edge if we are, then continue
            if x_next < 0 or y_next < 0 or x_next >= len(self.field) or y_next >= len(self.field[0]):
                continue
            # check that we did not visit this node yet
            if(x_next, y_next) in self.visited_positions:
                continue
            # check elevation and if the difference is grater than 1 continue
            elevation_number_current = self.field[position[0]][position[1]]
            elevation_number_next = self.field[x_next][y_next]
            if LOWERCASE[elevation_number_next] - LOWERCASE[elevation_number_current] >1:
                continue

            # we have a valid node and was not visit
            positions.append((x_next, y_next))
        return positions

    def get_all_start_possible_positions(self) -> list[tuple[int,int]]:
        start_positions = []
        for x, row in enumerate(self.field):
            for y, column in enumerate(row):
                if column == "S":
                    self.field[x][y] = "a"
                    start_positions.append((x, y))
                if column == "a":
                    start_positions.append((x, y))
        return start_positions

def get_raw_data(file: str) -> list[list[str]]:
    field =[]
    with open(file) as f:
        for line in f:
            height = []
            trees_row = line.split() # remove end of line
            for i in range(0, len(trees_row[0])):
                height.append(str(trees_row[0][i]))
            field.append(height)
    return field


def part_one(file: str):
    raw_data = get_raw_data(file)
    heightmap = Heightmap(raw_data)

    start_position = heightmap.get_start_position()
    end_position = heightmap.get_end_position()
    distance = heightmap.find_distance_path(start_position, end_position)

    print(f"What is the fewest steps required to move from your current position to the location that should get the best signal? {distance}")


def part_two(file: str):
    raw_data = get_raw_data(file)
    heightmap = Heightmap(raw_data)

    start_positions = heightmap.get_all_start_possible_positions()
    end_position = heightmap.get_end_position()
    all_distances_paths = heightmap.find_distance_path_from_all_possible_start_positions(start_positions, end_position)

    print(len(all_distances_paths))
    all_distances_paths.sort()
    print(set(all_distances_paths))
    print(f"What is the fewest steps required to move from your current position to the location that should get the best signal? {all_distances_paths[0]}")



if __name__ == "__main__":
    print("=== Part 1 Input ==")
    part_one("input.txt")

    print("=== Part 2 Input ==")
    part_two("input.txt")