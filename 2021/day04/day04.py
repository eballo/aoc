from typing import List, Tuple
from termcolor import colored


class Board:

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.board_marked = self._initialize_mark(len(board))

    @staticmethod
    def _initialize_mark(length: int) -> List[List[bool]]:
        board_mark = []
        for x in range(0, length):
            mark = []
            for y in range(0, length):
                mark.append(False)
            board_mark.append(mark)
        return board_mark

    def mark(self, number) -> None:
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board)):
                if self.board[x][y] == number:
                    self.board_marked[x][y] = True

    def bingo(self):
        for row_list in range(0, len(self.board_marked)):
            row = [value for value in self.board_marked[row_list]]
            if all(row):
                return True
            else:
                continue
        return False

    def sum_unmarked_numbers(self) -> int:
        total = 0
        for x in range(0, len(self.board_marked)):
            for y in range(0, len(self.board_marked)):
                if not self.board_marked[x][y]:
                    total = total + self.board[x][y]
        return total

    def __str__(self):
        display = ""
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board)):
                if self.board_marked[x][y]:
                    number = colored(str(self.board[x][y]), 'green', attrs=['bold'])
                else:
                    number = str(self.board[x][y])
                display = display + " " + "".join(number)
            display = display + "\n"
        display = display + "\n"
        return display


def load_file(file: str) -> Tuple[List[int], List[Board]]:
    with open(file, "r") as f:
        lines = f.readlines()
        numbers = [int(number) for number in lines[0].split(',')]

        # print(numbers)
        list_of_boards = []
        boards = []
        for line in lines[1:]:
            if line.strip() == "":
                if len(boards) > 0:
                    board = Board(boards)
                    list_of_boards.append(board)
                boards = []
            else:
                n = [int(number) for number in line.split()]
                boards.append(n)

    return numbers, list_of_boards


def part_one(file: str) -> None:
    numbers, boards = load_file(file)

    wining_board = None
    final_number = -1
    for number in numbers:
        for board in boards:
            board.mark(number)
            if board.bingo():
                print("BINGO!!")
                wining_board = board
                break
        if wining_board:
            final_number = number
            break

    print(wining_board)
    total = wining_board.sum_unmarked_numbers()
    print(f"Sum unmarked numbers - wining board : {total}")
    print(f"score: {final_number*total}")


def part_two(file: str) -> None:
    numbers, boards = load_file(file)

    final_number = -1
    wining_boards = []
    for number in numbers:
        # print(f"{number}\n")
        final_number = number
        if len(wining_boards) == len(boards) - 1:
            break
        for x in range(0, len(boards)):
            boards[x].mark(number)
            if boards[x].bingo() and boards[x] not in wining_boards:
                print("BINGO!!")
                wining_boards.append(boards[x])

    print(wining_boards)
    last_board = [board for board in boards if board not in wining_boards]
    print(last_board)
    last_board = last_board[0]
    print(final_number)

    last_board.mark(final_number)
    print(last_board)
    total = last_board.sum_unmarked_numbers()
    print(f"Sum unmarked numbers - wining board : {total}")
    print(f"score: {final_number * total}")


if __name__ == '__main__':
    print("-------- Part One -------")
    # part_one("test.txt")
    # part_one("input.txt")
    # print("")
    # print("-------- Part Two -------")
    # part_two("test.txt")
    part_two("input.txt")
