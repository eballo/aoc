import os
from aocd import get_data
import shutil


def get_full_directory_ppath(day, directory_path, year):
    return directory_path + '/' + year + '/day' + day.rjust(2, "0")


def create_directory(full_directory_path):
    if not os.path.exists(full_directory_path):
        os.makedirs(full_directory_path)
        print(f"Directory '{full_directory_path}' created successfully.")
    else:
        print(f"Directory '{full_directory_path}' already exists - SKIP")


def create_file_from_template(directory_path: str, full_directory_path: str, day: str) -> None:
    template = directory_path + "/template/dayXX.py"
    destination = full_directory_path + f"/day{day}.py"
    if not os.path.exists(destination):
        shutil.copy(template, destination)
        print("Template copied to '" + destination + "")
    else:
        print("Template not copied - File already exists - SKIP")


def create_input_data(directory_path: str, year: str, day: str) -> None:
    input_file = directory_path + "/input.txt"
    if not os.path.exists(input_file):
        data = get_data(day=int(day), year=int(year))
        if data:
            file_path = os.path.join(directory_path, "input.txt")
            with open(file_path, 'w') as file:
                file.write(data)
            print("Data successfully created.")
        else:
            print("No data found")
    else:
        print("Input file already exists - SKIP")


def create_data(directory_path: str, year: str, day: str) -> None:
    full_directory_path = get_full_directory_ppath(day, directory_path, year)

    create_directory(full_directory_path)
    create_input_data(full_directory_path, year, day)
    create_file_from_template(directory_path, full_directory_path, day)


if __name__ == '__main__':
    directory_path = '/Users/eballo/Documents/work/python/aoc'
    year = input("Year: ")
    day = input("Day: ")
    create_data(directory_path, year, day)
