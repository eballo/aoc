import os
from aocd import get_data
from aocd.exceptions import PuzzleLockedError


def get_aoc_input_data(directory_path: str, year: str, day: str) -> None:
    """
    if the input data is not present will try to download it from AOC
    web page using aocd library
    """
    input_file = directory_path + "/input.txt"
    if not os.path.exists(input_file):
        try:
            data = get_data(day=int(day), year=int(year))
            if data:
                file_path = os.path.join(directory_path, "input.txt")
                with open(file_path, 'w') as file:
                    file.write(data)
                print("Data successfully created.")
            else:
                print("No data found")
        except PuzzleLockedError:
            print("Error - Puzzle data is not available")
    else:
        print("Input file already exists - SKIP")