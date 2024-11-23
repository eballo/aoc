import os
from datetime import datetime

from jinja2 import Template

from .aoc_parser import get_advent_of_code_title


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


def load_template(template: str) -> Template:
    with open(template) as file_:
        template = Template(file_.read())
    return template


def create_file_from_template(directory_path: str, full_directory_path: str, year:str, day: str) -> None:
    """ Create a template file to the new created directory if it doesn't exist """
    padding_day = add_left_padding(day)
    rendered_content = get_rendered_content_template(year, day, directory_path)
    destination = full_directory_path + f"/day{padding_day}.py"
    if not os.path.exists(destination):
        with open(destination, "w") as f:
            f.write(rendered_content.strip())
        print("Template copied to '" + destination + "")
    else:
        print("Template not copied - File already exists - SKIP")


def get_rendered_content_template(year:str, day: str, directory_path: str) -> str:
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    custom_comment = f"Generated on {today}"
    title = get_advent_of_code_title(day, year)

    template = directory_path + "/template/dayXX.jinja"
    jinja_template = load_template(template)

    rendered_content = jinja_template.render(
        title=title,
        comment=custom_comment)

    return rendered_content