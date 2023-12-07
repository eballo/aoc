from collections import Counter
from typing import Tuple


def load_file(file):
    with open(file) as f:
        values = [line.rstrip() for line in f.readlines()]
    return values

# NOTES:
# Cards:
#   Highest A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2 Lowest
# From strongest to weakest, they are:
# 7- Five of a kind, where all five cards have the same label: AAAAA
# 6- Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 5- Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 4- Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 3- Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 2- One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 1- High card, where all cards' labels are distinct: 23456


def get_strength(hand: str) -> Tuple[int, str, str]:
    """Return the strength of the hand and the hand itself."""

    # Replace the letters the next char in the alphabet after 9
    # this way we can sort them good

    new_hand = hand.replace("T", chr(ord('9') + 1))
    new_hand = new_hand.replace("J", chr(ord('9') + 2))
    new_hand = new_hand.replace("Q", chr(ord('9') + 3))
    new_hand = new_hand.replace("K", chr(ord('9') + 4))
    new_hand = new_hand.replace("Q", chr(ord('9') + 5))

    counter = Counter(new_hand)
    # Five of a kind
    if list(counter.values()) == [5]:
        return 7, new_hand, hand
    # Four of a kind
    elif sorted(counter.values()) == [1, 4]:
        return 6, new_hand, hand
    # Full house
    elif sorted(counter.values()) == [2, 3]:
        return 5, new_hand, hand
    # Three of a kind
    elif sorted(counter.values()) == [1, 1, 3]:
        return 4, new_hand, hand
    # Two pair
    elif sorted(counter.values()) == [1, 2, 2]:
        return 3, new_hand, hand
    # One pair
    elif sorted(counter.values()) == [1, 1, 1, 2]:
        return 2, new_hand, hand
    # High card
    elif sorted(counter.values()) == [1, 1, 1, 1, 1]:
        return 1, new_hand, hand
    else:
        raise ValueError(f"Invalid hand {hand} {new_hand} - {counter.values()}")


def part_one(file: str):
    raw_values = load_file(file)

    game = []
    for camel_cards in raw_values:
        hand = camel_cards.split(" ")[0]
        bid = int(camel_cards.split(" ")[1])
        game.append((hand, bid))

    total_winning = 0
    game = sorted(game, key=lambda x: get_strength(x[0]))
    for i, (hand, bid) in enumerate(game):
        print(f"{i+1} - {hand} - {bid} - {get_strength(hand)}")
        total_winning += (i+1) * bid

    print(total_winning)


def part_two(file: str):
    raw_values = load_file(file)

    for value in raw_values:
        print(value)


if __name__ == "__main__":
    print("=== Part 1 Test ==")
    part_one("test.txt")
    print("=== Part 1 Input ==")
    part_one("input.txt")
    # print("=== Part 2 Test ==")
    # part_two("test.txt")
    # print("=== Part 2 Input ==")
    # part_two("input.txt")
