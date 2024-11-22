[![Python 3.13][python-shield]][python-url] ![womm](https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg)

# Advent of Code

Advent of Code is an annual coding event that takes place every December. It consists of 25 daily programming puzzles of increasing difficulty, designed to challenge and entertain participants of all skill levels.

## Getting Started
To get started with Advent of Code, simply visit the [Advent of Code website](https://adventofcode.com/) and sign in with your account or create a new one if you haven't already. Once logged in, you'll be able to access the current year's puzzles as well as previous years' puzzles.

## What can you find in here ?
Here you can find the collection of python solutions for each year and day that I have done for AOC.

### Files structure
The repository is organised by year, and we can find a python file for each day.
Each file has a method for `part_one()` and `part_two()`.

```shell
└── 2015/
    ├── day01/
    │   ├── day01.py
    │   day02/
    │   ├── day02.py
    │   ├── ...
    └── ...
```

**NOTE:** the input data is not in the repository, you will need to use your own input file if you want to test it.

## Development setup
1 - Create a virtual environment using the latest python version and activate the environment

```shell
pyenv install 3.13.0
pyenv virtualenv 3.13.0 aoc
pyenv local aoc
```
2 - Install the requirements
```shell
pip install -r requirements.txt
```
3 - Have fun!

### Quick start template
**NOTE:** We are using [AOCD](https://pypi.org/project/advent-of-code-data/) python package, the token needs to be setup in order to work
`.config/aocd/token`

We can run the command:
```shell
 make run
```
Will ask you few questions and after that will create a directory for the year and the day and download the input data to work with.
```shell
$> make run                                                                                                               ok | aoc 3.10.13 py | 10:41:53
python utils/create_template_and_input_data.py
Year (2024): 2015
Day (2): 3
Directory '/Users/XXX/Documents/work/python/aoc/2015/day03' created successfully.
Data successfully created.
Template copied to '/Users/XXX/Documents/work/python/aoc/2015/day03/day3.py
```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-shield]: https://img.shields.io/badge/python-3.13-blue.svg
[python-url]: https://www.python.org/downloads/release/python-3130/