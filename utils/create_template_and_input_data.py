import os
from services.aoc_data import get_aoc_input_data
from services.file_utils import get_full_directory_path, create_directory, create_file_from_template
from services.input_data import get_year_and_day


def create_aoc_template(directory_path: str, year_str: str, day_str: str) -> None:
    """
        Set up the directory structure and create the input file if it doesn't exist
    """
    full_directory_path = get_full_directory_path(directory_path, year_str, day_str)

    create_directory(full_directory_path)
    get_aoc_input_data(full_directory_path, year_str, day_str)
    create_file_from_template(directory_path, full_directory_path, year_str, day_str)


if __name__ == '__main__':
    try:
        current_working_directory = os.getcwd()
        year, day = get_year_and_day()

        create_aoc_template(current_working_directory, year, day)
    except KeyboardInterrupt as e:
        exit()
    except Exception as e:
        print(e)
        exit()
