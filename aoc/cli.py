from pathlib import Path
from typing import Optional

import typer

from aoc.services.aoc_data import get_aoc_input_data
from aoc.services.file_utils import (
    get_full_directory_path,
    create_directory,
    create_file_from_template,
)
from aoc.services.input_data import get_year_and_day

app = typer.Typer(no_args_is_help=True, help="AOC project helper CLI.")


def create_aoc_template(directory_path: str, year_str: str, day_str: str) -> None:
    """
    Set up the directory structure and create the input file if it doesn't exist.
    """
    full_directory_path = get_full_directory_path(directory_path, year_str, day_str)
    create_directory(full_directory_path)
    get_aoc_input_data(full_directory_path, year_str, day_str)
    create_file_from_template(directory_path, full_directory_path, year_str, day_str)


@app.command("create", help="Create folder/files and fetch input for a given year/day.")
def create(
    year: Optional[str] = typer.Option(
        None, "--year", "-y", help="AOC year (e.g., 2023). If omitted, you'll be prompted."
    ),
    day: Optional[str] = typer.Option(
        None, "--day", "-d", help="AOC day (1–25). If omitted, you'll be prompted."
    ),
    directory: Path = typer.Option(
        Path.cwd(),
        "--dir",
        "-C",
        exists=True,
        file_okay=False,
        writable=True,
        resolve_path=True,
        help="Base directory for the AOC project (defaults to current directory).",
    ),
) -> None:
    """
    Create the Advent of Code scaffold for the specified year/day.
    """
    try:
        # Allow partial/empty flags and fall back to your existing prompt function.
        if year is None or day is None:
            y, d = get_year_and_day()
            year = year or y
            day = day or d

        # Normalize to strings in case the prompt returned ints, etc.
        year = str(year)
        day = str(day)

        create_aoc_template(str(directory), year, day)
        typer.secho(
            f"✅ Created AOC template for {year}/day {day} under {directory}", bold=True
        )
    except KeyboardInterrupt:
        raise typer.Abort()
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
