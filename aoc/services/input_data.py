from datetime import datetime
from typing import Tuple


def get_year_and_day() -> Tuple[str, str]:
    default_day = datetime.now().day
    default_year = datetime.now().year

    # Ask for user input
    try:
        year = input(f"Year ({default_year}): ")
        day = input(f"Day ({default_day}): ")
    except KeyboardInterrupt as key:
        raise key

    #If no data default input
    if not year:
        year = str(default_year)
    if not day:
        day = str(default_day)

    # validate year and day
    if int(year) < 2015:
        raise ValueError("ERROR - Wrong year - Advent of Code started on 2015")
    if int(day) > 25:
        raise ValueError("ERROR - Wrong day - Advent of Code only runs from December 1st to 25th")

    return year, day