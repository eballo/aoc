from typing import Optional

import requests
from bs4 import BeautifulSoup


def get_advent_of_code_title(day: str, year: str) -> Optional[str]:
    url = f"https://adventofcode.com/{year}/day/{day}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("h2")
        title = None
        if title_tag:
            title = title_tag.text.strip()
        return title
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")