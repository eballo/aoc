import datetime
import os
from typing import Tuple

from aocd import get_data
import shutil

from aocd.exceptions import PuzzleLockedError


def add_left_padding(day: str) -> str:
    """ Add a padding of 2 with 0 if needed """
    return day.rjust(2, "0")


def get_full_directory_path(directory_path: str, year: str, day: str) -> str:
    """ Returns the full directory path for a given year and day """
    return directory_path + '/' + year + '/day' + add_left_padding(day)


def create_directory(full_directory_path: str) -> None:
    """ Creates the full directory path if it doesn't exist """
    if not os.path.exists(full_directory_path):
        os.makedirs(full_directory_path)
        print(f"Directory '{full_directory_path}' created successfully.")
    else:
        print(f"Directory '{full_directory_path}' already exists - SKIP")


def create_file_from_template(directory_path: str, full_directory_path: str, day: str) -> None:
    """ Copies a template file to the full directory if it doesn't exist """
    padding_day = add_left_padding(day)
    template = directory_path + "/template/dayXX.py"
    destination = full_directory_path + f"/day{padding_day}.py"
    if not os.path.exists(destination):
        shutil.copy(template, destination)
        print("Template copied to '" + destination + "")
    else:
        print("Template not copied - File already exists - SKIP")


def create_input_data(directory_path: str, year: str, day: str) -> None:
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


def create_data(directory_path: str, year: str, day: str) -> None:
    """
        Set up the directory structure and create the input file if it doesn't exist
    """
    full_directory_path = get_full_directory_path(directory_path, year, day)

    create_directory(full_directory_path)
    create_input_data(full_directory_path, year, day)
    create_file_from_template(directory_path, full_directory_path, day)


def get_year_and_day() -> Tuple[str, str]:
    default_day = datetime.datetime.now().day
    default_year = datetime.datetime.now().year
    try:
        year = input(f"Year ({default_year}): ")
        day = input(f"Day ({default_day}): ")
    except KeyboardInterrupt:
        exit()

    if not year:
        year = str(default_year)
    if not day:
        day = str(default_day)

    return year, day


if __name__ == '__main__':

    current_working_directory = os.getcwd()     # get the current working directory
    year, day = get_year_and_day()

    create_data(current_working_directory, year, day)
