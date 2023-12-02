def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values


class Game:

    def __init__(self, raw_line_game):
        self.game_id = None
        self.sets_of_cubes = None
        self.raw_game = raw_line_game
        self.set_of_totals = []

    def parse_game(self):
        game_section = self.raw_game.split(":")[0]
        self.sets_of_cubes = self.raw_game.split(":")[1].split(";")
        self.game_id = self._get_game_id(game_section)
        self._calculate_total()
        return self

    @staticmethod
    def _get_game_id(game_section):
        return int(''.join(i for i in game_section if i.isdigit()))

    def __str__(self):
        return f"Game {self.game_id} - {self.set_of_totals}"

    def _calculate_total(self) -> [dict]:
        for set_of_cubes in self.sets_of_cubes:
            total = self._calculate_set_total(set_of_cubes)
            self.set_of_totals.append(total)

    @staticmethod
    def _calculate_set_total(set_of_cubes: str) -> dict:
        cubes = set_of_cubes.split(",")
        total = {
            "green": 0,
            "red": 0,
            "blue": 0,
        }
        for cube in cubes:
            set_value = int(cube.strip().split(" ")[0])
            set_color = cube.strip().split(" ")[1]
            total[set_color] += set_value
        return total


def part_one(file: str):
    raw_lines = load_file(file)

    games = []
    for raw_line in raw_lines:
        # print(raw_line)
        games.append(Game(raw_line).parse_game())

    game_ids = []
    for game in games:
        possible = True
        for set_of_totals in game.set_of_totals:
            print(set_of_totals)
            for color, total in set_of_totals.items():
                print(f"{color}: {total}")
                if (color == "red" and total > 12) and possible:
                    print(f"Game {game.game_id} is Impossible!")
                    possible = False
                if (color == "green" and total > 13) and possible:
                    print(f"Game {game.game_id} is Impossible!")
                    possible = False
                if (color == "blue" and total > 14) and possible:
                    print(f"Game {game.game_id} is Impossible!")
                    possible = False
        if possible:
            print(f"Game {game.game_id} is Possible!")
            game_ids.append(game.game_id)

    print(f"Game IDs: {game_ids}")
    total = sum(game_ids)
    print(f"Total: {total}")


def part_two(file: str):
    raw_lines = load_file(file)

    games = []
    for raw_line in raw_lines:
        # print(raw_line)
        games.append(Game(raw_line).parse_game())

    game_ids = []
    power = 0
    for game in games:
        max_color = {
            "green": 0,
            "red": 0,
            "blue": 0,
        }
        for set_of_totals in game.set_of_totals:
            print(set_of_totals)
            for color, total in set_of_totals.items():
                print(f"{color}: {total}")
                if color == "red":
                    if total > max_color["red"]:
                        max_color["red"] = total
                if color == "green":
                    if total > max_color["green"]:
                        max_color["green"] = total
                if color == "blue":
                    if total > max_color["blue"]:
                        max_color["blue"] = total

        power += max_color["red"] * max_color["green"] * max_color["blue"]

    print(f"Total: {power}")


if __name__ == "__main__":
    # print("=== Part 1 Test ==")
    # part_one("test.txt")
    # print("=== Part 1 Input ==")
    # part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
