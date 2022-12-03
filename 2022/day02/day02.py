from typing import Tuple

GAME = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
}

ENCRYPTED = {
    "A": ('ROCK', 1),
    "B": ('PAPER', 2),
    "C": ('SCISSORS', 3),
    "X": ('ROCK', 1),
    "Y": ('PAPER', 2),
    "Z": ('SCISSORS', 3),
}

ENCRYPTED_RESULT = {
    "X": ('LOSE', 0),
    "Y": ('DRAW', 3),
    "Z": ('WIN', 6),
}

POSSIBILITIES = {
    ('ROCK', 'ROCK'): ('DRAW', 3),
    ('ROCK', 'PAPER'): ('LOSE', 0),
    ('ROCK', 'SCISSORS'): ('WIN', 6),
    ('PAPER', 'ROCK'): ('WIN', 6),
    ('PAPER', 'PAPER'): ('DRAW', 3),
    ('PAPER', 'SCISSORS'): ('LOSE', 0),
    ('SCISSORS', 'ROCK'): ('LOSE', 0),
    ('SCISSORS', 'PAPER'): ('WIN', 6),
    ('SCISSORS', 'SCISSORS'): ('DRAW', 3),

}


def load_file(file: str) -> Tuple[str, int]:
    with open(file, "r") as f:
        for line in f:
            opponent, me = line.split()
            yield opponent, me


def decrypt(opponent: str) -> Tuple[str, int]:
    return ENCRYPTED[opponent]


def calculate_round_score(my_hand, opponent_hand) -> Tuple[str, int]:
    result = POSSIBILITIES[(my_hand[0], opponent_hand[0])]
    return result[0], result[1] + my_hand[1]


def decrypt_result(result: str) -> Tuple[str, int]:
    return ENCRYPTED_RESULT[result]


def get_hand(result: Tuple[str, int], opponent_hand: Tuple[str, int]) -> Tuple[str, int]:
    for key, value in POSSIBILITIES.items():
        if key[1] == opponent_hand[0] and value == result:
            return key[0], GAME[key[0]]


def part_one(file: str):

    total_score = 0
    for opponent, me in load_file(file):
        opponent_hand = decrypt(opponent)
        my_hand = decrypt(me)
        result, round_score = calculate_round_score(my_hand, opponent_hand)
        total_score = total_score + round_score
        # print(f"opponent {opponent} : {opponent_hand[0]} - me {me} : {my_hand[0]} = {result} {round_score}")

    print(f"total score: {total_score}")


def part_two(file: str):
    total_score = 0
    for opponent, encrypted_result in load_file(file):
        opponent_hand = decrypt(opponent)
        expected_result = decrypt_result(encrypted_result)
        my_hand = get_hand(expected_result, opponent_hand)
        result, round_score = calculate_round_score(my_hand, opponent_hand)
        total_score = total_score + round_score
        # print(f"opponent {opponent} : {opponent_hand[0]} - me {my_hand[0]} = {encrypted_result} - {result} {round_score}")

    print(f"total score: {total_score}")


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    print("=== Part 2 Test ==")
    part_two("test.txt")
    print("=== Part 2 Input ==")
    part_two("input.txt")
