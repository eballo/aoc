import math
from typing import List
from termcolor import colored

# UP, LEFT, RIGHT, DOWN
DIRECTIONS = [(0, -1), (-1, 0), (1, 0), (0, 1)]


class Field:

    def __init__(self, field: List[List[int]]):
        self.field = field
        self.visible_trees = self._initialize_field(len(field))
        self.visible_count = 0

    @staticmethod
    def _initialize_field(length: int) -> List[List[bool]]:
        visible_trees = []
        for x in range(0, length):
            trees = []
            for y in range(0, length):
                trees.append(False)
            visible_trees.append(trees)
        return visible_trees

    def mark_visible_trees(self):
        len_row = len(self.field)
        len_col = len(self.field[0])
        for row in range(len_row):
            for col in range(len_col):
                visible = False
                for (x, y) in DIRECTIONS:
                    c_row = row
                    c_col = col
                    ok = True
                    while True:
                        c_row += x
                        c_col += y
                        if not (0 <= c_row < len_row and 0 <= c_col < len_col):
                            break
                        if self.field[c_row][c_col] >= self.field[row][col]:
                            ok = False
                    if ok:
                        visible = True
                        self.visible_trees[row][col] = True
                if visible:
                    self.visible_count += 1

    def calculate_scenic_score_trees(self) -> int:
        scenic_score = 1
        len_row = len(self.field)
        len_col = len(self.field[0])
        for row in range(len_row):
            for col in range(len_col):
                d = []
                for (x, y) in DIRECTIONS:
                    c_row = row + x
                    c_col = col + y
                    dist = 1
                    while True:
                        if not (0 <= c_row < len_row and 0 <= c_col < len_col):
                            dist -= 1
                            break
                        # print(f" check numbers ", self.field[c_col][c_row], self.field[col][row])
                        if self.field[c_col][c_row] >= self.field[col][row]:
                            break
                        dist += 1
                        c_row += x
                        c_col += y
                    d.append(dist)
                scenic_score = max(scenic_score, math.prod(d))
                # print(row, col, self.field[row][col], d, math.prod(d))
        return scenic_score

    def __str__(self):
        display = ""
        for x in range(0, len(self.field)):
            for y in range(0, len(self.field)):
                if self.visible_trees[x][y]:
                    number = colored(str(self.field[x][y]), 'green', attrs=['bold'])
                else:
                    number = str(self.field[x][y])
                display = display + " " + "".join(number)
            display = display + "\n"
        display = display + "\n"
        return display


def load_file(file: str) -> List[List[int]]:
    field = []
    with open(file, "r") as f:
        for line in f:
            trees = []
            trees_row = line.split()
            for i in range(0, len(trees_row[0])):
                trees.append(int(trees_row[0][i]))
            field.append(trees)
    return field


def part_one(file: str):
    raw_data = load_file(file)

    f = Field(raw_data)
    f.mark_visible_trees()
    # print(f)
    print(f"how many trees are visible from outside the grid? {f.visible_count}")


def part_two(file: str):
    raw_data = load_file(file)

    f = Field(raw_data)
    scenic_score = f.calculate_scenic_score_trees()
    # print(f)
    print(f"What is the highest scenic score possible for any tree? {scenic_score}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
